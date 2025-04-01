def main():
    phrase = input("Write a sentence with an emoticon in it ")
    convert(phrase)

def convert(emoji):
    emoji = emoji.replace(":)", "😀")
    emoji = emoji.replace(":(", "🙁")
    print (emoji)

main()