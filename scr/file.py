import os
import sysfun as sf




def replacefcc(env_variable, new_ip_address):
    root_folder = sf.getPath('ROOT')
    v_cloud_folder = sf.getvCloudFolder(env_variable)


    old_ip_address = getIPAddress(v_cloud_folder)

    for root, directories, files in os.walk(v_cloud_folder):
        for file in files:
            file_full_path = os.path.join(v_cloud_folder, file)
            sf.fileContent(root_folder, root_folder, v_cloud_folder)
            #replaceContent(file_full_path, old_ip_address, new_ip_address)



