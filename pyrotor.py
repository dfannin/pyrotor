#!/usr/bin/env python3

from PyQt5 import QtGui, QtCore, QtWidgets

import configparser
import argparse
import sys
import pathlib
import math
import random
import logging

logger = logging.getLogger('main')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)8s, %(name)s,  %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

from rotor  import *
from config import *
from rotctl import *
from about  import *

class RotorVars(object):
    def __init__(self,filename=None):
        logger.debug("init rotorvars")
        super().__init__()
        self.RC = {}
        self.RC['filename'] = filename
        self.setRotorVarsDefault()
        self.setConfigDir()
        if filename is not None:
            self.RC = self.readConfigFile(self.RC)

    def setRotorVarsDefault(self):
        logger.debug("setdefault rotorvars")
        self.RC['devserial'] = '/dev/ttyACM0'
        self.RC['poll'] =  1000
        self.RC['nettype'] = '2'
        self.RC['port'] = '4533'
        self.RC['modelid'] = '603'
        self.RC['path'] = '/usr/bin/rotctld'
        self.RC['baud'] = 3  # combo box , 3 entry = 9600
        self.RC['title'] = 'Rotor Display'
        self.RC['startrc'] = 0  # start up rotctld 
        self.RC['rotctlp'] = None

    def setConfigDir(self):
        logger.debug("setconfigdir")
        try:
            self.RC['defdotdir'] = os.path.join(os.path.expanduser("~"),'.config','pyrotor') 
            if not os.path.exists(self.RC['defdotdir']):
                logger.debug("created config dir %s" % (self.RC['defdotdir']))
                os.makedirs(self.RC['defdotdir'],0o755) 

        except OSError as e:
            logger.debug("Error accessing .config/pyrotor directory")


    @staticmethod
    def readConfigFile(RC):
        logger.debug("readconfigfile rotorvars")
        config = configparser.ConfigParser()
        try:
            cfname = os.path.join(RC['defdotdir'],RC['filename'])
            with open(cfname) as f:
                config.read_file(f)
        except IOError:
            logger.error("config file %s does not exist or opened" % (cfname))
            return RC

        allowed = ['devserial','poll','nettype','port','modelid','path','baud','title','startrc' ]
        allowed_intval = ['poll','baud','startrc' ] 

        for ckey in config['DEFAULT']:
            if ckey in allowed:
                if ckey in allowed_intval:
                    RC[ckey] = int(config['DEFAULT'][ckey])
                else:
                    RC[ckey] = config['DEFAULT'][ckey] 
        return RC

    @staticmethod
    def writeConfigFile(RC):
        RCcopy = RC.copy()
        logger.debug("writeconfigfile rotorvars")
        config = configparser.ConfigParser()
        cfname = os.path.join(RCcopy['defdotdir'], RCcopy['filename'])
        del RCcopy['filename']
        del RCcopy['rotctlp']
        del RCcopy['defdotdir']
        config['DEFAULT'] = RCcopy
        try:
            with open(cfname,'w') as configfile:
                config.write(configfile) 
        except IOError:
            logger.error("config file %s write failure" % (cfname))


