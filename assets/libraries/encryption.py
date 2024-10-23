letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=_+!@#$%^&*()}{":;/.,?><~`[]'

def encryption(input):
    password = ''
    for i in input:
        if i == ' ':
            password += '/'
            password += '$'
        else:
            code = letters.index(i)
            if code > 9:
                password += str(code)
                password += '$'
            else:
                password += '0'
                password += str(code)
                password += '$'

    return password

def decryption(input):
    password = ''
    word = input.split('$')
    for i in word:
        if i != '':
            if i == '/':
                password += ' '
            else:
                letter = letters[int(i)]
                password += letter
    return(password)
