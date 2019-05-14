import logging
import snap7
import time
from snap7.snap7types import S7Object, buffer_type, buffer_size, BlocksList
from snap7.snap7types import TS7BlockInfo, param_types, cpu_statuses, S7WLByte, S7AreaDB
from ctypes import byref

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
    
    value_1a = 0b00000001
    value_2 = 480
    
    size = 8
    wordlen = S7WLByte
    type_ = snap7.snap7types.wordlen_to_ctypes[wordlen]
    data = (type_ * size)()
    area = S7AreaDB
    db_number = 1

    result = plc.library.Cli_ReadArea(plc.pointer, area, db_number, 32,size, wordlen, byref(data))
    print(result)
    print(bytearray(data)) 
    
else:
    logger.error("Conncetion failed")

plc.disconnect()
logger.info("Disconnected")
plc.destroy()
