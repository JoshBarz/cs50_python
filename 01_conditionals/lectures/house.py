names = input("What is your name?")

match names:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor") 
    case "Draco":
        print("Slytherin")
    case _:
        print ("Who?")