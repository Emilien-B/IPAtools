import os

# Print the title
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
    path = input("Drag and drop the file ")

    # Check the path
    try:
        path_desktop = str("/"+path.split("/")[1]+"/"+path.split("/")[2]+"/Desktop")
    except:
        print("Invalid path")
        path = ""

if path.find(".ipa") >= 1:

    # Create a folder with the file's name
    os.chdir(path_desktop+"/IPA Export")
    name = path.split(".ipa")[0].split("/")
    name = name[len(name)-1]
    os.mkdir(name)
    os.chdir(name)

    # Unzip the file
    os.system("tar -xf " + path)

else:
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
    os.system("tar -cf " + name+".ipa Payload")

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

# Open the folder
os.system("open " + path_desktop+"/IPA\ Export")

os.system("clear")
print("Finished")

