import os
import sys
import ip_add as ip

if __name__ == '__main__':
    # var = str(sys.argv[1])
    var = "No"
    if var == "IP":
        envVariable = str(sys.argv[2])  # environment Variable
        newIPAddress = str(sys.argv[3])  # New IP address
        ip.replaceIPAddress(envVariable, newIPAddress)

    if var == 'FCCPath':
        pass

