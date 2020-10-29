import logging
from .snap7 import *
import time
import sys

# for setup the Logo connection please follow this link
# http://snap7.sourceforge.net/logo.html


logging.basicConfig(level=logging.INFO)

# Siemens LOGO devices Logo 8 is the default
Logo_7 = True

logger = logging.getLogger(__name__)

plc = snap7.logo.Logo()
plc.connect("172.31.1.20",0x3000,0x2000)

if plc.get_connected():
    logger.info("connected")
    plc.write_area(0,1,1)
    #plc.write("VW62",1110) #change precuring time
    #plc.write("V0.1", 1) #stop oven
    #plc.write("V0.0", 0) #start oven
    time.sleep(1)
    #val = str(plc.read("V0.3"))
    val = str(plc.read("VW1150"))
    print("Value is {}".format(val))

else:
    logger.error("Conncetion failed")

plc.disconnect()
logger.info("Disconnected")
plc.destroy()
