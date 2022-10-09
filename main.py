from requests.structures import CaseInsensitiveDict
from colorama import *
from pystyle import *
import requests
import os

os.system('cls')                                                                                                                                                                                                                                                                                                                 ,System.Title("title H.y.p.e. s.q.u.a.d. c.h.a.n.g.e.r. .-. B.y. X.a.r.a.".replace('.',''))

print(Colorate.Vertical(Colors.red_to_yellow, '''
           _                                                  _        _                                 
          | |                                                | |      | |                                
          | |__  _   _ _ __   ___   ___  __ _ _   _  __ _  __| |   ___| |__   __ _ _ __   __ _  ___ _ __ 
          | '_ \| | | | '_ \ / _ \ / __|/ _` | | | |/ _` |/ _` |  / __| '_ \ / _` | '_ \ / _` |/ _ \ '__|
          | | | | |_| | |_) |  __/ \__ \ (_| | |_| | (_| | (_| | | (__| | | | (_| | | | | (_| |  __/ |   
          |_| |_|\__, | .__/ \___| |___/\__, |\__,_|\__,_|\__,_|  \___|_| |_|\__,_|_| |_|\__, |\___|_|   
                  __/ | |                  | |                                            __/ |          
                 |___/|_|                  |_|                                           |___/           By >_xara\n\n\n
''', 1))



token = input(f'{Fore.LIGHTYELLOW_EX}[{Fore.RED}+{Fore.LIGHTYELLOW_EX}] {Fore.RED}Token {Fore.LIGHTYELLOW_EX}> ')
url = "https://discord.com/api/v9/hypesquad/online"
id = input(f'\n{Fore.LIGHTYELLOW_EX}[{Fore.RED}+{Fore.LIGHTYELLOW_EX}] {Fore.YELLOW}What house do you want {Fore.RED}1: {Fore.YELLOW}Bravery  {Fore.RED}2: {Fore.YELLOW}Brilliance  {Fore.RED}3: {Fore.YELLOW}Balance  {Fore.LIGHTYELLOW_EX}> {Fore.RESET}')
headers = CaseInsensitiveDict()
headers["Authorization"] = token
headers["Content-Type"] = "application/json"

data = '{"house_id":' + id + '}'
resp = requests.post(url, headers=headers, data=data)


if resp.status_code == 204:
    input(f'\n\n                                                    {Fore.RED}Success !\n \n                                             {Fore.LIGHTYELLOW_EX}Press Enter to Exit . . .{Fore.RESET}')


if resp.status_code != 204:
    input(f'\n\n                                                    {Fore.RED}Fail. Press enter to exit. {Fore.LIGHTYELLOW_EX}Error code ' + str(resp.status_code) + Fore.RESET)