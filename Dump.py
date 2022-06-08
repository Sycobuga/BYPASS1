import os, platform
try:
    import requests
except:
    os.system('pip install requests')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from Dump import Menu
    Menu()
elif bit == '32bit':
    print("\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools")
