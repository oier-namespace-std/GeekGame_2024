import struct
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_audio_pkt(p):
    typ = int(p['_source']['layers']['rtp']['rtp.p_type'])
    seq = int(p['_source']['layers']['rtp']['rtp.seq'])
    if typ==127: return # fec
    assert typ==97
    
    b = bytes.fromhex(p['_source']['layers']['rtp']['rtp.payload'].replace(':', ''))
    iv = struct.pack('>i', int('?????????')+seq) + b'\x00'*12 # https://github.com/LizardByte/Sunshine/blob/190ea41b2ea04ff1ddfbe44ea4459424a87c7d39/src/stream.cpp#L1516
    cipher = AES.new(b'????????????????', AES.MODE_CBC, iv)
    
    return unpad(cipher.decrypt(b), 16)


seq = 0
def decrypt_audio_bytes(b):
    # print(b)
    global seq
    # key = 0x93002D2BAC9D0146
    # key = b'????????????????'
    key = b'aaaaaaaaaaaaaaaa'
    iv = struct.pack('>i', int('000000000')+seq) + b'\x00'*12 # https://github.com/LizardByte/Sunshine/blob/190ea41b2ea04ff1ddfbe44ea4459424a87c7d39/src/stream.cpp#L1516
    cipher = AES.new(key, AES.MODE_CBC, iv)
    res = cipher.decrypt(b)
    seq = seq + 1
    # print(res)
    return res
    # return unpad(res, 16)