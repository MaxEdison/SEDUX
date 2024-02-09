import sys

def str2bin(string):

    binary = []
    
    for char in string:
        binary.append(format(ord(char), '08b'))
    return ' '.join(binary)

def bin2int(binary):
    return int(binary, 2)

def XOR(msgByte, keyByte):
    
    if len(msgByte) != 8 or len(keyByte) != 8 or not all(bit in '01' for bit in msgByte) or not all(bit in '01' for bit in keyByte):
        print("System ERROR [ERR CODE : 9]")
        return 9

    value1 = int(msgByte, 2)
    value2 = int(keyByte, 2)

    result = value1 ^ value2
    binary = format(result, '08b')
    return binary


def Encript(message, key):

    print("Encrypted Message: ")
    j = 0

    for i in range(0, len(message)):
        if j == len(key):
            j = 0
        
        print(bin2int(XOR(str2bin(message).split()[i], str2bin(key).split()[j])), end = "%")
        j += 1

    print("\n")

def Decrypt(message, key):
    
    message = message.split("%")
    if '' in message:
        message.remove('')
    message = list(map(lambda x : format(int(x), '08b'), message))

    print("Decrypted Message: ")

    j = 0
    for i in range(0, len(message)):
        if j == len(key):
            j = 0

        print(chr(bin2int(XOR(message[i], str2bin(key).split()[j]))), end = "")
        j += 1




message = input("Enter Message: ")
key = input("Enter Key: ")

print("Encrypt(e) or Decrypt(d) message?")
getchar = lambda: sys.stdin.read(1)

match getchar():
    case 'e':
        Encript(message, key)
    case 'd':
        Decrypt(message, key)
    case _:
        print("Invalid input. Exiting...")
        exit()