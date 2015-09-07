from datetime import datetime
import time

__author__ = 'bida'

stamp = time.mktime(datetime.now().timetuple())
print str(int(stamp))+'000'
