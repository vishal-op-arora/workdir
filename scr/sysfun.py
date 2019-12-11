import os

def getPath(env_var):
    return os.environ[env_var]


def getvCloudFolder(env_var):
    env_var = os.environ[env_var]
    v_cloud_folder = os.path.join(env_var, "vCloud")
    return v_cloud_folder


def fileContent(file_name, old_text, new_text):
    fin = open(file_name, "rt")
    data = fin.read()
    data = data.replace(old_text, new_text)
    fin.close()

    fin = open(file_name, "wt")
    fin.write(data)
    fin.close()
