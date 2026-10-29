import importlib
import math
import os
import random
import string
import sys
import time
import uuid
from datetime import datetime

LINE = "=" * 26


def create_file(name):
    open(name, "w").close()
    return "File created successfully!"


def write_file(name, data):
    with open(name, "w") as file:
        file.write(data)
    return "Data written successfully!"


def read_file(name):
    if not os.path.exists(name):
        return "File not found."
    with open(name) as file:
        return file.read()


def append_file(name, data):
    with open(name, "a") as file:
        file.write(data + "\n")
    return "Data appended successfully!"


def compound_interest(principal, rate, years):
    total = principal * (1 + rate / 100) ** years
    return round(total, 2), round(total - principal, 2)


def trigonometry(angle):
    radians = math.radians(angle)
    return {"sin": round(math.sin(radians), 4),
            "cos": round(math.cos(radians), 4),
            "tan": round(math.tan(radians), 4)}


def area(shape, a, b=0):
    if shape == "circle":
        return round(math.pi * a ** 2, 2)
    if shape == "rectangle":
        return round(a * b, 2)
    return round(0.5 * a * b, 2)


def convert(kind, value):
    if kind == "km_to_miles":
        return round(value * 0.621371, 2)
    return round(value * 9 / 5 + 32, 2)


def show_menu(title, options):
    print(LINE)
    print(title)
    for number, text in enumerate(options, 1):
        print(f"{number}. {text}")
    return input("Enter your choice: ").strip()


def ask_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid number.")


def log(text):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    append_file("toolkit_log.txt", f"[{now}] {text}")


def datetime_menu():
    options = ["Display current date and time",
               "Calculate difference between two dates",
               "Format date into custom format", "Stopwatch",
               "Countdown Timer", "Back to Main Menu"]
    while True:
        choice = show_menu("Datetime and Time Operations:", options)
        if choice == "1":
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("Current Date and Time:", now)
            log("Viewed current time: " + now)
        elif choice == "2":
            try:
                first = datetime.strptime(input("Enter the first date (YYYY-MM-DD): "), "%Y-%m-%d")
                second = datetime.strptime(input("Enter the second date (YYYY-MM-DD): "), "%Y-%m-%d")
                print(f"Difference: {abs((second - first).days)} days")
            except ValueError:
                print("Wrong format. Please use YYYY-MM-DD.")
        elif choice == "3":
            pattern = input("Enter a format (example: %d-%m-%Y %I:%M %p): ")
            print("Formatted:", datetime.now().strftime(pattern))
        elif choice == "4":
            input("Press Enter to START...")
            start = time.time()
            input("Press Enter to STOP...")
            seconds = round(time.time() - start, 2)
            print(f"Elapsed time: {seconds} seconds")
            log(f"Stopwatch: {seconds} seconds")
        elif choice == "5":
            for left in range(int(ask_number("Enter seconds: ")), 0, -1):
                print(left)
                time.sleep(1)
            print("Time is up!")
        elif choice == "6":
            break
        else:
            print("Invalid choice, please try again.")


def math_menu():
    options = ["Calculate Factorial", "Solve Compound Interest",
               "Trigonometric Calculations", "Area of Geometric Shapes",
               "Unit Conversions", "Back to Main Menu"]
    while True:
        choice = show_menu("Mathematical Operations:", options)
        if choice == "1":
            number = int(ask_number("Enter a number: "))
            print("Factorial:", math.factorial(number) if number >= 0 else "needs 0 or more")
        elif choice == "2":
            principal = ask_number("Enter principal amount: ")
            rate = ask_number("Enter rate of interest (in %): ")
            years = ask_number("Enter time (in years): ")
            total, interest = compound_interest(principal, rate, years)
            print(f"Final Amount: {total:.2f}")
            print(f"Compound Interest: {interest:.2f}")
            log(f"Compound interest calculated: {interest:.2f}")
        elif choice == "3":
            angle = ask_number("Enter an angle in degrees: ")
            for name, value in trigonometry(angle).items():
                print(f"{name}({angle}) = {value}")
        elif choice == "4":
            shape = input("Shape (circle / rectangle / triangle): ").strip().lower()
            if shape == "circle":
                print("Area:", area(shape, ask_number("Radius: ")))
            elif shape in ("rectangle", "triangle"):
                first = ask_number("Length (or base): ")
                second = ask_number("Width (or height): ")
                print("Area:", area(shape, first, second))
            else:
                print("Unknown shape.")
        elif choice == "5":
            kind = input("1. KM to Miles  2. Celsius to Fahrenheit: ").strip()
            value = ask_number("Enter the value: ")
            if kind == "1":
                print("Miles:", convert("km_to_miles", value))
            else:
                print("Fahrenheit:", convert("c_to_f", value))
        elif choice == "6":
            break
        else:
            print("Invalid choice, please try again.")