class Db_Config(QtWidgets.QDialog, Ui_Config):
    def __init__(self, RC):
        super().__init__()
        self.setupUi(self)
        self.RC = RC.copy()
        self.updateFromRC()

    def updateFromRC(self):
        self.LeModelId.setText(self.RC['modelid']) 
        self.LeRcPort.setText(self.RC['port']) 
        self.LeRcExePath.setText(self.RC['path'])
        self.LeRcPollRate.setText(str(self.RC['poll'])) 
        self.LeDevSerial.setText(self.RC['devserial'])
        self.LeFilename.setText(self.RC['filename'])
        self.LeMainTitle.setText(self.RC['title'])
        self.CbSpeedSerial.setCurrentIndex(self.RC['baud'])
        self.ChboxRcStartup.setChecked(self.RC['startrc'])


    def LeChanged(self):
        sender = self.sender()
        logger.debug(sender.objectName())
        changed = False 

        if sender.objectName() == 'LeRcPort' and \
                sender.text() != self.RC['port']:
            changed = True
            self.RC['port'] = sender.text()

        if sender.objectName() == 'LeRcPollRate' and \
                sender.text() != str(self.RC['poll']):
            changed = True
            v = int(sender.text())
            if v < 250 or v > 99999:
                logger.warn("rcpollrate value out of range, resetting")
                sender.setText('100')
                self.RC['poll'] = 250 
            else:
                self.RC['poll'] = sender.text()

        if sender.objectName() == 'LeModelId' and \
                sender.text() != self.RC['modelid']:
            changed = True
            self.RC['modelid'] = sender.text()

        if sender.objectName() == 'LeRcExePath' and \
                sender.text() != self.RC['path']:
            changed = True
            self.RC['path'] = sender.text()

        if sender.objectName() == 'LeDevSerial' and \
                sender.text() != self.RC['devserial']:
            changed = True
            self.RC['devserial'] = sender.text()

        if sender.objectName() == 'LeFilename' and \
                sender.text() != self.RC['filename']:
            changed = True
            self.RC['filename'] = sender.text()

        if sender.objectName() == 'LeMainTitle' and \
                sender.text() != self.RC['title']:
            changed = True
            self.RC['title'] = sender.text()

        if changed:
            msg = "Config object [%s] modified to [%s]" % (sender.objectName(), sender.text() ) 
            logger.debug(msg) 
            self.PteRcLog.appendPlainText(msg)


    def PbSave_Clicked(self):
        logger.debug('save clicked') 
        self.RC['baud'] = self.CbSpeedSerial.currentIndex()
        RotorVars.writeConfigFile(self.RC) 
        self.PteRcLog.appendPlainText('config saved to %s' % (self.RC['filename']))

    def PbOpen_Clicked(self):
        logger.debug('open clicked') 
        self.RC = RotorVars.readConfigFile(self.RC)
        self.updateFromRC()
        self.PteRcLog.appendPlainText('configuration file %s opened' % (self.RC['filename']))

    def ChboxRcStartup_StateChange(self,int):
        logger.debug('rcstarup clicked') 
        if self.ChboxRcStartup.isChecked():
            self.RC['startrc'] = 1
        else:
            self.RC['startrc'] = 0
        self.PteRcLog.appendPlainText('start rotctld set to %d' % (self.RC['startrc']))

    def PbRcTest_Clicked(self):
        logger.debug('rotctl test clicked') 
        if self.RC['rotctlp']:
            if self.RC['rotctlp'].show() == 0 :
                self.PteRcLog.appendPlainText('rotctld pid %d is running' % (self.RC['rotctlp'].rcprocess.pid) ) 
                return 
        self.PteRcLog.appendPlainText('rotctld is not running') 
        logger.info(self.RC['devserial'] ) 
        p = pathlib.Path(self.RC['devserial'])
        if p.is_char_device():
            self.PteRcLog.appendPlainText('serial dev %s exists' % ( p ) )  
        else:
            self.PteRcLog.appendPlainText('serial dev %s does not exist' % ( p ) )  


    def PbRcStart_Clicked(self):
        logger.debug('rotctl start clicked') 

        if self.RC['rotctlp']:
            logger.debug("rotctld already exists")
            self.PteRcLog.appendPlainText('rotctld already exists')
            return 

        self.RC['rotctlp'] = RotCtl(self.RC) 
        self.RC['rotctlp'].start() 
        self.PteRcLog.appendPlainText('start rotctld pid %d' % (self.RC['rotctlp'].rcprocess.pid))

    def PbRcStop_Clicked(self):
        logger.debug('rotctl stop clicked') 
        if self.RC['rotctlp']:
            self.PteRcLog.appendPlainText('stop rotctld pid %d' % (self.RC['rotctlp'].rcprocess.pid))
            self.RC['rotctlp'].stop()
        else:
            self.PteRcLog.appendPlainText('rotctld doesnt exist')
        self.RC['rotctlp'] = None

