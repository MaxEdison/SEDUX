import sys


def string_to_binary(string):
    """Converts a string to binary representation."""
    return ' '.join(format(ord(char), '08b') for char in string)


def binary_to_int(binary):
    """Converts binary representation to integer."""
    return int(binary, 2)


def xor_bytes(byte1, byte2):
    """Performs XOR operation on two bytes."""
    return format(binary_to_int(byte1) ^ binary_to_int(byte2), '08b')


def encrypt(message, key):
    """Encrypts the message using the provided key."""
    key_binary = string_to_binary(key).split()
    key_len = len(key_binary)
    encrypted_message = []

    for i, char in enumerate(message):
        encrypted_byte = xor_bytes(string_to_binary(char), key_binary[i % key_len])
        encrypted_message.append(binary_to_int(encrypted_byte))

    return "%".join(map(str, encrypted_message))


def decrypt(message, key):
    """Decrypts the message using the provided key."""
    key_binary = string_to_binary(key).split()
    key_len = len(key_binary)
    decrypted_message = []

    for i, byte in enumerate(message.split("%")):
        decrypted_byte = xor_bytes(byte, key_binary[i % key_len])
        decrypted_message.append(chr(binary_to_int(decrypted_byte)))

    return "".join(decrypted_message)


if __name__ == "__main__":
    message = input("Enter Message: ")
    key = input("Enter Key: ")

    print("Encrypt(e) or Decrypt(d) message?")
    action = input()

    if action == 'e':
        print("Encrypted Message:")
        print(encrypt(message, key))
    elif action == 'd':
        print("Decrypted Message:")
        print(decrypt(message, key))
    else:
        print("Invalid input. Exiting...")
        sys.exit()