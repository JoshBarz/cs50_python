def main():
    word = input("camelCase: ")
    snake_case(word)


def snake_case(word):
    for letter in word:
        if letter.isupper():
            x = "_" + letter.lower()
            word = word.replace(letter, x)
                    

    print(f"snake_case: {word}")


main()