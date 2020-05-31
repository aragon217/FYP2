#telnet into switch and copy show mac add table output in a file (macTable.txt)
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
	
	tn.write("enable\n")
        if password:
            tn.read_until("Password: ")
            tn.write(password + "\n")
	tn.write("show mac address-table dynamic\n")
	#tn.write("end\n")
	#tn.write("end\n")
	tn.write("exit\n")

	output = tn.read_all()
	#print output

	f = open("macTable.txt","w+")
	f.write(output)
	f.close()
	print ("MAC Address Table Obtained")


