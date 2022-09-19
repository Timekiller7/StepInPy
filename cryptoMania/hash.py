import hashlib

w = hashlib.sha224('SFedU_Championship2021'.encode()).hexdigest()
f = "Бутерин"

for i in range(10000, 1000000):
    wfx = str(w) + str(f) + str(i)
    hash_wfx = hashlib.sha3_224(wfx.encode()).hexdigest()
    hash_wfx_find = '13e656d84ccd2bed5446de7dda9741049f6086c465dd7e80b8271649'
    if hash_wfx == hash_wfx_find:
        print("пятизначное число", i)
        print("w = ", w)
        print("f = ", f)
