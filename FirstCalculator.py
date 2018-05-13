while True:
    print("Welcome to my calculator. Input two numbers, and then type, d, m, s, or a to divide, multiple, etc...")

    num1 = input()
    num2 = input()
    sign = input()

    if str(sign) == "d":
        print(float(num1) / float(num2))
    elif str(sign) == "m":
        print(float(num1) * float(num2))
    elif str(sign) == "s":
        print(float(num1) - float(num2))
    elif str(sign) == "a":
        print(float(num1) + float(num2))
    else:
        print("Sorry, I don't understand")
    
