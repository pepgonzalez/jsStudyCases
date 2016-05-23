import os

def rename_files():
    #r antes del path es para rawPath, con esto se le dice a python que interprete el path tal cual esta
    list = os.listdir(r"C:\Users\joseg\Desktop\Udacity\broma")
    print list

    #currentWorking directory
    currentPosition = os.getcwd()

    os.chdir(r"C:\Users\joseg\Desktop\Udacity\broma")
    #(2) for each file, reame
    for name in list:
        os.rename(name, name.translate(None, "0123456789"))

    os.chdir(currentPosition)
    print("fin del proceso")
rename_files()
