import os
name_rest_dir = "pozostale"
list_dirs_all = ["word", "excel", "powerpoint", "pdf", "zdjecia", "skompresowane", name_rest_dir]
list_dirs_selected = ["word", "excel", "powerpoint", "pdf", "zdjecia", "skompresowane", name_rest_dir]
list_dirs_types = ["word", "excel", "powerpoint", "pdf", "zdjecia", "skompresowane"]

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


""" print("drag path")
path = input() 
"""
path = "c:\\Users\\wojte\\Desktop\\test"
os.chdir(path)

for i in os.listdir():
    if os.path.isfile(i):
        extension = os.path.splitext(i)[1]
        if extension not in ext_dict.keys():
            os.rename(i, os.path.join(path, name_rest_dir))
            continue
        dir_name = ext_dict[extension]
        if not os.path.exists(os.path.join(path, dir_name)):
            os.mkdir(dir_name)
        path_to_dir = os.path.join(path, dir_name)
        os.rename(i, os.path.join(path_to_dir, i))
    else:
        pass
#print("\nend of script\n")