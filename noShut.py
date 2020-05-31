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
tn.write("openmsa\n")
tn.write("conf t\n")

tn.write("int range f0/1-48\n")
tn.write("no shutdown\n")
tn.write("end\n")
tn.write("exit\n")

output2 = tn.read_all()
print output2
