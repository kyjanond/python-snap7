import logging
import snap7
import time
from snap7.snap7types import S7Object, buffer_type, buffer_size, BlocksList
from snap7.snap7types import TS7BlockInfo, param_types, cpu_statuses, S7WLByte, S7AreaDB
from ctypes import byref
import struct


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
    
    # write some values in VM addresses between 0 and 100
    
    val = plc.read_area(40,8)
    print(struct.unpack_from('>4h',val)) 
    
else:
    logger.error("Conncetion failed")

plc.disconnect()
logger.info("Disconnected")
plc.destroy()
