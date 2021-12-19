import os
from rich import print

# Print the title
print("""

    ██╗██████╗  █████╗     ████████╗ ██████╗  ██████╗ ██╗     ███████╗
    ██║██╔══██╗██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
    ██║██████╔╝███████║       ██║   ██║   ██║██║   ██║██║     ███████╗
    ██║██╔═══╝ ██╔══██║       ██║   ██║   ██║██║   ██║██║     ╚════██║
    ██║██║     ██║  ██║       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
    ╚═╝╚═╝     ╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝

[bold]GitHub[/bold] : https://github.com/Emilien-B/IPAtools
By [bold]Emilien BARDE[/bold] (https://twitter.com/emilien_barde)
""")

print("""
1. Exporter a file .ipa
2. Décompresser a file .ipa
3. CRéer un fichier .plist de téléchargement

""")
choose = int(input("Enter a number..."))
path_desktop = ""
# a = input("Drag and drop the file ")
a = ""

def check_path(a):
    # Check the path
    try:
        path_desktop = str("/"+a.split("/")[1]+"/"+a.split("/")[2]+"/Desktop")
        return path_desktop
    except:
        print("Invalid path")
        return False

if choose==1:
    choose_path()
    name = input("Enter a name for your file ")

    # Check the name
    try: 
        name = str(name)
    except:
        print("Invalid name")
        name = input("Enter a name for your file ")

    while name.count(".")>1 or name.count("/")>1 or name.count(u"\x5c")>1:
        print("Invalid name")
        name = input("Enter a name for your file ")

    path = path.rstrip()+"/Products/Applications"
    path_ = path.replace(u"\x5c","") 
    
    # Define the correct file structure
    os.chdir(path_)
    os.mkdir("Payload")
    os.system("mv Runner.app Payload")

    # Create the .ipa file
    os.system("zip -ru " + name+".ipa Payload")

    # Define the old file structure
    os.system("mv Payload/Runner.app Runner.app")
    os.rmdir("Payload")
    os.chdir(path_desktop)

    # Create the IPA Export directory
    try:
        os.mkdir("IPA Export")
    except:
        pass
    os.system("mv "+ path + "/" + name+".ipa " + path_desktop+"/IPA\ Export")

if choose==2:
    path = input("Drag and drop the file ")
    print(check_path(path))
    while check_path(path) == False:
        path = input("Drag and drop the file ")
    
    # Create a folder with the file's name
    os.chdir(path_desktop+"/IPA Export")
    name = path.split(".ipa")[0].split("/")
    name = name[len(name)-1]
    os.mkdir(name)
    os.chdir(name)

    # Unzip the file
    os.system("tar -xf " + path)

# Open the folder
os.system("open " + path_desktop+"/IPA\ Export")

os.system("clear")
print("Finished")

