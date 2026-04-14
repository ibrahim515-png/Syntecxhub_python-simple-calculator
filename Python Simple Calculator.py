def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b


while True:
    try:
        operation = input("Choose operation (+, -, *, /) or type 'exit' to quit: ")

        if operation == "exit":
            print("Good bye")
            break

        if operation not in ["+", "-", "*", "/"]:
            print("Invalid operation")
            continue   # 👈 يرجع لأول اللوب

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == "+":
            print(add(num1, num2))

        elif operation == "-":
            print(sub(num1, num2))

        elif operation == "*":
            print(mul(num1, num2))

        elif operation == "/":
            if num2 == 0:
                print("Cannot divide by zero!")
            else:
                print(div(num1, num2))

    except ValueError:
        print("Please enter numbers only!")

























