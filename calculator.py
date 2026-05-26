# A working calculator app
def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    
    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
            
            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                result = num1 / num2
            else:
                print("Invalid operation")
                continue
                
            print(f"Result: {result}")
            
            again = input("Calculate again? (y/n): ")
            if again.lower() != 'y':
                break
                
        except ValueError:
            print("Invalid input! Please enter numbers.")
        except ZeroDivisionError:
            print("Cannot divide by zero!")

if __name__ == "__main__":
    calculator()