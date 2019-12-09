import os
import sys


def replaceContent(fileName, oldText, newText):
	fin = open(fileName, "rt")
	data = fin.read()
	data = data.replace(oldText, newText)
	fin.close()

	fin = open(fileName, "wt")
	fin.write(data)
	fin.close()


def getvCloudFolder(envVar):
	envVar = os.environ[envVar]
	vColudFolder = os.path.join(envVar, "vCloud")
	return vColudFolder


def getIPAddress(vColudFolder):
	ipFilePath = os.path.join(vColudFolder, "ipFile.txt")
	getEqual = False
	ipAddress = []

	with open(ipFilePath, 'r') as content:
		data = content.read()
		for each in data:
			if getEqual:
				ipAddress.append(each)
			if each == "=":
				getEqual = True

	getIPAddress = "".join(ipAddress)
	return getIPAddress


def replaceIPAddress(envVariable, newIPAddress):
	vColudFolder = getvCloudFolder(envVariable)
	oldIPAddress = getIPAddress(vColudFolder)

	for root, directories, files in os.walk(vColudFolder):
		for file in files:
			fileFullPath = os.path.join(vColudFolder, file)
			replaceContent(fileFullPath, oldIPAddress, newIPAddress)


if __name__ == '__main__':
	#if len(sys.argv) > 1:
	#	print(sys.argv[1])

    #var = str(sys.argv[1])
	print ("Hello")
	var = "No"

	if var == "IP":
		pass
        #envVariable = str(sys.argv[2]) # environment Variable
        #newIPAddress = str(sys.argv[3]) # New IP address
        #replaceIPAddress(envVariable, newIPAddress)
	pass