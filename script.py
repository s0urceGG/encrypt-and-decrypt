
abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.()-!? '
cba = 'lazmxsnkcdjvfbhgpoqwierutyQPWOALSKDEJIFRHUGTYZMXNCVB,.()-!? '
txt = []
txt2 = []

def main():
    print('What do you want to do?')
    print('[0] Encrypt')
    print('[1] Decrypt')
    print('[2] Exit')
    res = int(input())
    if res == 2:
        exit
    else:
        if res == 0:
            txt = input('Enter text to encrypt: ')
            for i in range(0, len(txt)):
                for j in range(0, len(abc)):
                    if txt[i] == abc[j]:
                        txt2.append(cba[j])
                    else:
                        continue
            print(''.join(txt2))
        else:
            if res == 1:
                txt = input('Enter text to decrypt: ')
                for i in range(0, len(txt)):
                    for j in range(0, len(cba)):
                        if txt[i] == cba[j]:
                            txt2.append(abc[j])
                        else:
                            continue
            print(''.join(txt2))
main()