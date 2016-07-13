
import logging
from datetime import datetime,tzinfo,timedelta
from flask import Flask

app = Flask(__name__)

class Zone(tzinfo):
    def __init__(self,offset,isdst,name):
        self.offset = offset
        self.isdst = isdst
        self.name = name
    def utcoffset(self, dt):
        return timedelta(hours=self.offset) + self.dst(dt)
    def dst(self, dt):
            return timedelta(hours=1) if self.isdst else timedelta(0)
    def tzname(self,dt):
         return self.name

@app.route('/')
def hello_world():
	logging.info('[GET] hello_world ...')
	KST = Zone(+9,False,'KST')
	now_time = datetime.now(KST).strftime('%Y-%m-%d %H:%M:%S %Z')
	return 'Hello, World! ' + now_time