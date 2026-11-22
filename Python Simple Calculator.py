# 1. Mathematical Operations

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


# 2. Calculation History
calculation_history = []


# 3. Main Program
while True:
    try:
        operation = input(
            "Choose operation (+, -, *, /) or type 'exit' to quit: "
        )

        if operation == "exit":
            print("Good bye!")
            break

        if operation not in ["+", "-", "*", "/"]:
            print("Invalid operation!")
            continue

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform calculation
        if operation == "+":
            result = add(num1, num2)

        elif operation == "-":
            result = sub(num1, num2)

        elif operation == "*":
            result = mul(num1, num2)

        elif operation == "/":
            if num2 == 0:
                print("Cannot divide by zero!")
                continue
            else:
                result = div(num1, num2)

        # Store calculation
        calculation = {
            "num1": num1,
            "operation": operation,
            "num2": num2,
            "result": result
        }

        calculation_history.append(calculation)

        # Display result
        print(f"Result: {result}")

    except ValueError:
        print("Please enter numbers only!")
