# ━━━━━━━━━━━━━━━
#C:\Users\Пользователь\PArseKrypto\main.py

import os, sys, time
import random

from colorama import Fore, Back, Style, init

init()

AskLogo = open('scr/Logo.txt', 'r').read().split('/')[0]
SetLogo = open('scr/Logo.txt', 'r').read().split('/')[1]

mainp = 'main.py'
mainl = 'scr/main.log'
mainc = 'scr/main.config'

def Setup():

    print(f'{Style.BRIGHT + SetLogo + Style.NORMAL}\n')
    r = open('scr/setup.log', 'r').read()
    open('scr/setup.log', 'w+').write(f'{r}log id{time.time()} #{time.localtime().tm_sec}s.{time.localtime().tm_min}m.{time.localtime().tm_mday}d.{time.localtime().tm_mon}m.{time.localtime().tm_year}y\n')
    del r
    input('Press Enter for Start Setup')
    m = 0

    #Setup visible
    for r in range(0, 30):
        gr = ''
        df = ''
        for i in range(0, r):
            gr += f'{Fore.GREEN}━'
        for i in range(r, 30):
            df += f'{Fore.WHITE}━'
        m += random.randint(1, 5)
        print(gr+df+f' Download: {m}mb / 147mb')
    print(f'{Fore.GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Download: 147mb / 147mb')
    del m

    r = '''import os, sys, time, random, pathlib
import traceback

from colorama import Fore, Back, Style, init

init()

print(f'{Style.BRIGHT + open("scr/Logo.txt", "r").read().split("/")[1]}\\n')

log = 'fDES.py'
path = os.getcwd()

while True:
    try:
        i = input(f'{Style.BRIGHT + Fore.RED}{path} {Style.NORMAL + Fore.RESET}$')
        if i == 'exit()':
            r = open('scr/DES.log', 'r').read()
            open('scr/DES.log', 'w+').write(f'{r}{log};log id{time.time()} #{time.localtime().tm_sec}s.{time.localtime().tm_min}m.{time.localtime().tm_mday}d.{time.localtime().tm_mon}m.{time.localtime().tm_year}y\\n')
            break; break; break;
        elif i == 'back' or i == 'bk':
            log += f',{i}'
            path = pathlib.Path(path).parent
        elif i == 'directory' or i == 'dir':
            log += f',{i}'
            fs = sorted(os.listdir(path))
            for item in fs:
                print(item)
        elif i.split(' ')[0] == 'sd':
            log += f',{i}'
            if i.split(' ')[1] != '..' and i.split(' ')[1] != '.' and pathlib.Path(path+'/'+i.split(' ')[1]).exists():
                path = pathlib.Path(path+'/'+i.split(' ')[1])
        elif i.split(' ')[0] == 'rd':
            log += f',{i}'
            if pathlib.Path(path+'/'+i.split(' ')[1]).exists():
                print(open(path+'/'+i.split(' ')[1], 'r').read())
        elif i.split(' ')[0] == 'wr':
            log += f',{i}'
            if pathlib.Path(path + '/' + i.split(' ')[1]).exists():

                open(path + '/' + i.split(' ')[1], 'w+').write(input(f'{Style.BRIGHT + Fore.RED}{path + "/" + i.split(" ")[1]}*write {Style.NORMAL + Fore.RESET}%'))
    except Exception:
        print(f'error')
        log += f',error\''''
    open('DES.py', 'w+').write(r); print(f'Create DES.py #{time.localtime().tm_sec}s.{time.localtime().tm_min}m')
    del r

    open('scr/DES.log', 'w+')

    open('scr/setup.backup', 'w+').write(open('setup.py', 'r').read())
    os.remove('setup.py')

Setup()