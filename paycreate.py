wordlist = input('What wordlist do you want to use?: ')
payload = input('Waht do you want the payload to be called?: ')

with open(payload, 'w') as firstr:
    firstr.write('STRING ')


with open(wordlist) as inf, open(payload, 'a') as outf:
    outf.write(next(inf))
    for line in inf:
        outf.write("ENTER\nDELAY 0.5\n")
        outf.write('STRING ' + line)
