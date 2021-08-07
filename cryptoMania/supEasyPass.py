from simplecrypt import decrypt
passwords=open('passwords.txt')
bin= open('encrypted.bin', 'rb')    # opening a binary file
encrypted = bin.read()
for i in passwords:
    s=i.strip()                    #обкусываем старт и конец строк у паролей из txt файла
    try:
        x= decrypt(s, encrypted)
        print(x.decode('utf-8'))
        break
    except:
        continue