class Db_About(QtWidgets.QDialog, Ui_About):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class RotorMain(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,rotorvars):
        super().__init__()
        self.setupUi(self)
        self.RC = rotorvars.RC.copy()
        self.actionConfig.triggered.connect(self.showConfig) 
        self.actionAbout.triggered.connect(self.showAbout) 
        self.actionExit.triggered.connect(self.close) 
        self.actionUpdate.toggled.connect(self.updateToggled)
        self.actionLock.toggled.connect(self.lockToggled)
        self.labeltitle.setText(self.RC['title'])
        self.sbdelay = 10000
        self.statusbar.showMessage("Hello, World",self.sbdelay)
        self.azimuth = 0 

        if self.RC['startrc']:
            self.RC['rotctlp'] = RotCtl(self.RC) 
            self.RC['rotctlp'].start() 
            self.statusbar.showMessage("rotctld autostarted",self.sbdelay)

        self.updateTimer = QtCore.QTimer()
        self.updateTimer.timeout.connect( self.updateDisplay)
        self.updateTimer.start(self.RC['poll'])


    def showConfig(self):
        logger.debug('showConfig enter') 

        utstore = True

        if self.updateTimer.isActive():
            self.updateTimer.stop()
        else:
            utstore = False
            
        self.statusbar.showMessage("Editing Config, Update Suspended",self.sbdelay)
        config = Db_Config(self.RC) 
        if  config.exec_() == QtWidgets.QDialog.Accepted:
            logger.debug('showConfig update RC vars')
            self.RC['modelid'] = config.LeModelId.text()
            self.RC['port'] = config.LeRcPort.text()
            self.RC['path'] = config.LeRcExePath.text()
            self.RC['poll'] = int(config.LeRcPollRate.text())
            self.RC['devserial'] = config.LeDevSerial.text()
            self.RC['baud'] = config.CbSpeedSerial.currentIndex()
            self.RC['filename'] = config.LeFilename.text()
            self.RC['title'] = config.LeMainTitle.text()
            self.RC['rotctlp'] = config.RC['rotctlp'] 
            self.labeltitle.setText(self.RC['title'])
            if config.ChboxRcStartup.isChecked():
                self.RC['startrc'] =  1
            else:
                self.RC['startrc'] =  0
            self.statusbar.showMessage('Update Config',self.sbdelay)
        else:
            self.statusbar.showMessage('Update Config Cancelled',self.sbdelay)

        if utstore:
            self.updateTimer.start(self.RC['poll'])

    def showAbout(self):
        logger.debug('showAbout enter') 
        about = Db_About()
        if  about.exec_() == QtWidgets.QDialog.Accepted:
            pass
        logger.debug('showAbout finished')

    def updateDisplay(self): 
        logger.debug('update display')
        retval = RCGetPosition(self.RC)
        if retval >= 0:
            self.azimuth = retval
        else:
            self.azimuth = 0 
            self.statusbar.showMessage('rotctl poll failed err: %d' % (retval),self.sbdelay)
            logger.debug('rotctl poll failed err: %d' % (retval)) 

        self.labelaz.setText( "%03d %s" % (self.azimuth,self.compassDir()) ) 
        self.compass() 

    def compassDir(self):
        a = self.azimuth
        if a <= 11:
            return 'N'
        elif a <= 33:
            return 'NNE'
        elif a <= 56:
            return 'NE'
        elif a <= 78:
            return 'ENE'
        elif a <= 101:
            return 'E'
        elif a <= 123:
            return 'ESE'
        elif a <= 146:
            return 'SE'
        elif a <= 168:
            return 'SSE'
        elif a <= 191:
            return 'S'
        elif a <= 213:
            return 'SSW'
        elif a <= 236:
            return 'SW'
        elif a <= 258:
            return 'WSW'
        elif a <= 281:
            return 'W'
        elif a <= 303:
            return 'WNW'
        elif a <= 326:
            return 'NW'
        elif a <= 348:
            return 'NNW'
        else:
            return 'N'


    def compass(self):
        logger.debug('draw compass')
        if hasattr(self,'scene'):
            self.scene.clear()
        else:
            self.scene = QtWidgets.QGraphicsScene(self)
            self.GvCompass.setScene(self.scene)
            self.GvCompass.setRenderHints(QtGui.QPainter.HighQualityAntialiasing)
            self.GvCompass.scale(1.6,1.6)

        colorLG = QtGui.QColor()
        colorLG.setNamedColor("#EFEFEF")
        penLG = QtGui.QPen(colorLG) 
        brushLG = QtGui.QBrush(colorLG) 

        colorDG = QtGui.QColor()
        colorDG.setNamedColor("#0A0A0A")
        penDG = QtGui.QPen(colorDG,1,QtCore.Qt.SolidLine) 
        brushDG = QtGui.QBrush(colorDG) 

        colorR = QtGui.QColor()
        colorR.setNamedColor("#990033")
        penR = QtGui.QPen(colorR)
        penR2 = QtGui.QPen(colorR,2)
        brushR = QtGui.QBrush(colorR) 

        colorG = QtGui.QColor()
        colorG.setNamedColor("#588C7E")
        penG = QtGui.QPen(colorG,4)
        brushG = QtGui.QBrush(colorG) 

        if self.actionLock.isChecked():
            font =  QtGui.QFont("Calibri",10) 
            textLocked = QtWidgets.QGraphicsSimpleTextItem("Rotor Locked") 
            textLocked.setFont(font)
            textLocked.setPos(-100,-60)
            self.scene.addItem(textLocked) 

        # draw compass circles
        self.scene.addEllipse(-50,-50,100,100,penG,brushLG) 
        self.scene.addEllipse(-2,-2,4,4,penDG,brushDG) 

        # draw compass hash marks
        r = 50
        for i in range(0,12): 
            if i % 3 == 0:
                inset = 0.2 * r 
                outset = 0.2 * r
                pen = penR2
            else:
                inset = 0.15 * r
                outset = 0 
                pen = penDG

            x1 = (r - inset) * math.cos(i * math.pi / 6) 
            y1 = (r - inset) * math.sin(i * math.pi / 6) 
            x2 = (r + outset)* math.cos(i * math.pi / 6) 
            y2 = (r + outset)* math.sin(i * math.pi / 6) 
            self.scene.addLine(x1,y1,x2,y2,pen) 

        # draw compass text
        font =  QtGui.QFont("Calibri",10,QtGui.QFont.Bold) 
        textS = QtWidgets.QGraphicsSimpleTextItem("S") 
        textS.setFont(font)
        textS.setPos(-4,60)
        self.scene.addItem(textS) 

        textN = QtWidgets.QGraphicsSimpleTextItem("N") 
        textN.setFont(font)
        textN.setPos(-4,-73)
        self.scene.addItem(textN) 

        textE = QtWidgets.QGraphicsSimpleTextItem("E") 
        textE.setFont(font)
        textE.setPos(63,-5)
        self.scene.addItem(textE) 

        textW = QtWidgets.QGraphicsSimpleTextItem("W") 
        textW.setFont(font)
        textW.setPos(-74,-5)
        self.scene.addItem(textW) 


        #  draw arrow and pointer
        penR5 = QtGui.QPen(colorR,3)
        pointer = self.scene.addLine(0,6,0,32,penR5) 
        pointer.setRotation( (self.azimuth + 180 ) % 360)

        # arrow head polygon
        arrowpts= QtGui.QPolygonF( [QtCore.QPointF(0,45), \
                                   QtCore.QPointF(-4,30), \
                                   QtCore.QPointF(0,35), \
                                   QtCore.QPointF(4,30) ] ) 
        arrow = self.scene.addPolygon(arrowpts,penR,brushR) 
        arrow.setRotation( (self.azimuth + 180 ) % 360)

    def updateToggled(self):
        logger.debug('update toggled')
        if self.updateTimer.isActive(): 
            if self.actionUpdate.isChecked():
                logger.debug('update timer no action')
            else:
                self.updateTimer.stop()
                self.labelaz.setStyleSheet("QLabel {background-color: red; color:black;}")
                self.statusbar.showMessage('polling stopped',self.sbdelay)
                logger.debug('update timer stopped')
        else:
            if self.actionUpdate.isChecked():
                self.updateTimer.start(self.RC['poll'])
                self.labelaz.setStyleSheet("")
                self.statusbar.showMessage('polling restarted',self.sbdelay)
                logger.debug('update timer restarted')
            else:
                self.updateTimer.stop()
                logger.debug('update time no action')

    def lockToggled(self):
        logger.debug('lock toggled')
        if self.actionLock.isChecked():
            self.statusbar.showMessage('rotor locked',self.sbdelay)
        else:
            self.statusbar.showMessage('rotor unlocked',self.sbdelay)

    def PbMoveToPos_Clicked(self):
        logger.debug('pb move to pos clicked')
        if self.actionLock.isChecked():
            self.statusbar.showMessage('rotor locked',self.sbdelay)
            return

        sender = self.sender()
        position = str(int(sender.objectName().split('_',1)[-1]))

        retval = RCmoveToPosition(self.RC,position) 
        if retval == 0:
            self.statusbar.showMessage('rotctl move to pos %s' % (position),self.sbdelay)
        else:
            self.statusbar.showMessage('rotctl move to pos err %d' % (retval),self.sbdelay)


    def PbMove_Clicked(self):
        logger.debug('pb move clicked')
        if self.actionLock.isChecked():
            self.statusbar.showMessage('rotor locked',self.sbdelay)
            return
        sender = self.sender()
        if sender.objectName() == 'pb_cw':
            retval = RCmove(self.RC,"CW") 
        elif sender.objectName() == 'pb_ccw':
            retval = RCmove(self.RC,"CCW")
        else:
            return

        if retval == 0:
            self.statusbar.showMessage('rotctl moving',self.sbdelay)
        else:
            self.statusbar.showMessage('rotctl moving dir err %d' % (retval),self.sbdelay)


    def PbStop_Clicked(self):
        logger.debug('pb stop clicked')
        sender = self.sender()
        logger.debug(sender.objectName())

        retval = RCStop(self.RC)

        if retval >= 0:
            logger.debug('pbstop successful')
        else:
            self.statusbar.showMessage('rotctl stop failed err: %d' % (retval),self.sbdelay)
            logger.debug('rotctl stop failed err: %d' % (retval)) 


