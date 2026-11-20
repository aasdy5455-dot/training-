
import math


class ScientificCalculator:

    def __init__(self):
        self.history = []

    # چهار عمل اصلی
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed!")
        return a / b

    # توان و جذر
    def power(self, a, b):
        return a ** b

    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        return math.sqrt(a)

    # توابع مثلثاتی (ورودی بر حسب درجه)
    def sin(self, a):
        return math.sin(math.radians(a))

    def cos(self, a):
        return math.cos(math.radians(a))

    def tan(self, a):
        return math.tan(math.radians(a))

    # لگاریتم
    def log(self, a):
        if a <= 0:
            raise ValueError("Logarithm requires a positive number!")
        return math.log10(a)

    def ln(self, a):
        if a <= 0:
            raise ValueError("Ln requires a positive number!")
        return math.log(a)

    # فاکتوریل
    def factorial(self, a):
        if a < 0 or not isinstance(a, int):
            raise ValueError("Factorial requires a non-negative integer!")
        return math.factorial(a)

    # ذخیره تاریخچه
    def save_history(self, operation, result):
        self.history.append(f"{operation} = {result}")


class CalculatorApp:

    def __init__(self):
        self.calculator = ScientificCalculator()

    def run(self):

        print("===== SCIENTIFIC CALCULATOR =====")

        while True:

            print("""
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Power
6. Square Root
7. Sin
8. Cos
9. Tan
10. Log
11. Ln
12. Factorial
13. History
0. Exit
""")

            choice = input("Select an operation: ")

            if choice == "0":
                print("Goodbye!")
                break

            try:
                if choice == "13":
                    print("\nCalculation History:")
                    for item in self.calculator.history:
                        print(item)
                    continue

                if choice in ["6", "7", "8", "9", "10", "11", "12"]:
                    a = float(input("Enter a number: "))

                    operations = {
                        "6": ("Square Root", self.calculator.square_root),
                        "7": ("Sin", self.calculator.sin),
                        "8": ("Cos", self.calculator.cos),
                        "9": ("Tan", self.calculator.tan),
                        "10": ("Log", self.calculator.log),
                        "11": ("Ln", self.calculator.ln),
                        "12": ("Factorial", self.calculator.factorial)
                    }

                    name, function = operations[choice]
                    result = function(a)

                elif choice in ["1", "2", "3", "4", "5"]:

                    a = float(input("Enter first number: "))
                    b = float(input("Enter second number: "))

                    operations = {
                        "1": ("Addition", self.calculator.add),
                        "2": ("Subtraction", self.calculator.subtract),
                        "3": ("Multiplication", self.calculator.multiply),
                        "4": ("Division", self.calculator.divide),
                        "5": ("Power", self.calculator.power)
                    }

                    name, function = operations[choice]
                    result = function(a, b)

                else:
                    print("Invalid choice!")
                    continue

                print(f"\nResult: {result}")

                self.calculator.save_history(name, result)

            except ValueError as error:
                print(f"Error: {error}")

            except OverflowError:
                print("Error: Result is too large!")

            except Exception as error:
                print(f"Unexpected error: {error}")


# اجرای برنامه
if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
