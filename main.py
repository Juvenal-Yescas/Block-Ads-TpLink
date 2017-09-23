import tpLink

# Start Functions parser domains of hosts.txt
lines = tuple(open("hosts.txt", 'r')) # Add to array domains
count = 0
array = []
numberEspecial=0
numberTitle=1

def willBeValid(lineDomain): # check if domain firs character is 0 > 0.0.0.0 mydomai.com
    if (lineDomain[0][0] == "0"):
        return True
    else:
        return False

def parserDomain(lineDomain):
    return lineDomain.replace("0.0.0.0 ", "")

def checkDomain(lineDomain):
    if (willBeValid(lineDomain)):
        array.append((parserDomain(lineDomain)).split()[0])

def specialAdd():
    global count,numberTitle,numberEspecial
    remaining=len(array)-numberEspecial
    if remaining == 1:
        tpLink.addTarget("Adspecial"+`numberTitle`,array[count],"","","")
    elif remaining == 2:
        tpLink.addTarget("Adspecial"+`numberTitle`,array[count],array[count+1],"","")
    elif remaining == 3:
        tpLink.addTarget("Adspecial"+`numberTitle`,array[count],array[count+1],array[count+2],"")
    else :
        tpLink.addTarget("Adspecial"+`numberTitle`,array[count],array[count+1],array[count+2],array[count+3])

def setupTargets():
    print "Add targets"
    global count,numberTitle,numberEspecial
    for lineDomain in lines:
        checkDomain(lineDomain)

    while (count <= len(array)):
        if ((count+4) > len(array)):
            numberEspecial=count
            numberTitle = numberTitle+1
            specialAdd()
            count = count + 4
        else:
            tpLink.addTarget("Ads"+`numberTitle`,array[count],array[count+1],array[count+2],array[count+3])
            count = count + 4
            numberTitle = numberTitle+1

# End Functions parser domains of hosts.txt

# Start count the rules and add
def setupRules():
    print "Setup rules"
    countRule=1
    numbeRules=(tpLink.countTarget(1)+tpLink.countTarget(2))
    while(countRule<=numbeRules):
        tpLink.addRule("Ads"+`countRule`,countRule-1)
        countRule=countRule+1
# End count the rules and add

if __name__ == "__main__":
    print 'Start'
    setupTargets()
    tpLink.addHostLan("Block Ads Lan","192.168.0.100","192.168.0.199")
    setupRules()
    tpLink.enableAccessControl()
    print "Good bye!"