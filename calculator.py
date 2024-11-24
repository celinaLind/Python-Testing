def add(x, y):
    return x + y

def main():
    print("Simple Calculator")
    print("----------------")

    while True:
        print("Enter an operation (+, -, *, /) or 'q' to quit:")
        op = input("> ")

        if op == 'q':
            break

        try:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))

            if op == '+':
                result = add(x, y)
            else:
                print("Invalid operation!")
                continue

            print(f"{x} {op} {y} = {result:.2f}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()