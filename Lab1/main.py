letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def generate_alphabet(key):
    alphabet = ""
    key = key.upper()
    for i in key:
        if i in alphabet:
            continue
        else:
            alphabet += i

    for i in letters:
        if i in alphabet:
            continue
        else:
            alphabet += i
    return alphabet.upper()


def eliminate_spaces(source):
    result = ""
    for i in source:
        if i == "":
            continue
        else:
            result = result + i
    return result


def valid_string(source):
    for i in source:
        if i.isalpha():
            return source
        else:
            raise Exception("Invalid format")


def encrypt(source, key, letters_en):
    encrypted = ""
    for i in source:
        char_en = letters_en[(letters_en.index(i.upper()) + key) % 26]
        encrypted = encrypted + char_en
    return encrypted


def decrypt(encryption, key, letters_dec):
    decrypted = ""

    for i in encryption:
        char_en = letters_dec[(letters_dec.index(i.upper()) - key) % 26]
        decrypted = decrypted + char_en
    return decrypted


def main():
    while True:
        print("\n1. Encrypt with numerical key"
              "\n2. Decrypt with numerical key"
              "\n3. Encrypt with key word"
              "\n4. Decrypt with key word"
              "\n5. Exit")
        choice = int(input("Chose service: "))
        match choice:
            case 1:
                message = input("Input the message: ")
                key = int(input("Input the key: "))
                if valid_string(eliminate_spaces(message)):
                    print("Encrypted message " + encrypt(message, key, letters))
            case 2:
                encoded = input("Input the encoded message: ")
                key = int(input("Input the key: "))
                if valid_string(eliminate_spaces(encoded)):
                    print("Decrypted message: " + decrypt(encoded, key, letters))
            case 3:
                message_word = input("Input the message: ")
                while True:
                    key_word = input("Input the key word: ")
                    if len(key_word) >= 7:
                        break
                    else:
                        print("Invalid key word")
                key = int(input("Input the numerical key: "))

                if valid_string(eliminate_spaces(message_word)):
                    print("Encrypted message with key word: " + encrypt(message_word, key, generate_alphabet(key_word)))
                    print(generate_alphabet(key_word))
            case 4:
                to_decrypt = input("Input the encoded message: ")
                while True:
                    key_word = input("Input the key word: ")
                    if len(key_word) >= 7:
                        break
                    else:
                        print("Invalid key word")
                key = int(input("Input the numerical key: "))
                if valid_string(eliminate_spaces(to_decrypt)):
                    print("Decrypted message with key word: " + decrypt(to_decrypt, key, generate_alphabet(key_word)))
                    print(generate_alphabet(key_word))


            case 5:
                print("Exiting the program")
                break


if __name__ == "__main__":
    main()
