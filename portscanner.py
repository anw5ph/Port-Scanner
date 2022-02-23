# Importing socket library and datetime
import socket
from datetime import datetime

# User inputs target IP address
target = input("Enter a target to scan: ")
targetIp = socket.gethostbyname(target)

# User enters the port range they would like to scan
print("Please enter the range of ports you would like to scan on the target")

portStartInput = input("Enter a start port: ")
startPort = int(portStartInput)

portEndInput = input("Enter an end port: ")
endPort = int(portEndInput)

# Notifies user of the current time
print("Scanning started at: " + str(datetime.now()))

# Notifies user that scan has begun
print("Please wait, scanning started now: " + target)

# Scans ports from user requested start port and end port
for port in range(startPort, endPort):
    searcher = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    portStatus = searcher.connect_ex((targetIp, port))
    if (portStatus == 0):
        print("Port " + str(port) + ":              " + "Open")
    else:
        print("Port " + str(port) + ":              " + "Closed")

    searcher.close()

# Notifies user that port scan has completed
print("Port Scanning Completed")
