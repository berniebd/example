# -*- encoding:utf-8 -*-
# import logging
#
# __auth__ = 'bida'
#
# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# logging.basicConfig(level=logging.DEBUG, filename='my.log', format=LOG_FORMAT)
#
# logging.debug("This is a debug log.")
# logging.info("This is a info log.")
# logging.warning("This is a warning log.")
# logging.error("This is a error log.")
# logging.critical("This is a critical log.")

import logging

#Formatter
format = logging.Formatter('%(asctime)s:%(clientip)s:%(user)s:%(levelname)s:%(message)s')

EXTRA = {'clientip':'192.168.1.1','user':'bernie'}
DATEFORMAT = '%Y/%m/%d %I:%M:%S %p'

logging.basicConfig(filename='test.log',
                   format=format,
                   level=logging.WARN,
                   datefmt=DATEFORMAT )

logging.debug('a debug message')
logging.warning('a warn message')
logging.error('an error message')

#logger
log = logging.getLogger('root.test')
log.setLevel(logging.WARNING)
log.debug('Protocol problem :%s','connection reset',extra=EXTRA)

#handler
log2 = logging.getLogger('root.hanlder')

#use default config
hdlr = logging.StreamHandler()
#use handler own config
hdlr2 = logging.FileHandler('FileHandler.log','a')

hdlr.setLevel(logging.WARN)

log2.addHandler(hdlr)
log2.addHandler(hdlr2)


log2.warning('Protocol problem :%s','connection reset',extra=EXTRA)