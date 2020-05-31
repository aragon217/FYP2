import startAlarm
startAlarm.main()
while True:    
    import commands
    import time
    import re
    import logging
    import codecs
    import json

    import urllib2
    import alarmOff
    import alarmOn
    import macToPortBlock


    result = []
    duplicateResult = []
    logging.basicConfig(filename='rapDetection.log' , level=logging.DEBUG,

                            format='%(asctime)s:%(levelname)s:%(message)s')

    contain = 0
    duplicate = False

    #Start Wireless Interface as Monitor Mode

    #output4 = commands.getoutput('sudo airmon-ng start wlan0')
    

    #Remove previous Logs
    output2 = commands.getoutput('sudo rm -R TestLogs-0*')
    print output2
    #Executing airodump-ng for x duration
    print "Scan Starting"
    output = commands.getoutput('sudo timeout -sHUP 30 airodump-ng --essid FYP_EMIR -w TestLogs --output-format csv wlan0 < /dev/null')
    print("Scan Complete")
    logging.debug("Scan Complete")
    logging.debug("Initiating Filtering Process")
    print("Initiating Filtering Process")

    #Opening WhiteList File
    textfile2 = open("WhitelistLogs-01.csv","r")
    whitelist = textfile2.read()
    textfile2.close()

    pattern2 = re.compile(r'([A-z0-9]+:[A-z0-9]+:[A-z0-9]+:[A-z0-9]+:[A-z0-9]+:[A-z0-9]+),.*?,.*?,.*?,.*?,.*?,.*?,.*?,'

                         r'\s+(.*?),.*?,.*?,.*?,.*?,\s*FYP_EMIR,')
    matches2 = pattern2.findall(whitelist)



    #Opening TestLogs File
    textfile = open("TestLogs-01.csv","r")
    logFiles = textfile.read()
    textfile.close()

    pattern = re.compile(r'([A-z0-9]+:[A-z0-9]+:[A-z0-9]+:[A-z0-9]+:[A-z0-9]+:[A-z0-9]+),.*?,.*?,.*?,.*?,.*?,.*?,.*?,'

                         r'\s+(.*?),.*?,.*?,.*?,.*?,\s*FYP_EMIR,')
    matches = pattern.findall(logFiles)

    for i in matches:
        blackMac = str(i)[2:19]
        result.append(blackMac)

    duplicateList = list(set([ele for ele in result 
                if result.count(ele) > 1]))

    if len(duplicateList)>0:
        print("Duplicate MAC was Found : " + str(duplicateList))



    def list_diff(matches2, matches):

        out = []

        for ele in matches2:

            if not ele in matches:

                out.append(ele)

        return out

    #Printing the Difference

    result = list_diff(matches, matches2)

    #print result

    for i in xrange(len(result)):
        for results in result:
            targetMac, targetRssi = (results)
            intTargetRssi = int(targetRssi)

            for match2 in matches2:
                whiteMac, whiteRssi= (match2)
                intWhiteRssi = int(whiteRssi)

                if targetMac == whiteMac and (intWhiteRssi-40 <= intTargetRssi <= intWhiteRssi+40): 
                    result.remove(results)





    print result

    if len(result) > 0 or len(duplicateList)>0 :
        resultWithVendor = []
        logging.warning("RAP Detected!")
        print "RAP Detected!"
        alarmOn.main()
        print "Alarm Triggered"

        for i in result:
            macAddress, rssi = (i)
            macAddress1 = str(macAddress)
            url = "http://macvendors.co/api/"
            request = urllib2.Request(url+macAddress1, headers={'User-Agent' : "API Browser"})
            response = urllib2.urlopen(request)
            reader = codecs.getreader("utf-8")
            obj = json.load(reader(response))
            vendor =str(obj)
            if vendor != "{u'result': {u'error': u'no result'}}":
                resultWithVendor.append(macAddress +" "+ obj['result']['company'])

            else:
                resultWithVendor.append(macAddress+" "+"Vendor Unknown")
        


        for i in duplicateList:
            macAddress = (i)
            macAddress1 = str(macAddress)
            url = "http://macvendors.co/api/"
            request = urllib2.Request(url+macAddress1, headers={'User-Agent' : "API Browser"})
            response = urllib2.urlopen(request)
            reader = codecs.getreader("utf-8")
            obj = json.load(reader(response))
            vendor =str(obj)
            if vendor != "{u'result': {u'error': u'no result'}}":
                resultWithVendor.append(macAddress +" "+ obj['result']['company'])
       
            else:
                resultWithVendor.append(macAddress+" "+"Vendor Unknown")
        

        finalResult = result + duplicateList
        print resultWithVendor
        logging.warning(resultWithVendor)
        q = open("blackMac.txt","w")
        q.write(str(finalResult))
        q.close()
        macToPortBlock.main()


    else:
        logging.debug("No RAP Detected")
        print "No RAP Detected"
        alarmOff.main()
        print "Alarm Turned Off"
