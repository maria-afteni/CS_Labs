alphabet = list("AĂÂBCDEFGHIÎKLMNOPQRSŞTȚUVWXYZ")


def create_matrix(key):
    matrix = []

    for char in key:
        if char not in matrix:
            matrix.append(char)

    for char in alphabet:
        if char not in matrix:
            matrix.append(char)

    return [matrix[i:i + 6] for i in range(0, 36, 6)]


def find_position(matrix, char):
    for x in range(6):
        for y in range(6):
            if matrix[x][y] == char:
                return x, y
    return


def reform_source(source):
    source = source.upper().replace(' ', '')
    if len(source) % 2 == 1:
        source += 'X'

    i = 0
    reformed_source = ''

    while i < len(source) - 1:
        if source[i] == source[i + 1]:
            reformed_source += source[i] + 'X'
            i += 1

        else:
            reformed_source += source[i] + source[i + 1]
            i += 2

    return reformed_source


def encrypt(matrix, source):
    encrypted_text = ""
    i = 0
    while i < len(source):
        x1, y1 = find_position(matrix, source[i])
        x2, y2 = find_position(matrix, source[i + 1])

        if x1 == x2:  # Same row
            encrypted_text += matrix[x1][(y1 + 1) % 6] + matrix[x2][(y2 + 1) % 6]

        elif y1 == y2:  # Same column
            encrypted_text += matrix[(x1 + 1) % 6][y1] + matrix[(x2 + 1) % 6][y2]

        else:
            encrypted_text += matrix[x1][y2] + matrix[x2][y1]

        i += 2

    return encrypted_text


def decrypt(matrix, source):
    decrypted_text = ""

    i = 0
    while i < len(source):
        x1, y1 = find_position(matrix, source[i])
        x2, y2 = find_position(matrix, source[i + 1])

        if x1 == x2:
            decrypted_text += matrix[x1][(y1 - 1) % 6] + matrix[x2][(y2 - 1) % 6]

        elif y1 == y2:
            decrypted_text += matrix[(x1 - 1) % 6][y1] + matrix[(x2 - 1) % 6][y2]
        else:
            decrypted_text += matrix[x1][y2] + matrix[x2][y1]

        if decrypted_text[-1] == "X":
            decrypted_text = decrypted_text[:-1]

        i += 2

    return decrypted_text


def validate_key(key):
    if len(key) < 7:
        print("!!! Key is too short. Enter a new key with at least 7 characters.")
        return False
    for ch in key:
        ch = ch.upper()
        if ch not in alphabet:
            print("!!! Unknown characters. Key must contain only Romanian letters.")
            return False
    return True


def validate_source(source):
    for ch in source:
        ch = ch.upper()
        if ch not in alphabet:
            print("!!! Unknown characters. The source must contain only Romanian letters.")
            return False
    return True


def get_key():
    key = input("Enter the key(at least 7 characters):\n")
    if not validate_key(key):
        get_key()
    else:
        key = key.upper().replace(' ', '')

    return key


def get_source():
    source = input("Enter the source text(plaintext or cypher):\n")
    source = source.upper().replace("J", "I")
    if not validate_source(reform_source(source)):
        get_source()

    return source


def print_matrix(matrix):
    print("Playfair Matrix:")
    for row in matrix:
        print(" ".join(row))
    print()


def main():
    option = int(input("Choose operation: \n1. Encrypt \n2. Decrypt \n"))

    match option:
        case 1:
            key = get_key()

            source = get_source()
            matrix = create_matrix(key)
            reformed_source = reform_source(source)
            print_matrix(matrix)
            print("Encrypted text:\n", encrypt(matrix, reformed_source))

        case 2:
            key = get_key()
            source = get_source()
            matrix = create_matrix(key)
            reformed_source = reform_source(source)
            print_matrix(matrix)
            print("Decrypted text:\n", decrypt(matrix, reformed_source))


if __name__ == "__main__":
    main()
