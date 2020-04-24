import os
from datetime import datetime
name_rest_dir = "pozostale"
list_for_change = [".jpg", ".png"]
""" list_dirs_selected = ["word", "excel", "powerpoint", "pdf", "zdjecia", "skompresowane", name_rest_dir]
list_dirs_types = ["word", "excel", "powerpoint", "pdf", "zdjecia", "skompresowane"] """

ext_dict = {
".docx" : "word",
".xlsx" : "excel",
".pptx" : "power_point",
".pdf" : "pdf",
".png" : "zdjecia",
".jpg" : "zdjecia",
".gif" : "zdjecia",
".zip" : "skompresowane",
".rar" : "skompresowane"
}

def name_changer(path):
    dir_name, file_full_name = os.path.split(path)
    name = os.path.basename(path)
    file_name, ext_name = os.path.splitext(name)
    mod_time = os.stat(path).st_mtime
    time = datetime.fromtimestamp(mod_time)
    str_time = str(time.strftime("%Y-%m-%d %Hh %Mmin %Ss"))
    new_name = str_time + ext_name
    return new_name
    #return os.path.join(dir_name, new_name)

""" print("drag path")
path = input() 
"""
path = "c:\\Users\\wojte\\Desktop\\test"
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
                file_name_whole = os.path.basename(os.path.join(path, name_changer(i)))
            else:
                file_name_whole = os.path.basename(os.path.join(path, i))
            
            file_name_base, file_name_ext = os.path.splitext(file_name_whole)
            file_name_base += "#"
            file_name_new = file_name_base + file_name_ext
            
            dir_name = ext_dict[extension]
            path_rest = os.path.join(path, dir_name)
            if not os.path.exists(os.path.join(path, dir_name)):
                os.mkdir(dir_name)
            path_to_dir = os.path.join(path, dir_name)
            os.rename(os.path.join(path, i), os.path.join(path_rest, file_name_new))
