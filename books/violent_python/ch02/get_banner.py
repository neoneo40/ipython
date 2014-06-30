
#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import optparse
import socket
from socket import *

# targetHost, targetPort
def connScan(tgtHost, tgtPort):
    try:
        # connect Socket
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('e ri python\r\n')
        results = connSkt.recv(100)
        print '[+] %d/tcp open' % tgtPort
        print '[+] ' + str(results)
        connSkt.close()
    except:
        print '[-] %d/tcp closed' % tgtPort
        
# portScan(특정 호스트, 포트들)
def portScan(tgtHost, tgtPorts):
    try:
        # 69.163.177.2 = gethostbyname('www.syngress')
        tgtIP = gethostbyname(tgtHost)
    except:
        print "[-] Cannot resolve '%s': Unknown host" % tgtHost
        return
    
    try:
        tgtName = gethostbyaddr(tgtIP)
        print '\n[+] Scan Results for: ' + tgtName[0]
    except:
        print '\n[+] Scan Results for: ' + tgtIP + ' except'
    
    setdefaulttimeout(1)
    
    for tgtPort in tgtPorts:
        print 'Scanning port ' + tgtPort
        # int method eliminates spaces
        connScan(tgtHost, int(tgtPort))
        
def main():
    parser = optparse.OptionParser('usage %prog ' +
                               '-H <target host> ' +
                               '-p <target port>')
    parser.add_option('-H', 
                      dest='tgtHost', 
                      type='string',
                      help='specify target host')
    parser.add_option('-p', 
                      dest='tgtPort', 
                      type='string',
                      help='specify target port[s] separated by comma')
    
    (options, args) = parser.parse_args()
    
    tgtHost = options.tgtHost
    tgtPorts = options.tgtPort.split(',')
    
    # eliminates spaces clearly
#     for idx, port in enumerate(tgtPorts):
#         tgtPorts[idx] = port.strip()
    
    print tgtPorts
    
    if (tgtHost == None) | (tgtPorts[0] == None):
        print '[-] You must specify a target host and port[s].'
        print parser.usage
#         exit(0)
    
    portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()