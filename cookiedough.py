def multiply():
    while True:
        x = input("Enter 1st Number: ")
        try:
            x = int(x)
            break
        except:
            print("Please enter an integer value.")
            continue

    while True:
        y = input("Enter 2nd Number: ")
        try:
            y = int(y)
            break
        except:
            print("Please enter an integer value.")
            continue

    print(f"{x} * {y} = {x * y}")


def divide():
    while True:
        x = input("Enter 1st Number: ")
        try:
            x = int(x)
            break
        except:
            print("Please enter an integer value.")
            continue

    while True:
        y = input("Enter 2nd Number: ")
        try:
            y = int(y)
            break
        except:
            print("Please enter an integer value.")
            continue

    print(f"{x} / {y} = {x / y}")


def add():
    while True:
        x = input("Enter 1st Number: ")
        try:
            x = int(x)
            break
        except:
            print("Please enter an integer value.")
            continue

    while True:
        y = input("Enter 2nd Number: ")
        try:
            y = int(y)
            break
        except:
            print("Please enter an integer value.")
            continue

    print(f"{x} + {y} = {x + y}")


def subtract():
    while True:
        x = input("Enter 1st Number: ")
        try:
            x = int(x)
            break
        except:
            print("Please enter an integer value.")
            continue

    while True:
        y = input("Enter 2nd Number: ")
        try:
            y = int(y)
            break
        except:
            print("Please enter an integer value.")
            continue

    print(f"{x} - {y} = {x - y}")


def main():
    while True:
        while True:
            x = input("Enter 1 to add, Enter 2 to subtract, Enter 3 to multiply, Enter 4 to divide, Enter 0 to quit: ")

            try:
                x = int(x)
            except:
                print("Please enter 1, 2, 3 or 4.")
                continue

            if x < 0:
                print("Please enter 1, 2, 3 or 4.")
            elif x > 4:
                print("Please enter 1, 2, 3 or 4.")
            else:
                break

        if x == 0:
            print("Goodbye!")
            quit()
        elif x == 1:
            add()
        elif x == 2:
            subtract()
        elif x == 3:
            multiply()
        elif x == 4:
            divide()


main()