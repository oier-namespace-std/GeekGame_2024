import random

read = []
write = []

def rw(argv):
    slot = 0
    index = 0
    option = 1
    while(True):
        slot = random.randint(0, 4)
        index = random.randint(0, 4)
        option = random.randint(1, 3)
        if(argv == 2):
            if(read[slot]):
                break
        else:
            if(write[slot]):
                break
    print(argv)
    print(slot)
    print(index)
    if(argv == 3):
        value = random.randint(0, 255)
        print(value)
    print(option)

def create():
    global read, write
    choice = random.randint(1, 3)
    size = 1024
    option = 1
    if(len(read) <= 2):
        option = random.randint(1, 3)
    read.append(option == 1 or option == 3)
    write.append(option == 2 or option == 3)
    if(choice == 1):
        size = min([random.randint(8,16) for _ in range(8)])
    print('1')
    print(choice)
    print(size)
    print(option)


for _ in range(32):
    create()


for _ in range(10240):
    argv = random.randint(1, 3)
    if(random.randint(0, 4096) != 0):
        argv = random.randint(2, 3)
    # print(argv)
    if(argv == 1):
        create()
    if(argv == 2 or argv == 3):
        rw(argv)


print('complete')