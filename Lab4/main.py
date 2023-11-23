
# Initial permutation (IP) table
initial_permutation = [58, 50, 42, 34, 26, 18, 10, 2,
                       60, 52, 44, 36, 28, 20, 12, 4,
                       62, 54, 46, 38, 30, 22, 14, 6,
                       64, 56, 48, 40, 32, 24, 16, 8,
                       57, 49, 41, 33, 25, 17, 9, 1,
                       59, 51, 43, 35, 27, 19, 11, 3,
                       61, 53, 45, 37, 29, 21, 13, 5,
                       63, 55, 47, 39, 31, 23, 15, 7]

# Permutation choice 1 (PC1) table
pc_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

# Left shift values for each round
shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# Permutation choice 2 (PC2) table
pc_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]


def split_key(key):
    round_key = 0
    permuted_key = []
    for shift in shift_schedule:
        # Split the 56-bit key into left and right halves
        left_half = key[:28]
        right_half = key[28:]

        # Perform circular left shift on both halves
        left_half = left_half[shift:] + left_half[:shift]
        right_half = right_half[shift:] + right_half[:shift]

        # Combine the halves and apply PC2 to get a 48-bit round key
        round_key = left_half + right_half
        pc2_result = []
        for i in range(48):
            pc2_result.append(round_key[pc_2[i] - 1])

        permuted_key.append(''.join(pc2_result))

        # Update the key for the next round
        key = left_half + right_half

    return permuted_key


def generate_key(key):
    key_binary = ''
    for c in key:
        key_binary += ''.join(format(ord(c), '08b'))

    pc1_result = []
    for i in range(56):
        pc1_result.append(key_binary[pc_1[i] - 1])

    return split_key(pc1_result)


def main():

    while True:
        key = input("Input key(8 characters) or press 'q' to quit: ")
        if key == "q":
            break
        if len(key) > 8 or len(key) < 8:
            print("Invalid key! Key should contain 8 characters.")
            continue

        permuted_key = generate_key(key)

        for i, round_key in enumerate(permuted_key):
            print(f"Round {i + 1} Key: {round_key}")


if __name__ == '__main__':
    main()
