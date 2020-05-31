def main():
    import getpass
    import sys
    import telnetlib

        
    HOST = "192.168.0.253"
    user = "openmsa"
    password = "openmsa"

    tn = telnetlib.Telnet(HOST)
    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:    
        tn.read_until("Password: ")
        tn.write(password + "\n")	

    tn.write("exit\n")
    tn.write("exit\n")
    output = tn.read_all()
    #print output
    print ("Telnet Connection Available")
