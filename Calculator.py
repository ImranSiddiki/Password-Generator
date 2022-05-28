while True:
    print("""
    Choices are :
    1. Enter +, -, *, / For Addition, Subtraction, Multiplication & Division Respectively  
    2. Enter ** For First Number "Raised To The Power Of" Second Number
    3. Enter % For "Remainder" When First Number Is Divided By Second Number
    4. Enter // For "Quotient" When First Number Is Divided By Second Number
    5. Enter 1 For "Exit"
    """)

    operator = input("Select an operator : ")

    operations = ["+", "-", "*", "/", "**", "%", "//"]
        
    if operator in operations:
        pass
    elif operator == "1":
        break
    else:
        print("Invalid Operator, please select a correct operator.")
        continue

    first_number = float(input("Enter First Number : "))
    second_number = float(input("Enter Second Number : "))

    if operator == "+":
        print("The result is :", first_number + second_number)
    elif operator == "-":
        print("The result is : ", first_number - second_number)
    elif operator == "*":
        print("The result is : ", first_number * second_number)
    elif operator == "/":
        if second_number == 0:
            print("Invalid Input, you cannot divide with zero.")
        else:
            print("The result is : ", first_number / second_number)
    elif operator == "**":
        print("The result is : ", first_number ** second_number)
    elif operator == "%":
        print("The result is : ", first_number % second_number)
    elif operator == "//":
        print("The result is : ", first_number // second_number)