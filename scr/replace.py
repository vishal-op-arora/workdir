import os
import sys


def replaceContent(file_name, old_text, new_text):
    fin = open(file_name, "rt")
    data = fin.read()
    data = data.replace(old_text, new_text)
    fin.close()

    fin = open(file_name, "wt")
    fin.write(data)
    fin.close()


def getvCloudFolder(env_var):
    env_var = os.environ[env_var]
    v_cloud_folder = os.path.join(env_var, "vCloud")
    return v_cloud_folder


def getIPAddress(v_cloud_folder):
    ip_file_path = os.path.join(v_cloud_folder, "ipFile.txt")
    get_equal = False
    ip_address = []

    with open(ip_file_path, 'r') as content:
        data = content.read()
        for each in data:
            if get_equal:
                ip_address.append(each)
            if each == "=":
                get_equal = True

    get_ip_address = "".join(ip_address)
    return get_ip_address


def replaceIPAddress(env_variable, new_ip_address):
    v_cloud_folder = getvCloudFolder(env_variable)
    old_ip_address = getIPAddress(v_cloud_folder)

    for root, directories, files in os.walk(v_cloud_folder):
        for file in files:
            file_full_path = os.path.join(v_cloud_folder, file)
            replaceContent(file_full_path, old_ip_address, new_ip_address)


if __name__ == '__main__':
    # if len(sys.argv) > 1:
    #	print(sys.argv[1])

    # var = str(sys.argv[1])
    print("Hello")
    var = "No"

    if var == "IP":
        pass
    # envVariable = str(sys.argv[2]) # environment Variable
    # newIPAddress = str(sys.argv[3]) # New IP address
    # replaceIPAddress(envVariable, newIPAddress)
    pass