class Application(QtWidgets.QApplication):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def cleanUpOnQuit(self):
        logger.debug('cleaning up, then exiting')
        if ui.RC['rotctlp']:
            ui.RC['rotctlp'].stop()
            logger.debug('killed rotctld') 
        else:
            logger.debug('no rotctld') 
            

''' MAIN '''
if __name__ == '__main__':
    #
    # argparse
    #
    parser = argparse.ArgumentParser(description="Antenna Rotor GUI Display")
    parser.add_argument("-v","--version",help="print version number",action="store_true")
    parser.add_argument("-c","--config",help="use ini config file (default pyrotor.ini)",default="pyrotor.ini")
    parser.add_argument("-d","--debug",help="turn on debug logging",action="store_true")
    args = parser.parse_args()

    #
    # logging
    #
    logger.debug('pyrotor start debug')
    logger.debug('pyrotor start info')

    if args.version:
        logger.info("pyrotor version 1.0c") 
        sys.exit(0)

    if args.debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("logging level set to debug")

    if args.config:
        logger.debug("config file set to %s" % (args.config))
        cfname = args.config
    #
    # 
    #
    rotorconfig = RotorVars(filename=cfname) 

    app = Application(sys.argv)
    app.aboutToQuit.connect(app.cleanUpOnQuit)
    ui = RotorMain(rotorconfig)
    ui.show()
    sys.exit(app.exec_())

