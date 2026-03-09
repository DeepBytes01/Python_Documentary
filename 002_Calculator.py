
def main():
    print("Calculator")
    try:
        x = float(input("Enter num1: "))
        y = float(input("Enter num2: "))
    except ValueError:
        print("Invalid input")
        return
    
    print("""
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    """)
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input")
        return

    operations = {
        1: add,
        2: sub,
        3: mul,
        4: div
    }
    
    if choice not in operations:
        print("Invalid choice")
        return
    try:
        result = operations[choice](x, y)
        print(result)
    except ZeroDivisionError as e:
        print(e)
    

def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

if __name__ == "__main__":            
    main()
