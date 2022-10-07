# def reverse_string(word):
#     reversed_word = ''
#
#     for letter in range(len(word) - 1, -1, -1):
#         reversed_word += word[letter]
#
#     return reversed_word


def reverse_string(word):
    reversed_word = ''

    for letter in word[::-1]:
        reversed_word += letter

    return reversed_word


def main():
    print(reverse_string("Codecademy"))
    print(reverse_string("Hello world!"))
    print(reverse_string(""))


if __name__ == '__main__':
    main()

