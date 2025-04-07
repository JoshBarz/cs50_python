def main():
    word = input("camelCase: ")
    snake_case(word)


def snake_case(word):
    new_word = []
    for letter in word:
        
        if letter.isupper():
            new_word.append("_")
            new_word.append(letter.lower())
        
        else:
            new_word.append(letter)

    new_word = ''.join(new_word)

    print(f"snake_case: {new_word}")


main()