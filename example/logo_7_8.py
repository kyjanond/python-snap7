import logging
import snap7
import time

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
    
    # read I1 from logo
    #vm_address = ("V923.0" if Logo_7==True else "V1024.0")
    
    vm_address = "V1064"
    print ("I1: " + str(plc.read(vm_address)))

    # write some values in VM addresses between 0 and 100
    
    value_1a = 0b00000001
    value_2 = 480
    
    plc.write("V0.2",0)
    plc.write("V0.3",0)
    time.sleep(3)
    plc.write("V0.3", 1)
    time.sleep(1)
    plc.write("VW40", 600)
    time.sleep(1)
    val = plc.read("VW40")
    print(val)
    

    print("read V10.0 must be 1 - check: " + str(plc.read("V10.0")))
    print("read V10.3 must be 0 - check: " + str(plc.read("V10.3")))
    print("read V10.7 must be 1 - check: " + str(plc.read("V10.7")))
    
    print("write 480 analog value to VW20")
    #plc.write("VW20", value_2)
    
    print("read VW20 must be 480 - check:" + str(plc.read("VW20")))
        
    print("trigger V10.2")
    #plc.write("V10.2", 0)
    #plc.write("V10.2", 1)
    #plc.write("V10.2", 0)

else:
    logger.error("Conncetion failed")

plc.disconnect()
logger.info("Disconnected")
plc.destroy()
