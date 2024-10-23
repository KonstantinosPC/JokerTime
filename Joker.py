from random import randint
from getpass import getpass
from assets.libraries.encryption import *

base = True
line = '+-------------------+'
empty = '\n'
while base:

    neworold = input('You are old or new user U/N: ')

    if neworold.upper() == 'N':
        usernameI = input('Set your username: ')
        passwordI = getpass('Set your Password: ')
        confpassword = getpass('Confirm your password: ')

        if passwordI != confpassword:
            print('Sorry but something went wrong try again later! ')
        else:
            readfile = open('./assets/files/users.txt','r').read()
            Userenc = encryption(str(usernameI))
            Passenc = encryption(str(passwordI))
            Moneyenc = encryption('20000')
            try:
                open('./assets/files/users.txt', 'w').write(Userenc + ',' + Passenc + ',' + Moneyenc + '\n')
                print('Done!')
            except:
                print('Error')


    elif neworold.upper() == 'U':
        username = getpass('Please insert your Username: ')
        password = getpass('Please insert your password: ')

        for i in open('./assets/files/users.txt', 'r'):
            cutted = (i.strip()).split(',')
            if (decryption(cutted[0]) == username) and (decryption(cutted[1]) == password):
                print('You successfully logged in')
                print(line + '\nWelcome ' + decryption(cutted[0]) + '\nMoney: ' + decryption(cutted[2]) + empty + line)
                difficulty = int(input('Set your difficulty (<=10):'))
                while base:
                    if difficulty >= 10:
                        set = input('Set your number (0-'+ str(difficulty) +') and your money(Number,Money): ')
                        if set == 'stop':
                            base = False
                        else:
                            setter = set.split(',')
                            setmoney = setter[1]
                            setnumber = setter[0]
                            if int(setmoney) > int(decryption(cutted[2])):
                                print('Hey bro you cant do that!')
                            else:
                                random1 = randint(0,difficulty)
                                random2 = randint(0,difficulty)
                                random3 = randint(0,difficulty)
                                random4 = randint(0,difficulty)
                                random5 = randint(0,difficulty)

                                print(str(random1) + empty + str(random2) + empty + str(random3) + empty + str(random4) + empty + str(random5) + empty + 'Yours: ' + str(setnumber) + empty + line)
                                if (int(setnumber) == random1) or (int(setnumber) == random2) or (int(setnumber) == random3) or (int(setnumber) == random4) or (int(setnumber) == random5):
                                    print('Congratulation you won!')
                                    s = ''
                                    filewin = open('./assets/files/users.txt','r')
                                    for i in filewin:
                                        splitted = i.split(',')
                                        if decryption(splitted[0]) == username:
                                            filemoney = decryption(splitted[2].strip())
                                            finalmoney = int(filemoney) + 2*(int(setmoney))
                                            print('Your money: ' + str(finalmoney))
                                            final = (splitted[0]) + ',' + (splitted[1]) + ',' + str(encryption(str(finalmoney)))
                                            s += (final + '\n')
                                        else:
                                            s += i
                                    filewin.close()
                                    filer = open('./assets/files/users.txt', 'w')
                                    filer.write(s)
                                    filer.close()

                                else:
                                    print('Sorry bro you lost!')
                                    b = ''
                                    filelost = open('./assets/files/users.txt','r')
                                    for i in filelost:
                                        splitted = i.split(',')
                                        
                                        if decryption(splitted[0]) == username:
                                            filemoney = decryption(splitted[2].strip())
                                            finalmoney = int(filemoney) - (int(setmoney))
                                            print('Your money: ' + str(finalmoney))
                                            final = (splitted[0]) + ',' + (splitted[1]) + ',' + str(encryption(str(finalmoney)))
                                            b += (final + '\n')
                                        else:
                                            b += i
                                    filer = open('./assets/files/users.txt', 'w')
                                    filer.write(b)
                                    filer.close()
                                    filelost.close()
                    else:
                        print('Sorry bro I caught you. You can put less than 10!')
                    

                    
    elif neworold.upper() == 'STOP':
        base = False
    else:
        print('Sorry something went wrong try again later!')