import os
from rich import print
os.system("clear")
# Print the title
print("""

    ██╗██████╗  █████╗     ████████╗ ██████╗  ██████╗ ██╗     ███████╗
    ██║██╔══██╗██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
    ██║██████╔╝███████║       ██║   ██║   ██║██║   ██║██║     ███████╗
    ██║██╔═══╝ ██╔══██║       ██║   ██║   ██║██║   ██║██║     ╚════██║
    ██║██║     ██║  ██║       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
    ╚═╝╚═╝     ╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝

By [bold]Emilien BARDE[/bold] (https://twitter.com/emilien_barde)
""")

print("""
1. Exporter a file .ipa
2. Décompresser a file .ipa
3. CRéer un fichier .plist de téléchargement
4. Accéder au projet sur GitHub

""")
choose = int(input("Enter a number..."))


def check_path(a):
    # Check the path
    try:
        path_desktop = str("/"+a.split("/")[1]+"/"+a.split("/")[2]+"/Desktop")
        return path_desktop
    except:
        print("Invalid path")
        return False

if choose==1:

    path = input("Drag and drop the file ")

    # Check the path
    while check_path(path) == False:
        path = input("Drag and drop the file ")
    
    # ???
    path_desktop = check_path(path)

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

    # Check the path
    while check_path(path) == False:
        path = input("Drag and drop the file ")
    
    # ???
    path_desktop = check_path(path)

    # Create a folder with the file's name
    os.chdir(path_desktop+"/IPA Export")
    name = path.split(".ipa")[0].split("/")
    name = name[len(name)-1]
    os.mkdir(name)
    os.chdir(name)

    # Unzip the file
    os.system("tar -xf " + path)
if choose == 4:
    os.system("open https://github.com/Emilien-B/IPAtools")
    os.system("clear")
    print("Finished")
    quit()

# Open the folder
os.system("open " + path_desktop+"/IPA\ Export")

os.system("clear")
print("Finished")

