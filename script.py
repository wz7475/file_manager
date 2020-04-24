import os
list_dirs_all = ["word", "excel", "powerpoint", "pdf", "zdjecia", "skompresowane", "pozostale"]
list_dirs_selected = ["word", "excel", "powerpoint", "pdf", "zdjecia", "skompresowane", "pozostale"]
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
path = "c:\\Users\\wojte\\Desktop"
os.chdir(path)

for i in os.listdir():
    if os.path.isfile(i):
        extension = os.path.splitext(i)[1]
        if extension not in list_dirs_types:
            os.rename(i, os.path.join(path, "pozostale"))
            continue
        dir_name = ext_dict[extension]
        if not os.path.exists(os.path.join(path, dir_name)):
            pass

#print("\nend of script\n")