    #get mac from switch, parse, and check if same as targetted
def main():    
    import re


    targetMac = []

    f = open("macTable.txt","r")
    toFilter = f.read()
    f.close()

    regexPattern = re.compile (r'\s+\d\s+([0-9A-z]+.[0-9A-z]+.[0-9A-z]+)\s+DYNAMIC\s+(.+)')

    matches = regexPattern.findall(toFilter)

    w = open("blackMac.txt","r")
    text = w.read()
    w.close()

    blockPort=[]

    regex = re.compile (r'[A-z0-9]+.[A-z0-9]+.[A-z0-9]+.[A-z0-9]+.[A-z0-9]+.[A-z0-9]+')
    MacRegexMatch = regex.findall(text)

    for i in MacRegexMatch:
            blackMac = str(i)[0:19]
            blackMac = re.sub(":","",i)
            blackMac = blackMac[:4]+"."+blackMac[4:8]+"."+blackMac[8:12]
            blackMac = blackMac.lower()
            targetMac.append(blackMac)

    print targetMac	

    #print matches

    for r in targetMac:
            xMac = (r)
            for z in matches:
                    macAddress, Port = (z)
                    if xMac == macAddress and Port != "Fa0/1\r":
                            blockPort.append(Port)


    print blockPort

    if len(blockPort) > 0:
            print "Mac Address Found!"
            g = open("Port2Block.txt","w+")
            g.write(str(blockPort))
            g.close()
    else:	
            print ("Mac Address does not exist in Switch")
            g = open("Port2Block.txt","w+")
            g.close()
