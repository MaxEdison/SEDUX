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
    result_binary = format(result, '08b')
    return result_binary


message = input("Enter Message: ")
key = input("Enter Key: ")

print("Encrypt(e) or Decrypt(d) message?")
getchar = lambda: sys.stdin.read(1)

match getchar():
    case 'e':
        pass