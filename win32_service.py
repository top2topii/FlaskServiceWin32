import win32serviceutil
import win32service
import win32event
import win32evtlogutil
import servicemanager
import socket
import time
import logging
from multiprocessing import Process

import os
import sys
sys.path.append(os.path.dirname(__name__))

from myapp import app

logging.basicConfig(
    filename = 'c:\\Temp\\hello-service.log',
    level = logging.DEBUG, 
    format = '[helloflask] %(levelname)-7.7s %(message)s'
)

class HelloFlaskSvc (win32serviceutil.ServiceFramework):
    _svc_name_ = "HelloFlask"
    _svc_display_name_ = "Hello Flask Service"
    
    def __init__(self, *args):
        win32serviceutil.ServiceFramework.__init__(self, *args)
        self.hWaitStop = win32event.CreateEvent(None,0,0,None)
        socket.setdefaulttimeout(5)
        self.stop_requested = False

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.ReportServiceStatus(win32service.SERVICE_STOPPED)
        logging.info('Stopped service ...')
        self.stop_requested = True

    def SvcDoRun(self):
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STARTED,
            (self._svc_name_,'')
        )

        self.main()

    def main(self):
        app.run(host="127.0.0.1", port=8900)

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(HelloFlaskSvc)