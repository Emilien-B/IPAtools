import os
import subprocess
from rich import print

os.system('clear')

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
choose = int(input('Enter a number...'))

# Get the path of the desktop
path_desktop = str(subprocess.check_output("pwd", shell=True)).replace("b'",'').replace(u"\x5cn'",'')
path_desktop = str('/'+path_desktop.split('/')[1]+'/'+path_desktop.split('/')[2]+'/Desktop')

# Check the name file
def check_name_file(name):
    return not name.count('.')>=1 or name.count('/')>=1 or name.count(u'\x5c')>=1

# Check the path
def check_path(a):
    try:
        a = a.strip().replace(u"\x5cn'",'')
        return True
    except:
        return False

# Create the IPAtools-exports directory
def create_directory():
    try:
        os.chdir(path_desktop)
        os.mkdir('IPAtools-exports')
    except:
        pass

# ?
if choose==1:

    create_directory()

    path = input('Drag and drop the file ')

    # Check the path
    while check_path(path) == False:
        print('Invalid path')
        path = input('Drag and drop the file ')
    
    # Check the file
    while path.count('.xcarchive') == 0:
        print('Invalid file')
        path = input('Drag and drop the file ')
    

    name = input('Enter a name for your file ')

    # Check the name
    name = str(name)
    while check_name_file(name) == False:
        print('Invalid name')
        name = input('Enter a name for your file ')

    path = path.rstrip()+'/Products/Applications'
    path_ = path.replace(u'\x5c','') 
    
    # Define the correct file structure
    os.chdir(path_)
    os.mkdir('Payload')
    os.system('mv Runner.app Payload')

    # Create the .ipa file
    os.system('zip -ru ' + name+'.ipa Payload')

    # Define the old file structure
    os.system('mv Payload/Runner.app Runner.app')
    os.rmdir('Payload')
    os.chdir(path_desktop)

    # Move the file
    os.system('mv '+ path + '/' + name+'.ipa ' + path_desktop+'/IPAtools-exports')

if choose==2:

    create_directory()

    path = input('Drag and drop the file ')

    # Check the path
    while check_path(path) == False:
        print("Invalid path")
        path = input('Drag and drop the file ')

    # Chech the file
    while path.count('.ipa') == 0:
        print('Invalid file')
        path = input('Drag and drop the file ')

    # Create a folder with the file's name
    os.chdir(path_desktop+'/IPAtools-exports')
    name = path.split('.ipa')[0].split('/')
    name = name[len(name)-1]
    os.mkdir(name)
    os.chdir(name)

    # Unzip the file
    os.system('tar -xf ' + path)

if choose == 3:

    create_directory()

    url = str(input('Enter a URL '))
    # Check the URL
    while url.count('http')==0 or url.count('://')==0 or url.count('.ipa')==0:
        print('Invalid URL')
        url = input('Enter a URL ')
    
    bundle_identifier = str(input('Enter the bundle identifier '))
    # Check the bundle identifier
    while bundle_identifier=="":
        bundle_identifier = str(input('Enter the bundle identifier '))

    bundle_version = str(input('Enter the bundle version '))
    # Check the bundle version
    while bundle_version.replace('.','').isdigit() == False:
        print('Invalid bundle version')
        bundle_version = str(input('Enter the bundle version '))

    title = str(input('Enter the title '))
    # Check the title
    while check_name_file(title) == False:
        print('Invalid title')
        title = str(input('Enter the title '))

    # Generate the file
    plist_file =   """<?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>
        <key>items</key>
        <array>
            <dict>
                <key>assets</key>
                <array>
                    <dict>
                        <key>kind</key>
                        <string>software-package</string>
                        <key>url</key>
                        <string>"""+ url +"""</string>
                    </dict>
                </array>
                <key>metadata</key>
                <dict>
                    <key>bundle-identifier</key>
                    <string>"""+ bundle_identifier +"""</string>
                    <key>bundle-version</key>
                    <string>"""+ bundle_version +"""</string>
                    <key>kind</key>
                    <string>software</string>
                    <key>title</key>
                    <string>"""+ title +"""</string>
                </dict>
            </dict>
        </array>
    </dict>
    </plist>"""

    name = input('Enter a name for your file ')

    # Check the name
    name = str(name)
    while check_name_file(name) == False:
        print('Invalid name')
        name = input('Enter a name for your file ')
    
    # Save the file
    file = open(path_desktop+'/IPAtools-exports/'+name+".plist", 'w')
    file.write(plist_file)
    file.close()

if choose == 4:

    # Open the webpage
    os.system('open https://github.com/Emilien-B/IPAtools')
    
    os.system('clear')
    print('Finished')
    quit()

# Open the folder
os.system('open ' + path_desktop+'/IPAtools-exports')

os.system('clear')
print('Finished')

