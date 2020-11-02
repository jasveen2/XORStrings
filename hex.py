import sys

mode = sys.argv[1]
keyfile = sys.argv[2]
inpfile = sys.argv[3]

key = open(keyfile + '.txt').read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
inp = open(inpfile + '.txt').read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
debug = True


if(debug):
    print('mode:'+mode)
    print('key: '+key)
    print('inp: '+inp)

if len(inp) > len(key): #repeats key to length of input
    repeats = (len(inp) // len(key)) + 1
    key2 = key * repeats
    key = key2[:len(inp)]

output = ''
for i in range(len(inp)):
    inpd = ord(inp[i])
    keyd = ord(key[i])
    add = inpd ^ keyd
    if (mode == 'human'):
        output += chr(add)
    else:
        hexadd = hex(add)
        output += hexadd[2:] + ' '
    i += 1
print (output)
    

    
    
    
