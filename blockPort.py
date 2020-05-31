def main():
    import getMac
    import macFilter
    import initializePython
    import telnetlib
    import time
    import os
    import re

    #Check if File Exist and Has content
    file_path = 'Port2Block.txt'

    def is_file_empty(file_path):
        """ Check if file is empty by confirming if its size is 0 bytes"""
        # Check if file exist and it is empty
        return os.path.exists(file_path) and os.stat(file_path).st_size == 0

    is_empty = is_file_empty(file_path)

    if is_empty:
            print("No Port is Blocked")
    else:
            f = open("Port2Block.txt","r")
            port2Block = f.read()
            f.close()

            portRegex = re.compile (r'Fa[0-4]\/[0-9]+')
            PortRegexMatch = portRegex.findall(port2Block)
            
            print "Port To Block: " , PortRegexMatch
            HOST = "192.168.0.253"
            user = "openmsa"
            password = "openmsa"

            tn = telnetlib.Telnet(HOST)

            tn.read_until("Username: ")
            tn.write(user + "\n")
            if password:
                    tn.read_until("Password: ")
                    tn.write(password + "\n")	
                    
            tn.write("enable\n")
            if password:
                    tn.read_until("Password: ")
                    tn.write(password + "\n")

            tn.write("conf t\n")
            for x in PortRegexMatch:
                    print 'x'
                    tn.write("int " +x + "\n")
                    tn.write("shutdown\n")
                    tn.write("exit\n")
                    
            tn.write("end\n")
            tn.write("exit\n")
            outputFinal = tn.read_all()
            #print outputFinal
            #print (port2Block)
            print(port2Block,'Is blocked')
