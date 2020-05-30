import os
path = "/mnt/c/users/wojte/Desktop/test"
print(path)


def exists_checker(path):
    if (os.path.exists(path)):
        return True
    return False 


os.chdir(path)

if(exists_checker(os.path.join(path, "pozostale"))):
    # os.mkdir("pozostale")
    print(1)
os.mkdir("pozostale")
#print(os.path.isdir(os.path.join(path, "pozostale")))
