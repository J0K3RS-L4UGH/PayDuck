wordlist = input('What wordlist do you want to use?: ')
payload = input('Waht do you want the payload to be called?: ')

with open(wordlist) as inf, open(payload, 'w') as outf:
    outf.write('STRING ', next(inf))
    for line in inf:
        outf.write("ENTER\nDELAY 0.5\n")
        outf.write(line)
