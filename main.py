def encode_number(number):
    return hex(number)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero!"


def calculator():
    print("Base 10 Calculator")
    print("Type 'exit' to quit")

    while True:
        expression = input("Enter an expression (e.g., 2 + 3, 5 * 6, etc.): ")

        if expression.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            # Split the expression into operands and operator
            operands, operator = expression.split()
            a = float(operands)
            b = float(operator)

            if operator == '+':
                result = add(a, b)
            elif operator == '-':
                result = subtract(a, b)
            elif operator == '*':
                result = multiply(a, b)
            elif operator == '/':
                result = divide(a, b)
            else:
                result = "Error: Invalid operator!"

            encoded_result = encode_number(result)
            print("Encoded Result:", encoded_result)

        except ValueError:
            print("Error: Invalid input format.")


if __name__ == "__main__":
    calculator()
