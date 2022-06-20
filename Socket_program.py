# 1. Objective: a program to request and download web objects from any web server like www.yahoo.com or www.google.com
# 2. User enters a url as command line arg
# 3. Program will then issue an HTTP GET request for the object.  

'''
Resource used:
1. https://www.networkcomputing.com/data-centers/python-network-programming-handling-socket-errors
2. TextBook
3. Lecture material
4. https://www.programiz.com/python-programming/exception-handling
5. https://pythontic.com/modules/socket/gethostbyname
6. https://www.geeksforgeeks.org/socket-programming-python/
7. https://www.pubnub.com/blog/socket-programming-in-python-client-server-p2p/
8. https://pythonprogramming.net/sockets-tutorial-python-3/

'''

import argparse
from socket import *
import socket
import sys

#def pir(a,b):
#    print ("the sum is:", a+b)

#if __name__=="__main__":
#    a=int(sys.argv[1])
#    b=int(sys.argv[2])
#    pir(a,b)
#print ('Number of args:', len(sys.argv), 'argument.')
#print ('arg list:', str(sys.argv))

#----------------------------------
# For our main() function:
'''
1. We open HTTPoutput.html file
2. Get the total number of user argument 
3. Get the arguments
4. if first arg then split that from '/'
5. 
3. If it is 3 -> Ip at index 1 and domain at 2.

'''
def getLog(hostName, port):
    pass
    #true=''
    #)
    #f.write(info + "\n\n")
    #f.close()
def getServer(hostname, hostDom1, getPort, epstr):
    output = open("HTTPoutput.html", "w")
    print(hostname)
    print(hostDom1)
    print(getPort)
    #get the domain host name
    try:
        serverIP=socket.gethostbyname(hostDom1)
    except socket.error:
        raise Exception('Could not resolve host.')
        
    print(serverIP)
    #print(hostDom1)
    #create a TCP connection
    connect_soc=socket.create_connection((serverIP, int(getPort)))
    
    #f = open("Log.csv", "a")
    #src_ip, src_port = connect_soc.getsockname()
    #dst_ip = socket.gethostbyname()

    
    #we GET request in appropriate format
    if epstr is not None:
        request="GET / "+epstr +"HTTP/1.1\r\n\Host: "+hostDom1+"\r\n\r\n"
    else:
        request="GET / HTTP/1.1\r\n\Host: "+hostDom1+"\r\n\r\n"
    #we  send the request that we encoded. 
    connect_soc.send(request.encode())
    str1=""
    getHead=""
   
    srcip,srcport=connect_soc.getsockname()
    while True:
        try:
            data=connect_soc.recv(1024)
            str1=data.decode()
            if len(data) <1024:
                break
        except ConnectionResetError:
            connect_soc.close()
            sys.exit("connection reset error")
    
    ret=str1.find("\r\n\r\n")
    output.write(str1[ret:])
    getHead=str1[:ret]
    print(getHead)
    
    stat= getHead.split("\r\n")[0].split(' ')[1]
    #right=str1.split("r")[0]
    
    if(len(str1)>=1):
        result=stat[1]
        mess=stat[2]
    else:
        result='56'
        mess='Empty Response!'
    
    if(result=='200' and epstr != '443'):
        final="Successful"
        print("Successful, "+str(stat)+", "+str(hostname)+", "+str(hostDom1)+", "+str(srcip)+", "+str(serverIP)+", "+str(srcport))
    else:
        print("Unsuccessful, "+str(stat)+", "+str(hostname)+", "+str(hostDom1)+", "+str(srcip)+", "+str(serverIP)+", "+str(srcport))
        print("Bad Request: ", getHead.split('\r\n')[0])
        
    #try:
    #    connect_soc.connect((hostDom1, getPort))
    #except socket.gaierror as e:

        #print "Address-related error connecting to server: %s" % e
    file1=open("Log.csv", "a")
    file1.write("Unsuccessful, Not Valid")
    file1.close()
    #sys.exit(1)
    
    connect_soc.close()
    '''except socket.gaierror:
        file=open("Log.csv", "a")
        file.write("Unsuccessful, Domain not valid")
        file.close()'''
    
        
