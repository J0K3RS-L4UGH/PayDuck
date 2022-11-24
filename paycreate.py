import os
import argparse

parser = argparse.ArgumentParser(description='A program to create rubber ducky scripts')
parser.add_argument("wordlist", help="The wordlist file [i.e. ~/Wordlists/Wordlist.txt]")
parser.add_argument("payload", help="The file you want the payload to be saved as [i.e. ~/Payloads/Payload.txt]")
parser.add_argument("-b", "--break_time", help="The seconds in between typing the words", default="0.5")

args = parser.parse_args()


with open(args.payload, 'w') as firstr:
    firstr.write('STRING ')


with open(args.wordlist) as inf, open(args.payload, 'a') as outf:
    outf.write(next(inf))
    for line in inf:
        outf.write("ENTER\nDELAY " + args.break_time + "\n")
        outf.write('STRING ' + line)

