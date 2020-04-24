import os
name_rest_dir = "pozostale"
path = "c:\\Users\\wojte\\Desktop\\test2"
os.chdir(path)

path_rest = os.path.join(path, name_rest_dir)

for i in os.listdir():
    if os.path.isdir(i):
        for j in os.walk(i):
            path_current_rest = os.path.join(path_rest, j[0])
            path_current = os.path.join(path, j[0])
            if not os.path.exists(path_current_rest):
                os.mkdir(path_current_rest)
            else:
                os.mkdir(os.path.join(path_rest, "new"))
                last_dir = os.path.basename(path_current_rest)
                last_dir = last_dir + "_(" + "1" + ")"
                
