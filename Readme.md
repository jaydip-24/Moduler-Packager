# Multi-Utility Toolkit

## Project Name

Moduler & Packager - Multi-Utility Toolkit

## Project Type

Python Console Program using Standard Modules, Custom Functions and a Menu-Driven Interface

## Project Folder

Create a folder for the project, for example:

`D:\RND Assignments\Multi_Utility_Toolkit\`

Main Python file:

`multi_utility_toolkit.py`

## About the Project

Multi-Utility Toolkit is a Python console program that puts many small tools
in one place. A small business owner can check dates, calculate interest,
create passwords for the team, make unique invoice numbers, and save notes to
text files, all from one simple menu.

The program uses several built-in Python modules (`datetime`, `time`, `math`,
`random`, `string`, `uuid`, `os`, `importlib`). The file operations and the
math utilities are written as separate reusable functions. Important actions
are saved automatically to a log file named `toolkit_log.txt`.

## Features

The main menu provides the following options:

1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit

### Sub-menus

| Main option | Sub-menu options |
|-------------|------------------|
| 1. Datetime and Time | Current date and time, difference between two dates, custom date format, stopwatch, countdown timer |
| 2. Mathematical Operations | Factorial, compound interest, trigonometry, area of shapes, unit conversions |
| 3. Random Data Generation | Random number, random list, random password, random OTP, random sampling |
| 4. Unique Identifiers | UUID4, invoice ID |
| 5. File Operations | Create, write, read, append |

## Function Design

### File operations (custom module section)

| Function | What it does |
|----------|--------------|
| `create_file(name)` | Creates a new empty file |
| `write_file(name, data)` | Writes data into a file (mode `w`) |
| `read_file(name)` | Reads and returns the file content, or a message if the file is missing |
| `append_file(name, data)` | Adds data at the end of a file (mode `a`) |

### Math utilities (custom module section)

| Function | What it does |
|----------|--------------|
| `compound_interest(principal, rate, years)` | Returns the final amount and the interest |
| `trigonometry(angle)` | Returns sin, cos and tan of an angle in degrees |
| `area(shape, a, b)` | Returns the area of a circle, rectangle or triangle |
| `convert(kind, value)` | Converts KM to Miles or Celsius to Fahrenheit |

### Helper functions

| Function | What it does |
|----------|--------------|
| `show_menu(title, options)` | Prints any menu and returns the user's choice |
| `ask_number(message)` | Keeps asking until the user types a valid number |
| `log(text)` | Saves a line with date and time into `toolkit_log.txt` |

### Menu functions

| Function | What it does |
|----------|--------------|
| `datetime_menu()` | Runs the datetime and time sub-menu |
| `math_menu()` | Runs the mathematical operations sub-menu |
| `random_menu()` | Runs the random data sub-menu |
| `uuid_menu()` | Runs the unique identifier sub-menu |
| `file_menu()` | Runs the file operations sub-menu |
| `explore_menu()` | Shows the attributes of any module using `dir()` |
| `main()` | Shows the main menu and sends the user to the chosen option |

## Python Concepts Used

- Standard modules: `datetime`, `time`, `math`, `random`, `string`, `uuid`, `os`
- Dynamic importing using `importlib`
- Exploring module attributes using `dir()`
- Functions using `def` with parameters and return values
- `__name__` and `__main__` to start the program only when the file is run directly
- File handling using `open()` and the `with` statement
- File modes `r`, `w` and `a`
- Date and time formatting using `strftime` and `strptime`
- Exception handling using `try` and `except`
- `while` loop for every menu
- `if`, `elif`, and `else`
- Dictionary used to connect menu numbers to functions
- List comprehension and generator expressions

## How to Run the Project

### Step 1: Open the Project

Open the project folder in Visual Studio Code (or any editor you like).

### Step 2: Open the Terminal

Open the integrated terminal in Visual Studio Code.

### Step 3: Go to the Project Folder

```powershell
cd "D:\RND Assignments\Multi_Utility_Toolkit"
```

### Step 4: Run the Python File

```powershell
py multi_utility_toolkit.py
```

### Step 5: Use the Menu

The welcome menu appears. Type a number from 1 to 7 and press Enter.

## How the Program Works (Step by Step)

### 1. Datetime and Time Operations

Type `1` in the main menu. A sub-menu appears:

1. Display current date and time
2. Calculate difference between two dates
3. Format date into custom format
4. Stopwatch
5. Countdown Timer
6. Back to Main Menu

**Display current date and time:** shows the current date and time as
`YYYY-MM-DD HH:MM:SS` and saves it in the log file.

**Difference between two dates:** type two dates in `YYYY-MM-DD` format. The
program shows the number of days between them. If the format is wrong, a
friendly message is shown.

**Custom format:** type a format using `strftime` codes, such as
`%d-%m-%Y %I:%M %p`, and the current date and time is shown in that style.

**Stopwatch:** press Enter to start, press Enter again to stop. The elapsed
time in seconds is shown and saved in the log file.

**Countdown timer:** type the number of seconds. The program counts down one
number per second and shows `Time is up!` at the end.

```text
Enter your choice: 2
Enter the first date (YYYY-MM-DD): 2024-12-25
Enter the second date (YYYY-MM-DD): 2025-01-04
Difference: 10 days
```

### 2. Mathematical Operations

Type `2` in the main menu. A sub-menu appears:

1. Calculate Factorial
2. Solve Compound Interest
3. Trigonometric Calculations
4. Area of Geometric Shapes
5. Unit Conversions
6. Back to Main Menu

**Factorial:** type a number (0 or more) and the factorial is shown.

**Compound interest:** type the principal, the rate in % and the time in
years. The program shows the final amount and the interest earned.

**Trigonometry:** type an angle in degrees. The program shows sin, cos and tan.

**Area:** type `circle`, `rectangle` or `triangle` and then the sizes asked.

**Unit conversions:** choose KM to Miles or Celsius to Fahrenheit and type the value.

```text
Enter principal amount: 1000
Enter rate of interest (in %): 5
Enter time (in years): 2
Final Amount: 1102.50
Compound Interest: 102.50
```

### 3. Random Data Generation

Type `3` in the main menu. A sub-menu appears:

1. Generate Random Number
2. Generate Random List
3. Create Random Password
4. Generate Random OTP
5. Random Sampling from a Dataset
6. Back to Main Menu

**Random number:** type the smallest and largest number to get a random number
between them.

**Random list:** type how many numbers you want. Each number is between 1 and 100.

**Random password:** type the length. The password uses letters, digits and
the symbols `@#$!&`.

