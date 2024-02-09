import sys


message = input("Enter Message: ")
key = input("Enter Key: ")

print("Encrypt(e) or Decrypt(d) message?")
getchar = lambda: sys.stdin.read(1)

match getchar():
    case 'e':
        pass