def random_menu():
    options = ["Generate Random Number", "Generate Random List",
               "Create Random Password", "Generate Random OTP",
               "Random Sampling from a Dataset", "Back to Main Menu"]
    while True:
        choice = show_menu("Random Data Generation:", options)
        if choice == "1":
            low = int(ask_number("Enter the smallest number: "))
            high = int(ask_number("Enter the largest number: "))
            print("Random Number:", random.randint(min(low, high), max(low, high)))
        elif choice == "2":
            count = int(ask_number("How many numbers? "))
            print("Random List:", [random.randint(1, 100) for _ in range(count)])
        elif choice == "3":
            length = int(ask_number("Enter password length: "))
            letters = string.ascii_letters + string.digits + "@#$!&"
            print("Generated Password:", "".join(random.choice(letters) for _ in range(length)))
            log("Password generated")
        elif choice == "4":
            print("Your OTP:", "".join(random.choice(string.digits) for _ in range(6)))
        elif choice == "5":
            items = [i.strip() for i in input("Enter items separated by commas: ").split(",") if i.strip()]
            size = int(ask_number("How many items to pick? "))
            if 0 < size <= len(items):
                print("Sample:", random.sample(items, size))
            else:
                print("Please pick between 1 and", len(items), "items.")
        elif choice == "6":
            break
        else:
            print("Invalid choice, please try again.")


def uuid_menu():
    options = ["Generate a UUID (UUID4)", "Generate an Invoice ID",
               "Back to Main Menu"]
    while True:
        choice = show_menu("Generate Unique Identifiers:", options)
        if choice == "1":
            print("Generated UUID:", uuid.uuid4())
        elif choice == "2":
            invoice_id = "INV-" + uuid.uuid4().hex[:8].upper()
            print("Invoice ID:", invoice_id)
            log("Invoice ID created: " + invoice_id)
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")


def file_menu():
    options = ["Create a new file", "Write to a file", "Read from a file",
               "Append to a file", "Back to Main Menu"]
    while True:
        choice = show_menu("File Operations:", options)
        if choice == "5":
            break
        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice, please try again.")
            continue
        name = input("Enter file name: ").strip()
        if choice == "1":
            print(create_file(name))
        elif choice == "2":
            print(write_file(name, input("Enter data to write: ")))
        elif choice == "3":
            print("File Content:\n" + read_file(name))
        else:
            print(append_file(name, input("Enter data to append: ")))


def explore_menu():
    print(LINE)
    name = input("Enter module name (e.g. math, random, or 'toolkit' for this file): ").strip()
    try:
        module = sys.modules[__name__] if name == "toolkit" else importlib.import_module(name)
    except ImportError:
        print("Sorry, that module could not be found.")
        return
    print(f"Available Attributes in {name} module:")
    print([item for item in dir(module) if not item.startswith("_")])


def main():
    options = ["Datetime and Time Operations", "Mathematical Operations",
               "Random Data Generation", "Generate Unique Identifiers (UUID)",
               "File Operations (Custom Module)",
               "Explore Module Attributes (dir())", "Exit"]
    actions = {"1": datetime_menu, "2": math_menu, "3": random_menu,
               "4": uuid_menu, "5": file_menu, "6": explore_menu}
    print(LINE)
    print("Welcome to Multi-Utility Toolkit")
    while True:
        choice = show_menu("Choose an option:", options)
        if choice == "7":
            print(LINE)
            print("Thank you for using the Multi-Utility Toolkit!")
            print(LINE)
            break
        if choice in actions:
            actions[choice]()
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()