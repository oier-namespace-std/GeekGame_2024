s = 'IIIIIIIIllIllll.txt  IIlllIlIIIlllII.txt  IlllIIIIllllIlI.txt  lIllIlIlIIllIll.txt  lllIIIIIIIllllI.txt \
IIIIIIIlIIIlIlI.txt  IIllllIIIIllIII.txt  IlllIllIlIlIIll.txt  lIllIlIlllIIIll.txt  lllIIIlIIIIIllI.txt \
IIIIIIlIIllIIll.txt  IIllllIIIllIIlI.txt  IllllIlIllIIIlI.txt  lIllllIIlIllIlI.txt  lllIIIlIlllllII.txt \
IIIIlIllIlllIll.txt  IIlllllllIIIIII.txt  lIIIIIIlllIlIll.txt  lIlllllIllIIllI.txt  lllIIIlllIllIlI.txt \
IIIIllllIIIlIlI.txt  IIlllllllIIlIll.txt  lIIIIllllIIlIIl.txt  lIlllllllIlIIlI.txt  lllIIlIlllIlllI.txt \
IIIIlllllIIIIIl.txt  IlIIIIIlllIlIIl.txt  lIIIlIIIIIIIlII.txt  llIIIIIIllIlllI.txt  lllIlIIIlIlIlll.txt \
IIIlIIIIIllllIl.txt  IlIIIlllIlllIII.txt  lIIIllIIlllIIlI.txt  llIIIlllIIlIlll.txt  llllIlllllIllII.txt \
IIIllIIIIIIlIll.txt  IlIIllIIIlIllIl.txt  lIIIllIlIIllIII.txt  llIIlIlIllllIll.txt  lllllIIlllllllI.txt \
IIIllIIlllIIlll.txt  IlIlIIlllllllll.txt  lIIlIIIllIlIllI.txt  llIIlIllIIIIIll.txt  lllllIlIllllIll.txt \
IIlIIIIIIIlIIII.txt  IlIlIlIIlIIIIIl.txt  lIIlIIllIIIllll.txt  llIIlIllllIlIll.txt  llllllIIlIlIllI.txt \
IIlIIlIIlIlIlII.txt  IlIllIlIIlIIlll.txt  lIIlIlIIlIIIIII.txt  llIlIIlIIIIIlll.txt  llllllIlIIIlIII.txt \
IIlIIlIIlIlIllI.txt  IlIllIllIlIllll.txt  lIIlIlIIlIIllII.txt  llIlIIlllIIIIll.txt  llllllIllIllIII.txt \
IIlIlIIlllllllI.txt  IlIllllIIllIIII.txt  lIIlIllIIIllIll.txt  llIlIllIlIIIllI.txt  llllllllllllIlI.txt \
IIlIllIIIlIIlIl.txt  IlIlllllIlIlIIl.txt  lIIllIIllIIIIIl.txt  llIllIIlIlIlIII.txt \
IIlIllIIllIIIIl.txt  IllIIIIllIIIlll.txt  lIlIlIIIIllllII.txt  llIlllIIlllIIII.txt \
IIlIllIlIllIIII.txt  IllIIIllIlllIlI.txt  lIlIllIlIlIIlll.txt  llIlllIllllIIll.txt \
IIllIlIllIIIlll.txt  IllIIllllllIIll.txt  lIllIlIIIIIlIII.txt  llIlllIllllIlIl.txt'

import os

for z in s.split(' '):
    if(z != ''):
        fd = os.open(z, os.O_RDWR)
        ret = os.read(fd,512)
        print (ret)
