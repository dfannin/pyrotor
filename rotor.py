# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rotor.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(582, 546)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 550, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labeltitle = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labeltitle.sizePolicy().hasHeightForWidth())
        self.labeltitle.setSizePolicy(sizePolicy)
        self.labeltitle.setMaximumSize(QtCore.QSize(16777215, 120))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.labeltitle.setFont(font)
        self.labeltitle.setAutoFillBackground(False)
        self.labeltitle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labeltitle.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labeltitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labeltitle.setObjectName("labeltitle")
        self.verticalLayout.addWidget(self.labeltitle)
        self.horizontalLayout_azlabels = QtWidgets.QHBoxLayout()
        self.horizontalLayout_azlabels.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_azlabels.setObjectName("horizontalLayout_azlabels")
        self.labelaztext = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelaztext.sizePolicy().hasHeightForWidth())
        self.labelaztext.setSizePolicy(sizePolicy)
        self.labelaztext.setMinimumSize(QtCore.QSize(0, 0))
        self.labelaztext.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.labelaztext.setFont(font)
        self.labelaztext.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelaztext.setObjectName("labelaztext")
        self.horizontalLayout_azlabels.addWidget(self.labelaztext)
        self.labelaz = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelaz.sizePolicy().hasHeightForWidth())
        self.labelaz.setSizePolicy(sizePolicy)
        self.labelaz.setMaximumSize(QtCore.QSize(16777215, 121))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.labelaz.setFont(font)
        self.labelaz.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelaz.setObjectName("labelaz")
        self.horizontalLayout_azlabels.addWidget(self.labelaz)
        self.verticalLayout.addLayout(self.horizontalLayout_azlabels)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pb_ccw = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_ccw.sizePolicy().hasHeightForWidth())
        self.pb_ccw.setSizePolicy(sizePolicy)
        self.pb_ccw.setObjectName("pb_ccw")
        self.verticalLayout_2.addWidget(self.pb_ccw)
        self.pb_stop = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_stop.sizePolicy().hasHeightForWidth())
        self.pb_stop.setSizePolicy(sizePolicy)
        self.pb_stop.setStyleSheet("background-color: rgba(167, 21, 28, 100);")
        self.pb_stop.setObjectName("pb_stop")
        self.verticalLayout_2.addWidget(self.pb_stop)
        self.pb_cw = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_cw.sizePolicy().hasHeightForWidth())
        self.pb_cw.setSizePolicy(sizePolicy)
        self.pb_cw.setObjectName("pb_cw")
        self.verticalLayout_2.addWidget(self.pb_cw)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pb_000 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_000.setObjectName("pb_000")
        self.horizontalLayout_2.addWidget(self.pb_000)
        self.pb_045 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_045.setObjectName("pb_045")
        self.horizontalLayout_2.addWidget(self.pb_045)
        self.pb_090 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_090.setObjectName("pb_090")
        self.horizontalLayout_2.addWidget(self.pb_090)
        self.pb_135 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_135.setObjectName("pb_135")
        self.horizontalLayout_2.addWidget(self.pb_135)
        self.pb_179 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_179.setObjectName("pb_179")
        self.horizontalLayout_2.addWidget(self.pb_179)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pb_360 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_360.setObjectName("pb_360")
        self.horizontalLayout_4.addWidget(self.pb_360)
        self.pb_315 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_315.setObjectName("pb_315")
        self.horizontalLayout_4.addWidget(self.pb_315)
        self.pb_270 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_270.setObjectName("pb_270")
        self.horizontalLayout_4.addWidget(self.pb_270)
        self.pb_225 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_225.setObjectName("pb_225")
        self.horizontalLayout_4.addWidget(self.pb_225)
        self.pb_181 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_181.setObjectName("pb_181")
        self.horizontalLayout_4.addWidget(self.pb_181)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.GvCompass = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        self.GvCompass.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.GvCompass.setLineWidth(1)
        self.GvCompass.setMidLineWidth(4)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 246))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.GvCompass.setBackgroundBrush(brush)
        self.GvCompass.setObjectName("GvCompass")
        self.verticalLayout.addWidget(self.GvCompass)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 582, 25))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuConfig = QtWidgets.QMenu(self.menubar)
        self.menuConfig.setObjectName("menuConfig")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionConfig = QtWidgets.QAction(MainWindow)
        self.actionConfig.setObjectName("actionConfig")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionLock = QtWidgets.QAction(MainWindow)
        self.actionLock.setCheckable(True)
        self.actionLock.setAutoRepeat(False)
        self.actionLock.setObjectName("actionLock")
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setCheckable(True)
        self.actionUpdate.setChecked(True)
        self.actionUpdate.setAutoRepeat(False)
        self.actionUpdate.setObjectName("actionUpdate")
        self.menuAbout.addAction(self.actionAbout)
        self.menuConfig.addAction(self.actionConfig)
        self.menuConfig.addAction(self.actionLock)
        self.menuConfig.addAction(self.actionExit)
        self.menuConfig.addAction(self.actionUpdate)
        self.menubar.addAction(self.menuConfig.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.pb_000.clicked.connect(MainWindow.PbMoveToPos_Clicked)
        self.pb_045.clicked.connect(MainWindow.PbMoveToPos_Clicked)
        self.pb_090.clicked.connect(MainWindow.PbMoveToPos_Clicked)
        self.pb_135.clicked.connect(MainWindow.PbMoveToPos_Clicked)
        self.pb_179.clicked.connect(MainWindow.PbMoveToPos_Clicked)
        self.pb_181.clicked.connect(MainWindow.PbMoveToPos_Clicked)
        self.pb_225.clicked.connect(MainWindow.PbMoveToPos_Clicked)
        self.pb_270.clicked.connect(MainWindow.PbMoveToPos_Clicked)
        self.pb_315.clicked.connect(MainWindow.PbMoveToPos_Clicked)
        self.pb_360.clicked.connect(MainWindow.PbMoveToPos_Clicked)
        self.pb_ccw.clicked.connect(MainWindow.PbMove_Clicked)
        self.pb_cw.clicked.connect(MainWindow.PbMove_Clicked)
        self.pb_stop.clicked.connect(MainWindow.PbStop_Clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labeltitle.setText(_translate("MainWindow", "Controller Title"))
        self.labelaztext.setText(_translate("MainWindow", "Azimuth:"))
        self.labelaz.setText(_translate("MainWindow", "001 N"))
        self.pb_ccw.setText(_translate("MainWindow", "<< CCW"))
        self.pb_stop.setText(_translate("MainWindow", "STOP"))
        self.pb_cw.setText(_translate("MainWindow", "CW >>"))
        self.pb_000.setText(_translate("MainWindow", "000"))
        self.pb_045.setText(_translate("MainWindow", "045"))
        self.pb_090.setText(_translate("MainWindow", "090"))
        self.pb_135.setText(_translate("MainWindow", "135"))
        self.pb_179.setText(_translate("MainWindow", "179"))
        self.pb_360.setText(_translate("MainWindow", "360"))
        self.pb_315.setText(_translate("MainWindow", "315"))
        self.pb_270.setText(_translate("MainWindow", "270"))
        self.pb_225.setText(_translate("MainWindow", "225"))
        self.pb_181.setText(_translate("MainWindow", "181"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.menuConfig.setTitle(_translate("MainWindow", "File"))
        self.actionConfig.setText(_translate("MainWindow", "Config"))
        self.actionConfig.setToolTip(_translate("MainWindow", "Config and Settings"))
        self.actionConfig.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionLock.setText(_translate("MainWindow", "Lock Rotor"))
        self.actionLock.setToolTip(_translate("MainWindow", "Lockout for  rotor"))
        self.actionLock.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionUpdate.setText(_translate("MainWindow", "Poll"))
        self.actionUpdate.setToolTip(_translate("MainWindow", "Update Display Activate"))
        self.actionUpdate.setShortcut(_translate("MainWindow", "Ctrl+P"))
