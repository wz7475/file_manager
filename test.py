import json
name_rest_dir = "pozostale"
path = "c:\\Users\\wojte\\Desktop\\test2"
# os.chdir(path)


def open_settings():
    with open("test.json") as f:
        data = f.read()
    return json.loads(data)

def ext_checker(name):
    if name[0] != ".":
        return False
    for i in name[1:]:
        if ord(i) not in range(97, 123):
            return False
    return True

def save_settings(settings):
    data = json.dumps(settings, indent=2)
    with open("test.json", "w") as f:
        f.write(data)

def add_ext():
    ext = input("podaj poprawną nazwę rozszerzenia np .pdf:\n")
    while(not ext_checker(ext)):
        ext = input("podaj poprawną nazwę rozszerzenia np .pdf:\n")

    

''' settings = open_settings()
del settings["ext"][".pdf"]
settings["ext"][".cpp"] = "c++"
save_settings(settings) '''

''' mydict = {'george': 16, 'amber': 19}
print(list(mydict.keys())[list(mydict.values()).index(19)]) '''

add_ext()