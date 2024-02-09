import sys

def str2bin(string):

    binary = []
    
    for char in string:
        binary.append(format(ord(char), '08b'))
    return ' '.join(binary)


message = input("Enter Message: ")
key = input("Enter Key: ")

print("Encrypt(e) or Decrypt(d) message?")
getchar = lambda: sys.stdin.read(1)

match getchar():
    case 'e':
        pass