import os

# Define styles
error_style = 'red bold'
loading_style = 'blue'

try:
    from rich import print
    from rich.status import Status
    from pyfade import Fade,Colors
except:
    # Display loader
    with Status('['+loading_style+']Waiting \n [/'+loading_style+']', spinner='aesthetic', spinner_style=loading_style):
        # Install rich
        os.system('pip install rich')
    try:
        from rich import print
        from rich.status import Status
        from pyfade import Fade,Colors
    except:
        print('['+error_style+']rich package needed[/'+error_style+']')

# Print 'Finished'
def print_finised():
    print('[green] :white_heavy_check_mark: Finished[/green]')

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

def check_choose(a):
    try:
        a = int(a)
        return a <= 4
    except:
        return False

os.system('clear')




# Print the title
print("""
[cyan]
    ██╗██████╗  █████╗     ████████╗ ██████╗  ██████╗ ██╗     ███████╗
    ██║██╔══██╗██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
    ██║██████╔╝███████║       ██║   ██║   ██║██║   ██║██║     ███████╗
    ██║██╔═══╝ ██╔══██║       ██║   ██║   ██║██║   ██║██║     ╚════██║
    ██║██║     ██║  ██║       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
    ╚═╝╚═╝     ╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
[/cyan]""")

print("""By [bold blue]Emilien BARDE[/bold blue] (https://twitter.com/emilien_barde)

1. :package: Export a .ipa file
2. :open_file_folder: Decompress a .ipa file
3. :down_arrow:  Create a download file .plist
4. :cat: Access the project on GitHub
""")
choose = input('Choose an option...')
while not check_choose(choose):
    print('['+error_style+']Invalid choice[/'+error_style+']')
    choose = input('Choose an option...')
choose = int(choose)

# Get the path of the desktop
path_desktop = str(os.popen('pwd').read()).replace("b'",'').replace(u"\x5cn'",'').replace('\n','')
path_desktop = str('/'+path_desktop.split('/')[1]+'/'+path_desktop.split('/')[2]+'/Desktop')

# Create the IPAtools-exports directory
try:
    os.mkdir(path_desktop+'/IPAtools-exports')
except:
    pass

# Export a .ipa file
if choose==1:

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

    os.system('clear')
    print_finised()

# Decompress a .ipa file
if choose==2:
    
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
    os.system('clear')
    print_finised()

# Create a download file .plist
if choose == 3:

    url = str(input('Enter a URL '))
    # Check the URL
    while url.count('http')==0 or url.count('://')==0 or url.count('.ipa')==0:
        print('['+error_style+']Invalid URL[/'+error_style+']')
        url = input('Enter a URL ')
    
    bundle_identifier = str(input('Enter the bundle identifier '))
    # Check the bundle identifier
    while bundle_identifier=='':
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
    file = open(path_desktop+'/IPAtools-exports/'+name+'.plist', 'w')
    file.write(plist_file)
    file.close()

    print("""[white]
╭──────────────────────────────────────────────────── ❗IMPORTANT❗ ─────────────────────────────────────────────────────╮
│                                                                                                                        │
│                             Le fichier doit obligatoirement être renommer manifest.plist.                              │
│                                                                                                                        │
│                                         URL d'installation de l'application :                                          │
│                  itms-services://?action=download-manifest&url=https://url_du_fichier_manifest.plist                   │
│                                                                                                                        │
│                Share this link to your testers or friends, they will be able to install the .ipa file.                 │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
[/white]""")
    input("It's ok ?")

    print_finised()

# Access the project on GitHub
if choose == 4:

    # Open the webpage
    os.system('open https://github.com/Emilien-B/IPAtools')

    os.system('clear')
    print_finised()
    quit()

# Open the folder
os.system('open ' + path_desktop+'/IPAtools-exports')

