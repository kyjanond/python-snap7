import logging
import snap7
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
    
    #plc.write("V0",0)
    plc.write("VW40",910)
    time.sleep(1)
    print(plc.read("VW40"))
    #plc.write("V0.3", 1)
    #plc.write("V0.1", 1)
    #plc.write("V0.0", 0)
    time.sleep(1)
    #plc.write("V0",0)
    val = str(plc.read("V1104.3"))
    print(val)

else:
    logger.error("Conncetion failed")

plc.disconnect()
logger.info("Disconnected")
plc.destroy()
