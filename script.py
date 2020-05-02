import os
import shutil
from datetime import datetime
import json
name_rest_dir = "pozostale"
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
path = input()

#path = "c:\\Users\\wojte\\Desktop\\test"
os.chdir(path)

for i in os.listdir():
    if os.path.isfile(i):
        try:
            extension = os.path.splitext(i)[1]
            """ if extension not in ext_dict.keys():
                os.rename(i, os.path.join(path, name_rest_dir))
                continue """
            dir_name = ext_dict[extension]
            if not os.path.exists(os.path.join(path, dir_name)):
                os.mkdir(dir_name)
            path_to_dir = os.path.join(path, dir_name)
            if extension in list_for_change:
                os.rename(i, os.path.join(path_to_dir, name_changer(i)))
            else:
                os.rename(i, os.path.join(path_to_dir, i))
        except FileExistsError:
            if extension in list_for_change:
                file_name_whole = os.path.basename(
                    os.path.join(path, name_changer(i)))
            else:
                file_name_whole = os.path.basename(os.path.join(path, i))

            file_name_base, file_name_ext = os.path.splitext(
                file_name_whole)
            file_name_base += "#"
            file_name_new = file_name_base + file_name_ext

            dir_name = ext_dict[extension]
            path_rest = os.path.join(path, dir_name)
            if not os.path.exists(os.path.join(path, dir_name)):
                os.mkdir(dir_name)
            path_to_dir = os.path.join(path, dir_name)
            os.rename(os.path.join(path, i), os.path.join(
                path_rest, file_name_new))
    if os.path.isdir(i):
        pass
        #https://www.geeksforgeeks.org/copy-a-directory-recursively-using-python-with-examples/
