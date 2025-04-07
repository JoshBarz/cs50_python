def calculator():
    exp = input("Expression: ")

    x, y, z = exp.split(" ")

    if y == "+":
      print(float(int(x) + int(z)))

    if y =="-":
       print(float(int(x) - int(z)))

    if y =="/":
       print(float(int(x) / int(z)))

    if y =="*":
       print(float(int(x) * int(z)))


calculator()  