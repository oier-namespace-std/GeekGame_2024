shift = False
capsLck = False
keyA = 0

# src | https://www.bejson.com/othertools/keycodes/

while(True):
    s = input().split(' ')
    lastKey = ''
    
    if(s[0] == 'keyAction'):
        z = int(s[1][1:-2])
        keyA = z
    if(s[0] == 'keyCode'):
        z = int(s[1][1:-2], 16) - 32768
        # print('keyCode', z)
        if(keyA == 3):
            # press
            if(z == 0x10):
                shift = True
            elif(z == 219):
                if(shift): c = '{' 
                else : c = '['
            elif(z == 221):
                if(shift): c = '}' 
                else : c = ']'
            elif(z >= 65 and z <= 90):
                if(shift): c = chr(z) 
                else : c = chr(z + 32)
            else: c = ''
            print(c, end = '')
        if(keyA == 4):
            # pop
            if(z == 0x10):
                shift = False
            pass

# shifupymahebadagewosxueshengyigexingbuflag[onlyapplecando]dengxiayouneiguihaodehaod
