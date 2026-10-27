
def add(x, y):
    return x + yA


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y


def calculator():
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    while True:
        choice = input("\nEnter choice (1/2/3/4) or 'q' to quit: ").strip()

        if choice.lower() == 'q':
            print("Exiting calculator.")
            break

        if choice not in ('1', '2', '3', '4'):
            print("Invalid input. Please enter 1, 2, 3, or 4.")
            continue

        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number. Please try again.")
            continue

        if choice == '1':
            print("Result:", add(x, y))
        elif choice == '2':
            print("Result:", subtract(x, y))
        elif choice == '3':
            print("Result:", multiply(x, y))
        elif choice == '4':
            print("Result:", divide(x, y))


if __name__ == "__main__":
    calculator()
