import os
import fade
import gratient
import time
import requests
from dhooks import Webhook

os.system("title 𝘿𝙀𝙏𝙍𝘼𝙓 𝙒𝙚𝙗𝙊𝙥𝙥")

print(fade.purpleblue("""

██████   ██████  ██   ██ ██     ██ ███████ ██████  ██   ██  ██████   ██████  ██   ██ 
██   ██ ██    ██  ██ ██  ██     ██ ██      ██   ██ ██   ██ ██    ██ ██    ██ ██  ██  
██   ██ ██    ██   ███   ██  █  ██ █████   ██████  ███████ ██    ██ ██    ██ █████   
██   ██ ██    ██  ██ ██  ██ ███ ██ ██      ██   ██ ██   ██ ██    ██ ██    ██ ██  ██  
██████   ██████  ██   ██  ███ ███  ███████ ██████  ██   ██  ██████   ██████  ██   ██ 
                                                                                     
                d        e        t        r       a        x                                                                     
                                                                                     
                                                                                     """))

hook = Webhook(input(gratient.purple(" WEBHOOK : ")))
hook.get_info()
print(gratient.blue(f"\n GUILD ID    : {hook.guild_id}"))
print(gratient.blue(f" CHANNEL ID  : {hook.channel_id}"))
print(gratient.blue(f" USERNAME    : {hook.default_name}"))
print(gratient.blue(f" IMAGE       : {hook.default_avatar_url}"))

time.sleep(3)

input(gratient.blue("""
[@]The webhook deleter option will start, if you want to use it, press enter once, if you want to cancel that, press enter button twice.
"""))

os.system("cls")

print(fade.purpleblue("""


██     ██ ███████ ██████  ██████  ███████ ██      ███████ ████████ ███████ ██████  
██     ██ ██      ██   ██ ██   ██ ██      ██      ██         ██    ██      ██   ██ 
██  █  ██ █████   ██████  ██   ██ █████   ██      █████      ██    █████   ██████  
██ ███ ██ ██      ██   ██ ██   ██ ██      ██      ██         ██    ██      ██   ██ 
 ███ ███  ███████ ██████  ██████  ███████ ███████ ███████    ██    ███████ ██   ██ 
                                                                                   
         d      e      t      r      a      x                                                                        
                                                                                 
                                                                                   """))

webhook = input(gratient.purple(" [INPUT] ENTER THE WEBHOOK TO DELETE : "))

def delete():
    requests.delete(webhook)
    check = requests.get(webhook)
    if check.status_code == 404:
        print(gratient.blue("\n [LOGS] WEBHOOK SUCCESFULLY DELETED"))
        os.system("pause >nul")  
    elif check.status_code == 200:
        print(gratient.blue("\n [LOGS] FAILED TO DELETE WEBHOOK"))
        os.system("pause >nul")

test = requests.get(webhook)
if test.status_code == 404:
    print(gratient.blue("\n [LOGS] THE WEBHOOK IS INVALID"))
    os.system("pause >nul")
elif test.status_code == 200:
    print(gratient.blue("\n [LOGS] THE WEBHOOK IS VALID"))
    delete()



