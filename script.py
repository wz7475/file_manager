import os
import shutil
from datetime import datetime
import json
name_rest_dir = "pozostale"
name_folder_dir = "foldery"
list_for_change = [".jpg", ".png"]
""" list_dirs_selected = ["word", "excel", "powerpoint", "pdf", "zdjecia", "skompresowane", name_rest_dir]
list_dirs_types = ["word", "excel", "powerpoint", "pdf", "zdjecia", "skompresowane"] """

ext_dict = json.load(open("ext.json"))

""" def write_json(data, filename='ext.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4) """


def name_changer(path):
    dir_name, file_full_name = os.path.split(path)
    name = os.path.basename(path)
    file_name, ext_name = os.path.splitext(name)
    mod_time = os.stat(path).st_mtime
    time = datetime.fromtimestamp(mod_time)
    str_time = str(time.strftime("%Y-%m-%d %Hh %Mmin %Ss"))
    new_name = str_time + ext_name
    return new_name
    # return os.path.join(dir_name, new_name)

def exists_checker(path):
    if (os.path.exists(path)):
        return True
    return False

def name_for_duplicates(path):
    if os.path.isfile(path):
        old_name = os.path.splitext(path)[0]
        new_name = old_name + "_" + os.path.splitext(path)[1]
    else:
        old_name = os.path.basename(path)
        new_name = old_name + "_"
    return new_name

def delete_dir():
    name = input("Podaj nazwę folderu - uwaga usuwasz całą jego zawartość:\n")
    if os.path.exists(os.path.join(os.getcwd(), name)):
        shutil.rmtree(os.path.join(os.getcwd(), name), ignore_errors=True)


def list_dirs():
    for i in ext_dict.values():
        print(i)


def list_ext():
    for i in ext_dict.keys():
        print(i)


def ext_checker(name):
    if name[0] != ".":
        return False
    for i in name[1:]:
        if ord(i) not in range(97, 123):
            return False
    return True


def name_checker(name):
    for i in name:
        if i in ["/", "\\", ":", "*", "?", "<", ">"]:
            return False
    return True


""" def add_ext():
    ext = input("Podaj nazwe rozszerzenia np. .txt\n")
    while not ext_checker(ext):
        ext = input("Podaj nazwe rozszerzenia, pamiętaj o poprawności np. .txt\n")
    if ext in ext_dict.keys():
        print("Rozszerzenie już wspierane")
        return
    folder = input("Podaj nazwe folderu:\n")
    while not name_checker(folder):
        folder = input("Podaj nazwe folderu, pamiętaj o poprawnośc")
    def write_json(data, filename='data.json'): 
        with open(filename,'w') as f: 
            json.dump(data, f, indent=4) 
        
        
        with open('ext.json') as json_file: 
            data = json.load(json_file) 

            # python object to be appended 
            y = {ext : folder}
        
            # appending data to emp_details  
            data.update(y) 
            
        write_json(data)   """



print("Przeciągnij folder lub wpisz ścieżkę:\n")
#path = input()

#path = "c:\\Users\\wojte\\Desktop\\test"
path = "/mnt/c/users/wojte/Desktop/test"
print(path)
os.chdir(path)

for i in os.listdir():
    if os.path.isfile(i):
        extension = os.path.splitext(i)[1]
        """ if extension not in ext_dict.keys():
            os.rename(i, os.path.join(path, name_rest_dir))
            continue """
        dir_name = ext_dict[extension]
        if not os.path.exists(os.path.join(path, dir_name)):
            os.mkdir(dir_name)
        path_to_dir = os.path.join(path, dir_name)
        if extension in list_for_change:
            new_name = name_changer(i)
            if exists_checker(os.path.join(path_to_dir, new_name)):
                new_name = name_for_duplicates(new_name)
            os.rename(i, os.path.join(path_to_dir, new_name))
        else:
            if exists_checker(os.path.join(path_to_dir, i)):
                new_name = name_for_duplicates(i)
                os.rename(i, os.path.join(path_to_dir, new_name))
            else:
                os.rename(i, os.path.join(path_to_dir, i))
    if os.path.isdir(i) and os.path.basename(i) != name_folder_dir and os.path.basename(i) not in ext_dict.values():
        """ if not os.path.exists(os.path.join(path, name_folder_dir)):
            os.mkdir(name_folder_dir)
            print("create foldery") """
        path_to_folder_dir = os.path.join(path, name_folder_dir)
        if exists_checker(os.path.join(path_to_folder_dir, i)):
            new_name = name_for_duplicates(i)
            shutil.copytree(i, os.path.join(path_to_folder_dir, new_name))
        else:
            shutil.copytree(i, os.path.join(path_to_folder_dir, os.path.basename(i)))
        shutil.rmtree(i, ignore_errors=True)
        #shutil.rmtree(i, ignore_errors=True)

        #https://www.geeksforgeeks.org/copy-a-directory-recursively-using-python-with-examples/
