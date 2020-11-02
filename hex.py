import sys

mode = sys.argv[1]
keyfile = sys.argv[2]
inpfile = sys.argv[3]

key = open(keyfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
inp = open(inpfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
debug = False


if(debug):
    print('mode:'+mode)
    print('key: '+key)
    print('inp: '+inp)

if len(inp) > len(key): #repeats key to length of input
    repeats = (len(inp) // len(key)) + 1
    key2 = key * repeats
    key = key2[:len(inp)]

output = ''
i = 0
while (i < len(inp)):
    add = chr(ord(inp[i] ^ ord(key[i])))
    if (mode == 'human'):
        output += add
    else:
        output += hex(add)[2:] + ''
print (output)
    

    
    
    
