import os
from rich import print
from rich.status import Status


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

def check_choose(a):
    try:
        a = int(a)
        return a <= 4
    except:
        return False


os.system('clear')

# Define styles
error_style = 'red'
loading_style = 'blue'

# Display loader
with Status('['+loading_style+']Waiting[/'+loading_style+']', spinner='aesthetic', spinner_style=loading_style):
    # Install rich
    os.system('pip install rich')
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
1. :package: Export a .ipa file
2. :open_file_folder: Decompress a .ipa file
3. :down_arrow:  Create a download file .plist
4. :cat: Access the project on GitHub

""")
choose = input('Enter a number...')
while not check_choose(choose):
    choose = input('Enter a number...')


# Get the path of the desktop

path_desktop = str(os.popen('pwd').read()).replace("b'",'').replace(u"\x5cn'",'')
path_desktop = str('/'+path_desktop.split('/')[1]+'/'+path_desktop.split('/')[2]+'/Desktop')

# ?
if choose==1:

    create_directory()

    path = input('Drag and drop the file ')

    # Check the path
    while not check_path(path):
        print('['+error_style+']Invalid path[/'+error_style+']')
        path = input('Drag and drop the file ')
    
    # Check the file
    while path.count('.xcarchive') == 0:
        print('['+error_style+']Invalid file[/'+error_style+']')
        path = input('Drag and drop the file ')
    

    name = input('Enter a name for your file ')

    # Check the name
    name = str(name)
    while not check_name_file(name):
        print('['+error_style+']Invalid name[/'+error_style+']')
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
    while not check_path(path):
        print('['+error_style+']Invalid path[/'+error_style+']')
        path = input('Drag and drop the file ')

    # Chech the file
    while path.count('.ipa') == 0:
        print('['+error_style+']Invalid file[/'+error_style+']')
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
        print('['+error_style+']Invalid URL[/'+error_style+']')
        url = input('Enter a URL ')
    
    bundle_identifier = str(input('Enter the bundle identifier '))
    # Check the bundle identifier
    while bundle_identifier=="":
        bundle_identifier = str(input('Enter the bundle identifier '))

    bundle_version = str(input('Enter the bundle version '))
    # Check the bundle version
    while not bundle_version.replace('.','').isdigit():
        print('['+error_style+']Invalid bundle version[/'+error_style+']')
        bundle_version = str(input('Enter the bundle version '))

    title = str(input('Enter the title '))
    # Check the title
    while not check_name_file(title):
        print('['+error_style+']Invalid title[/'+error_style+']')
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
    while not check_name_file(name):
        print('['+error_style+']Invalid name[/'+error_style+']')
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

