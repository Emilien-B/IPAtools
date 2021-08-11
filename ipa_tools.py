import os
# python3 ipa_tools.py
print("""

    ██╗██████╗  █████╗     ████████╗ ██████╗  ██████╗ ██╗     ███████╗
    ██║██╔══██╗██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
    ██║██████╔╝███████║       ██║   ██║   ██║██║   ██║██║     ███████╗
    ██║██╔═══╝ ██╔══██║       ██║   ██║   ██║██║   ██║██║     ╚════██║
    ██║██║     ██║  ██║       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
    ╚═╝╚═╝     ╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝

GitHub : https://github.com/Emilien-B/IPAtools
By Emilien BARDE (https://twitter.com/emilien_barde)
""")
path = ""
while path == "":
    
    path = str(input("Drag and drop the file "))
    
    try:
        
        path_desktop = "/"+path.split("/")[1]+"/"+path.split("/")[2]+"/Desktop"
    except:
        print("Invalid path")
        path = ""

if path.find(".ipa") >= 1:
    os.chdir(path_desktop+"/IPA Export")
    name = path.split(".ipa")[0].split("/")
    name = name[len(name)-1]
    os.mkdir(name)
    os.chdir(name)
    os.system("tar -xf " + path)
else:
    name = input("Enter a name for your file ")
    while name.count(".")>1 or name.count("/")>1 or name.count(u"\x5c")>1:
        print("Invalid name")
        name = input("Enter a name for your file ")

    path = path.rstrip()+"/Products/Applications"
    path_ = path.replace(u"\x5c","") 
    
    os.chdir(path_)
    os.mkdir("Payload")
    os.system("mv Runner.app Payload")
    os.system("tar -cf " + name+".ipa Payload")
    os.system("mv Payload/Runner.app Runner.app")
    os.rmdir("Payload")
    print(path_desktop)
    os.chdir(path_desktop)
    try:
        os.mkdir("IPA Export")
    except:
        pass
    os.system("mv "+ path + "/" + name+".ipa " + path_desktop+"/IPA\ Export")
os.system("open " + path_desktop+"/IPA\ Export")
os.system("clear")
print("Finished")

