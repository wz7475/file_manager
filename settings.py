import script
while True:
    print("1 - pokaż listę folderów")
    print("2 - pokaż listę rozszerzeń")
    print("3 - usuń folder")
    a = input()
    if a == "1":
        script.list_dirs()
    if a == "2":
        script.list_ext()
    if a == "3":
        script.delete_dir()
