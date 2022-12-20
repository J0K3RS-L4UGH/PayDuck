import os
import argparse


parser = argparse.ArgumentParser(description='A program to create rubber ducky scripts')
parser.add_argument("wordlist", help="The wordlist file [i.e. ~/Wordlists/Wordlist.txt]")
parser.add_argument("payload", help="The file you want the payload to be saved as [i.e. ~/Payloads/Payload.txt]")
parser.add_argument("-b", "--break_time", help="The time in milliseconds between typing the words", default="500")

class bcolors:
    RED = '\033[1;31;40m'
    ENDC = '\033[0m'

args = parser.parse_args()

print(f'''{bcolors.RED}

 ██▓███   ▄▄▄     ▓██   ██▓▓█████▄  █    ██  ▄████▄   ██ ▄█▀
▓██░  ██▒▒████▄    ▒██  ██▒▒██▀ ██▌ ██  ▓██▒▒██▀ ▀█   ██▄█▒ 
▓██░ ██▓▒▒██  ▀█▄   ▒██ ██░░██   █▌▓██  ▒██░▒▓█    ▄ ▓███▄░ 
▒██▄█▓▒ ▒░██▄▄▄▄██  ░ ▐██▓░░▓█▄   ▌▓▓█  ░██░▒▓▓▄ ▄██▒▓██ █▄ 
▒██▒ ░  ░ ▓█   ▓██▒ ░ ██▒▓░░▒████▓ ▒▒█████▓ ▒ ▓███▀ ░▒██▒ █▄
▒▓▒░ ░  ░ ▒▒   ▓▒█░  ██▒▒▒  ▒▒▓  ▒ ░▒▓▒ ▒ ▒ ░ ░▒ ▒  ░▒ ▒▒ ▓▒
░▒ ░       ▒   ▒▒ ░▓██ ░▒░  ░ ▒  ▒ ░░▒░ ░ ░   ░  ▒   ░ ░▒ ▒░
░░         ░   ▒   ▒ ▒ ░░   ░ ░  ░  ░░░ ░ ░ ░        ░ ░░ ░ 
               ░  ░░ ░        ░       ░     ░ ░      ░  ░   
                   ░ ░      ░               ░               
{bcolors.ENDC}''')

with open(args.payload, 'w') as firstr:
    firstr.write('STRING ')


with open(args.wordlist) as inf, open(args.payload, 'a') as outf:
    outf.write(next(inf))
    for line in inf:
        outf.write("ENTER\nDELAY " + args.break_time + "\n")
        outf.write('STRING ' + line)

finished = input('Your file has been saved to ' + args.payload + '. Would you like to view the contents of it [y/n]?: ')
if finished == 'y':
    os.system('cat ' + args.payload)
else:
    pass
