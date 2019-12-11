import os
import sysfun as sf


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
    v_cloud_folder = sf.getvCloudFolder(env_variable)
    old_ip_address = getIPAddress(v_cloud_folder)

    for root, directories, files in os.walk(v_cloud_folder):
        for file in files:
            file_full_path = os.path.join(v_cloud_folder, file)
            sf.fileContent(file_full_path, old_ip_address, new_ip_address)
            #replaceContent(file_full_path, old_ip_address, new_ip_address)



