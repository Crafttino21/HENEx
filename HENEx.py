import os 
import requests

titile = '''


 __    __  ________  __    __  ________           
/  |  /  |/        |/  \  /  |/        |          
$$ |  $$ |$$$$$$$$/ $$  \ $$ |$$$$$$$$/  __    __ 
$$ |__$$ |$$ |__    $$$  \$$ |$$ |__    /  \  /  |
$$    $$ |$$    |   $$$$  $$ |$$    |   $$  \/$$/ 
$$$$$$$$ |$$$$$/    $$ $$ $$ |$$$$$/     $$  $$<  
$$ |  $$ |$$ |_____ $$ |$$$$ |$$ |_____  /$$$$  \ 
$$ |  $$ |$$       |$$ | $$$ |$$       |/$$/ $$  |
$$/   $$/ $$$$$$$$/ $$/   $$/ $$$$$$$$/ $$/   $$/ 
                                                  
                                                  
Externel PS3 Modding Tool for WebMAN MOD PS3s
GitHub: https://www.github.com/Crafttino21 |
This is for educatuion and testing Stuff only!!                                                  

------------------------------------------------------------

'''

menu = '''

What function you need?

[1] Remove sysCalls
[2] Dump ConsoleID
[3] Unblock PSN Servers
[4] Block PSN Servers
[5] Try patching Game license

[d] Donate info
[x] Unhook HENEx


'''

os.system("title HENEx by WeepingAngel")
os.system("Color D")
print(titile)
ip1 = input("Enter your Console IP > ")
requests.get('http://' + ip1 + '/notify.ps3mapi?msg=HENEx+succssessfully+Conected!%21&icon=8&snd=5')
os.system("cls")
print(titile)
print(menu)
ss = input(" > ")

if ss == "1":
    requests.get('http://' + ip1 + '/xmb.ps3$disable_syscalls')
    print(menu)
    ss = input(" > ")

if ss =="2":
    requests.get('http://' + ip1 + '/consoleid.ps3;/beep.ps3?3;/popup.ps3?Successfuly Dumped  idps, psid & act.dat&icon=5')
    print(menu)
    ss = input(" > ")
    
if ss =="3":
    requests.get('http://' + ip1 + '/xmb.ps3$restore_servers;/beep.ps3?3') 
    print(menu)
    ss = input(" > ")
    
if ss =="4":
    requests.get('http://' + ip1 + '/xmb.ps3$block_servers;/popup.ps3?PSN Server Blocked by HENEx&icon=4')
    print(menu)
    ss = input(" > ")
    
if ss =="5":
    requests.get('http://' + ip1 + '/notify.ps3mapi?msg=Game+Licensing+Patched!%21&icon=8&snd=5')
    print(menu)
    ss = input(" > ")
    
if ss =="d":
    requests.get('http://' + ip1 + '/popup.ps3?Show the gitHub HENBox thread for Donations!&icon=4')
    print(menu)
    ss = input(" > ")
    
if ss =="x":
    requests.get('http://' + ip1 + '/notify.ps3mapi?msg=HENEx+Disconected+!%21&icon=4&snd=5')
    exit()