import os
import time
name=str(input('Enter the name you want ingame: '))
subpath ="Goldberg SteamEmu Saves/settings/account_name.txt"
file=open(os.path.join(os.getenv('APPDATA'),subpath),mode="w+")
file.write(name)
print('Success, name set to: ',name)
time.sleep(10)