**Random OTP:** shows a 6-digit OTP.

**Random sampling:** type items separated by commas, then how many items to
pick. The program picks that many different items at random.

```text
Enter your choice: 3
Enter password length: 8
Generated Password: Kd8@qzP!
```

### 4. Generate Unique Identifiers (UUID)

Type `4` in the main menu. A sub-menu appears:

1. Generate a UUID (UUID4)
2. Generate an Invoice ID
3. Back to Main Menu

**UUID4:** shows a random unique identifier.

**Invoice ID:** shows a short unique number starting with `INV-` and saves it
in the log file.

```text
Enter your choice: 2
Invoice ID: INV-084B9256
```

### 5. File Operations (Custom Module)

Type `5` in the main menu. A sub-menu appears:

1. Create a new file
2. Write to a file
3. Read from a file
4. Append to a file
5. Back to Main Menu

The program asks for a file name (for example `example.txt`) and then does
the chosen task.

```text
Enter your choice: 1
Enter file name: example.txt
File created successfully!
Enter your choice: 2
Enter file name: example.txt
Enter data to write: This is a sample file.
Data written successfully!
Enter your choice: 3
Enter file name: example.txt
File Content:
This is a sample file.
```

If the file does not exist while reading, the message `File not found.` is shown.

### 6. Explore Module Attributes (dir())

1. Type `6` and press Enter.
2. Type a module name such as `math` or `random`.
3. The program shows all public attributes of that module.

Type `toolkit` to explore the functions inside this program itself. If the
module name is wrong, the message `Sorry, that module could not be found.`
is displayed.

### 7. Exit

Type `7` and press Enter. The message
`Thank you for using the Multi-Utility Toolkit!` is displayed and the program
closes.

If any other number or text is typed, the message
`Invalid choice, please try again.` is displayed and the menu appears again.

## The Log File

The program saves these actions in `toolkit_log.txt` with the date and time:

- Current date and time viewed
- Stopwatch result
- Compound interest calculated
- Password generated
- Invoice ID created

Example:

```text
[2026-10-29 12:28:55] Invoice ID created: INV-084B9256
```

## File Modes Used

| Mode | Where it is used | Effect |
|------|------------------|--------|
| `r` | Read from a file | Only reads the file. The file must exist |
| `w` | Create a file and write to a file | Creates the file, or replaces the old content if it already exists |
| `a` | Append to a file and the log file | Adds to the end of the file and keeps old content |

The log file uses mode `a`, so old log lines are never erased.

## Exception Handling

| Error | When it happens | What the program does |
|-------|-----------------|-----------------------|
| `ValueError` | User types letters instead of a number | Asks again for a valid number |
| `ValueError` | User types a date in the wrong format | Shows `Wrong format. Please use YYYY-MM-DD.` |
| `ImportError` | User types an unknown module name in the explore option | Shows `Sorry, that module could not be found.` |
| Missing file | User reads a file that does not exist | Shows `File not found.` |

## Project Structure

```text
Multi_Utility_Toolkit
│
├── multi_utility_toolkit.py
├── toolkit_log.txt
└── README.md
```

`toolkit_log.txt` is created automatically the first time an action is logged.
Files created from the File Operations menu are saved in the same folder.

## Assumptions

- All files are saved in the same folder where the program is run.
- Dates are typed in `YYYY-MM-DD` format.
- Compound interest is calculated once per year.
- The compound interest option shows both the final amount and the interest earned.
- Passwords use letters, digits and the symbols `@#$!&`.
- OTPs are always 6 digits.
- Random list numbers are between 1 and 100.
- Creating a file with an existing name empties that file, because mode `w` is used.
- The custom file and math modules are kept as separate sections inside one
  Python file, so that the project is easy to run and submit.
- The program works only with text files.

## Requirements

- Python 3.8 or newer
- Visual Studio Code (optional)
- Python extension for Visual Studio Code (optional)

No external Python libraries are required for this project.

## Learning Outcomes

After completing this project, the user can understand:

- How to use standard modules such as `datetime`, `time`, `math`, `random` and `uuid`
- How to write reusable functions and keep related code together
- How `__name__` and `__main__` control when a program starts
- How to explore a module using `dir()`
- How to read, write and append text files
- How to handle invalid user input without crashing
- How to build a menu-driven Python program with sub-menus

## Conclusion

Multi-Utility Toolkit is a practical Python console project. It combines
standard modules, reusable functions, file handling and a simple menu system
in one program, and it is suitable for beginners who are learning how Python's
modular structure works.