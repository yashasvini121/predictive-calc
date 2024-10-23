import math

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square root")
    print("6. Natural logarithm")
    print("7. Exponential")
    print("8. Trigonometric functions (sin, cos, tan)")
    print("9. Inverse trigonometric functions (sin^-1, cos^-1, tan^-1)")

    choice = input("Enter the number of the operation you want to perform: ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", num1 + num2)

    elif choice == '2':
        print(num1, "-", num2, "=", num1 - num2)

    elif choice == '3':
        print(num1, "*", num2, "=", num1 * num2)

    elif choice == '4':
        if num2 != 0:
            print(num1, "/", num2, "=", num1 / num2)
        else:
            print("Error! Division by zero is not allowed.")

    elif choice == '5':
        if num1 >= 0:
            print("Square root of", num1, "=", math.sqrt(num1))
        else:
            print("Error! Negative number doesn't have a real square root.")

    elif choice == '6':
        if num1 > 0:
            print("Natural logarithm of", num1, "=", math.log(num1))
        else:
            print("Error! Logarithm of non-positive number is undefined.")

    elif choice == '7':
        print("Exponential of", num1, "=", math.exp(num1))

    elif choice == '8':
        print("Sine of", num1, "=", math.sin(num1))
        print("Cosine of", num1, "=", math.cos(num1))
        print("Tangent of", num1, "=", math.tan(num1))

    elif choice == '9':
        print("Inverse sine of", num1, "=", math.asin(num1))
        print("Inverse cosine of", num1, "=", math.acos(num1))
        print("Inverse tangent of", num1, "=", math.atan(num1))

    else:
        print("Invalid input")

calculator()
