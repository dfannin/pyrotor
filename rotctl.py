import subprocess
import logging
import os

logger = logging.getLogger('main')

class RotCtl:
    def __init__(self,RC):
        self.RC = RC.copy()
        self.rcprocess= None
        logger.debug("init rotctl object")

    def start(self):
        logger.debug("trying to start rotctld") 

        # strip out everything before the : char
        prt = self.RC['port'].split(':',1)[-1] 

        cmd = [self.RC['path'] , \
              '-m' , self.RC['modelid'] ,\
              '-r' , self.RC['devserial'] , 
              '-s' , '9600',\
              '-t' , prt, \
              '&>/dev/null', \
              '&' ]
        try:
            self.rcprocess = subprocess.Popen(cmd,shell=False,close_fds=True)
        except ValueError as e:
            logger.info("rotctl start value error") 
        except subprocess.TimeoutExpired as e:
            logger.info("rotctl start timeout error") 
        except subprocess.CalledProcessError as e:
            logger.info("rotctl start called process error") 

        logger.debug("rotctl start pid %d,  %s" % ( self.rcprocess.pid, ' '.join(cmd) ) ) 


    def stop(self):
        logger.debug("ok trying to stop rotctld") 
        if self.rcprocess:
            logger.debug("rotctl kill pid %d" % ( self.rcprocess.pid) ) 
            self.rcprocess.kill()

    def show(self):
        logger.debug('show rotctld process')
        if self.rcprocess:
            try:
                os.kill(self.rcprocess.pid,0)
                return 0 
            except OSError:
                return 2

        return 1


# 
# global functions
#

def RCGetPosition(RC):
        logger.debug("rotctl get position") 

        cmd = [ '/usr/bin/rotctl' , '-m' , '2' , '-r' , RC['port'], 'p' ]

        logger.debug(cmd)

        try:
            cpval = subprocess.run(cmd,timeout=2,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            
            if cpval.stdout and cpval.returncode == 0:
                #
                # [0] is az, [1] is el
                retvals  = cpval.stdout.splitlines()
                if retvals[0]:
                    return int( float(retvals[0]) ) 

            logger.debug(cpval.stdout)
            logger.info("rotctl no value returned") 
            return -1

        except ValueError as e:
            logger.info("rotctl value error") 
            return -2
        except subprocess.TimeoutExpired as e:
            logger.info("rotctl timeout error") 
            return -3
        except subprocess.CalledProcessError as e:
            logger.info("rotctl called process error") 
            return -4

def RCStop(RC):
        logger.debug("rotctl stop") 

        cmd = [ '/usr/bin/rotctl' , '-m' , '2' , '-r' , RC['port'], 'S' ]

        logger.debug(cmd)

        try:
            cpval = subprocess.run(cmd,timeout=3,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            
            if cpval.returncode == 0:
                logger.debug("rotctl stop rotation") 
                return 0 
            else:
                logger.debug("rotctl stop cmd error") 
                return -1

        except subprocess.TimeoutExpired as e:
            logger.info("rotctl stop timeout error") 
            return -2
        except subprocess.CalledProcessError as e:
            logger.info("rotctl called process error") 
            return -3

def RCmove(RC,direction=None):
        logger.debug("rotctl move") 

        dir = "0"
        speed = "100"

        if direction == "CW":
            dir = "16"
        elif direction == "CCW":
            dir = "8"
        else:
            logger.error("rotctl move error direction input")
            return -1

        cmd = [ '/usr/bin/rotctl' , '-m' , '2' , '-r' , RC['port'], 'M', dir, speed ]

        logger.debug(cmd)

        try:
            cpval = subprocess.run(cmd,timeout=2,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            
            if cpval.returncode == 0:
                logger.debug("rotctl moving ") 
                return 0 
            else:
                return -2

        except subprocess.TimeoutExpired as e:
            logger.info("rotctl stop timeout error") 
            return -3
        except subprocess.CalledProcessError as e:
            logger.info("rotctl called process error") 
            return -4

def RCmoveToPosition(RC,position=None):
        logger.debug("rotctl move to position") 

        if int(position) < 0 or int(position) > 360:
            logger.error("rotctl move to position input error")
            return -1 

        cmd = [ '/usr/bin/rotctl' , '-m' , '2' , '-r' , RC['port'], 'P', position , '0' ]

        logger.debug(cmd)

        try:
            cpval = subprocess.run(cmd,timeout=2,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            
            if cpval.returncode == 0:
                logger.debug("rotctl moving to position %s" % (position)) 
                return 0 
            else:
                return -2

        except subprocess.TimeoutExpired as e:
            logger.info("rotctl stop timeout error") 
            return -3
        except subprocess.CalledProcessError as e:
            logger.info("rotctl called process error") 
            return -4
