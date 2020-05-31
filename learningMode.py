import commands
import time
import re 

print ("Removing Existing Whitelist Files")
output0 = commands.getoutput('sudo rm WhitelistLogs-0*')
print output0
print ("Scanning...")
output = commands.getoutput('sudo timeout -sHUP 60 airodump-ng --essid FYP_EMIR -w WhitelistLogs --output-format csv wlan0 < /dev/null')
print ("Scan completed")
print ("The new whitelist are: ")

output2 = commands.getoutput('head -n 15 WhitelistLogs-01.csv')
print output2