# ----------GLOBAL VAR-----------
#keep track of the arg count
arg_count=len(sys.argv)
#get all the args 
arg=sys.argv
#--------------------------------
# Check for valid user args
def checkArg():
    #if arg is 1 then show the usage format
    if (arg_count == 1):
        print("Usage: pmahaleMyCurl.py [fullURL] or [hostname]")
        sys.exit(1)
    if (arg_count == 1):
        print("Usage: pmahaleMyCurl.py [fullURL] or [hostname]")
        sys.exit(1)
    
#--------------------------------
#def util(hostname, hostDom1, getPort, epstr):
    #checkPort=header

# -------------------------------
#Make sure 'https' is not supported
if 'https:' in arg[1].split('/'):
    temp= open ('Log.csv', 'a')
    temp.write('Unsuccessful, HTTPS used')
    temp.close()
    print("HTTPS not supported")
    sys.exit()
#--------------------------------
#check for expections:
def checker2(name):
    f_dom=name.find('//')
    proto=name[:f_dom]
    if proto != 'http:':
        exit()
'''
python Socket.py htttp://word.com/path.html

1. Here Socket.py is the file name which is arg[0]
2. Here http://word.com/ host name which is arg[1] and we want to split it from '//'
'''
    
#--------------------------------
def checker():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='to test program')    
    hostname= arg[1]
    hostInd=hostname.split('//')[1]
    hostDom=hostInd
    #ep length
    epstr=''
    setPort='80'
    #print(hostInd)
    #create socket
    #cSoc = socket(AF_INET, SOCK_STREAM)
    print(arg)
    # There is only domain/host to handle like below
    '''
    python3 TestFile.py http://www.google.com:80
    or 
    python TestFile.py http://93.184.216.34:80/foo.html
    '''
    #--------------------------------
    if arg_count==2:
        #we need to split on the ':' part
        
        if ':' in hostInd:
            split_port=hostInd.split(':')[1]
            #print(split_port)
            #80/foo.html
            #we need to grab only the port number in above example
            if (split_port == '443'):
                sys.exit("Bad Port #")
            if '/' in split_port:
                split_port=split_port.split('/')[0]
                setPort=split_port
                print(setPort)
            elif split_port=='':
                setPort=None
            #we need to set the default port number to 80 if there is no port
            else:
                setPort=split_port
        h=arg[0][7:]
        if h.find(':') !=-1:
            t5=h[h.find(':'):]
            host5=h[:h.find(':')]
            
        #check for the endpoint which is the foo.html in above example
        if '/' in hostInd:
            ep=hostInd.split('/')[1]
            if ep=='':
                epstr=None
            else:
                epstr= ep
            print(ep)
        if ':' in hostInd:
            hostDom=hostInd.split(':')[0]
        elif '/' in hostInd:
            hostDom=hostInd.split('/',1)[0]
        else:
            hostDom=hostInd
        #cSoc.connect((hostDom, int(setPort)))
        getServer(hostname,hostDom,setPort, epstr)
        getLog(hostname, setPort)
        #-------------------------------- 
    #--------------------------------        
    elif arg_count==3:
        #ipAdd=hostInd
        hostDom=arg[2]
        if ':' in hostInd:
            split_port=hostInd.split(':')[1]
            website=hostInd.split(':')[0]
            print(website)
            #80/foo.html
            #we need to grab only the port number in above example
            if (split_port == '443'):
                sys.exit("Bad Port #")
            if '/' in split_port:
                split_port=split_port.split('/')[0]
                setPort=split_port
                #print(getPort)
            elif split_port=='':
                setPort=None
            else:
                setPort=split_port
        #else:
            #getPort='80'
        #check for the endpoint which is the foo.html in above example
        if '/' in hostInd:
            ep=hostInd.split('/')[1]
            print(ep)
            if ep=='':
                epstr=None
            else:
                epstr= ep
        #--------------------------------    
        #cSoc.connect((hostDom, int(setPort)))
        getServer(hostname,hostDom,setPort,epstr)
        getLog(hostname, setPort)

        #-------------------------------- 
    #else:
        #exit()
    
#--------------------------------
if __name__=="__main__":
    checker()
