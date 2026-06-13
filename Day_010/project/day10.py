def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    if n2 == 0:
        return "Error (Cannot divide by zero)"
    return n1 / n2


def calculate():
    # Fixed: Removed the accidental extra indentation here
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))

    # Fixed: Aligned this while loop with the inputs above
    while True:
        n3 = input("Enter the symbol to perform that operation (+, -, *, /): ")

        if n3 == '+':
            print("Result (Addition):", add(n1, n2))
            break
        elif n3 == '-':
            print("Result (Subtraction):", sub(n1, n2))
            break
        elif n3 == '*':
            print("Result (Multiplication):", mul(n1, n2))
            break
        elif n3 == '/':
            print("Result (Division):", div(n1, n2))
            break
        else:
            print("Invalid symbol. Please try again.")


while True:
    choice = input("Enter 'y' to perform a calculation or 'n' to exit: ").lower()

    if choice == 'y':
        calculate()
    elif choice == 'n':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 'y' or 'n'.")