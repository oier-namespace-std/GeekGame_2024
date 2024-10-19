import random
import base64

# flag1 = "flag{you_Ar3_tHE_MaSTer_OF_PY7h0n}"
# from pymaster_extracted/PYZ-00.pyz_extracted/random.pyc: 
# flag2 = "flag{wElc0me_tO_THe_w0RlD_OF_pYtHON}"
# flag3 = "flag{0123456789bchijkmnopqrstuvwxyz}"

class RotateR:
    def __init__(thiseng, r1, r2):
        thiseng.r1 = r1
        thiseng.r2 = r2
        thiseng.Father = None
        thiseng.Lson = None
        thiseng.Rson = None


class Engine:
    def __init__(thiseng):
        thiseng.root = None

    def Engine(thiseng, node):
        while node.Father != None:
            if node.Father.Father == None:
                if node == node.Father.Lson:
                    thiseng.RotateR(node.Father)
                else:
                    thiseng.RotateL(node.Father)
            elif (
                node == node.Father.Lson
                and node.Father == node.Father.Father.Lson
            ):
                thiseng.RotateR(node.Father.Father)
                thiseng.RotateR(node.Father)
            elif (
                node == node.Father.Rson
                and node.Father == node.Father.Father.Rson
            ):
                thiseng.RotateL(node.Father.Father)
                thiseng.RotateL(node.Father)
            elif (
                node == node.Father.Rson
                and node.Father == node.Father.Father.Lson
            ):
                thiseng.RotateL(node.Father)
                thiseng.RotateR(node.Father)
            else:
                thiseng.RotateR(node.Father)
                thiseng.RotateL(node.Father)

    def RotateL(thiseng, x):
        y = x.Rson
        x.Rson = y.Lson
        if y.Lson != None:
            y.Lson.Father = x
        y.Father = x.Father
        if x.Father == None:
            thiseng.root = y
        elif x == x.Father.Lson:
            x.Father.Lson = y
        else:
            x.Father.Rson = y
        y.Lson = x
        x.Father = y

    def RotateR(thiseng, x):
        y = x.Lson
        x.Lson = y.Rson
        if y.Rson != None:
            y.Rson.Father = x
        y.Father = x.Father
        if x.Father == None:
            thiseng.root = y
        elif x == x.Father.Rson:
            x.Father.Rson = y
        else:
            x.Father.Lson = y
        y.Rson = x
        x.Father = y

    def iterate(thiseng, r1, r2):
        node = RotateR(r1, r2)
        eng_key = thiseng.root
        Father = None
        while eng_key != None:
            Father = eng_key
            if r1 < eng_key.r1:
                eng_key = eng_key.Lson
            else:
                eng_key = eng_key.Rson
        node.Father = Father
        if Father == None:
            thiseng.root = node
        elif r1 < Father.r1:
            Father.Lson = node
        else:
            Father.Rson = node
        thiseng.Engine(node)


def hash(node):
    s = b""
    if node != None:
        s += bytes([node.r2 ^ random.randint(0, 0xFF)])
        s += hash(node.Lson)
        s += hash(node.Rson)
    return s

def whash(node):
    s = b""
    if node != None:
        s += bytes([random.randint(0, 0xFF)])
        s += whash(node.Lson)
        s += whash(node.Rson)
    return s

def chash(node):
    s = ''
    if node != None:
        s += chr(node.r2)
        s += chash(node.Lson)
        s += chash(node.Rson)
    return s

def mixin(eng):
    eng_key = eng.root
    Father = None
    while eng_key != None:
        Father = eng_key
        if random.randint(0, 1) == 0:
            eng_key = eng_key.Lson
        else:
            eng_key = eng_key.Rson
    eng.Engine(Father)


def adJGrTXOYD():
    eng = Engine()

    # player_input = input("Please enter the flag: ")
    player_input = 'flag{0123456789bchijkmnopqrstuvwxyz}'

    if len(player_input) != 36:
        print("Try again!")
        return
    if player_input[:5] != "flag{" or player_input[-1] != "}":
        print("Try again!")
        return

    for input_chr in player_input:
        eng.iterate(random.random(), ord(input_chr))

    for _ in range(0x100):
        mixin(eng)
    
    shuffled =  '_rltrYY{PYR_FU3OgoAL}@s_S_efaA7l_uEm'
    flag_base = 'flag{0123456789bchijkmnopqrstuvwxyz}'

    # plain = whash(eng.root)
    cresult = chash(eng.root)
    # result = hash(eng.root)


    eng_key = base64.b64decode("7EclRYPIOsDvLuYKDPLPZi0JbLYB9bQo8CZDlFvwBY07cs6I")
    
    # for i in range(len(eng_key)):
    #     print(chr(int(plain[i]) ^ int(eng_key[i])), end = '')

    print(cresult)

    
    for (i, c) in enumerate(flag_base):
        for (j, w) in enumerate(cresult):
            if(c == w):
                print(shuffled[j], end = '')
    # flag{YOU_ArE_7ru3lY_m@SteR_oF_sPLAY}

    # print(result)
    # print(eng_key)

    return

    if result == eng_key:
        print("You got the flag3!")
    else:
        print("Try again!")


if __name__ == "__main__":
    random.seed('flag2 = flag{wElc0me_tO_THe_w0RlD_OF_pYtHON}')
    if random.randint(0, 65535) == 54830:
        print('shell3 success')
        adJGrTXOYD()
