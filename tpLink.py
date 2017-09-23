import urllib2, base64, json

with open('config.json') as data_file:    
    data = json.load(data_file)

auth = 'Basic ' + base64.b64encode(data["Login"]["User"]+':'+data["Login"]["Password"])

def makeRequest(url,heads):
    request = urllib2.Request(url, None, heads)
    return (urllib2.urlopen(request)).read()

def addTarget(Description,domain1,domain2,domain3,domain4):
    url = 'http://' + data["IpRouter"] + '/userRpm/AccessCtrlAccessTargetsRpm.htm?target_type=0&targets_lists_name='+Description+ '&dst_ip_start=&dst_ip_end=&dst_port_start=&dst_port_end=&proto=0&Commonport=0&url_0='+domain1+'&url_1='+domain2+'&url_2='+domain3+'&url_3='+domain4+'&Changed=0&SelIndex=0&fromAdd=0&Page=1&Save=Save'
    
    heads = { 'Referer' : 'http://' + data["IpRouter"] + '/userRpm/AccessCtrlAccessTargetsRpm.htm',
             'Authorization' : auth
    }

    return makeRequest(url,heads)

def addHostLan(Description,ipStart,ipEnd):
    Description = Description.replace(" ", "+")
    url = 'http://' + data["IpRouter"] + '/userRpm/AccessCtrlHostsListsRpm.htm?addr_type=1&hosts_lists_name='+Description+'&src_ip_start='+ipStart+'&src_ip_end='+ipEnd+'&mac_addr=&Changed=0&SelIndex=0&fromAdd=0&Page=1&Save=Save'
    
    heads = { 'Referer' : 'http://' + data["IpRouter"] + '/userRpm/AccessCtrlHostsListsRpm.htm',
             'Authorization' : auth
    }

    return makeRequest(url,heads)

def getTotalTarget(number):
    url = 'http://' + data["IpRouter"] + '/userRpm/AccessCtrlAccessTargetsRpm.htm?Page='+`number`
    
    heads = { 'Referer' : 'http://' + data["IpRouter"] + '/userRpm/AccessCtrlAccessTargetsRpm.htm',
             'Authorization' : auth
    }

    return makeRequest(url,heads)


def countTarget(number):
    page = getTotalTarget(number)
    devices = []

    #Parse out target list
    page = page.split("new Array(", 1)
    page = page[1].split('0,0 );', 1)
    page = page[0].replace('"',"").replace(' ',"")
    data = page.split("\n")

    for index in range(len(data)):
        if(index != 0):
            devices.append( data[index].split(",") )

    return (len(devices))-1

def addRule(ruleName,numberTarget):
    url = 'http://' + data["IpRouter"] + '/userRpm/AccessCtrlAccessRulesRpm.htm?rule_name='+ruleName+'&hosts_lists=0&targets_lists='+`numberTarget`+'&scheds_lists=255&enable=1&Changed=0&SelIndex=0&Page=1&Save=Save'
    
    heads = { 'Referer' : 'http://' + data["IpRouter"] + '/userRpm/AccessCtrlAccessRulesRpm.htm',
             'Authorization' : auth
    }

    return makeRequest(url,heads)

def enableAccessControl():
    print "Enable Acces Control"
    url = 'http://' + data["IpRouter"] + '/userRpm/AccessCtrlAccessRulesRpm.htm?enableCtrl=1&defRule=0&Page=1'
    heads = { 'Referer' : 'http://' + data["IpRouter"] + '/userRpm/AccessCtrlAccessRulesRpm.htm',
             'Authorization' : auth
    }

    return makeRequest(url,heads)

if __name__ == "__main__":
    enableAccessControl()