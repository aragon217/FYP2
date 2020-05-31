def main():
#combine getMac, macFilter, and block corresponding port in the switch using telnet
    import getMac
    import macFilter
    import initializePython
    import blockPort
    import telnetlib
    import time
    import os

    print ("Checking For Telnet Connection...")
    initializePython.main()
    time.sleep(3)
    print ("Getting Mac Address Table from Switch...")
    getMac.main()
    time.sleep(3)
    print ("Checking if targetted Mac Address is in the Switch...")
    time.sleep(3)
    macFilter.main()
    time.sleep(3)
    blockPort.main()

