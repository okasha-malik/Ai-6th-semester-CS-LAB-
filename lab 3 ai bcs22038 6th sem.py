# Program to find numbers divisible by 7 and multiple of 5 between a range
start_num = int(input("Enter the start number: "))
end_num = int(input("Enter the end number: "))

for number in range(start_num, end_num + 1):
    if number % 7 == 0 and number % 5 == 0:
        print(number)

# Temperature conversion program
def celsius_to_fahrenheit(temp_c):
    temp_f = (temp_c * 9/5) + 32
    return temp_f

def fahrenheit_to_celsius(temp_f):
    temp_c = (temp_f - 32) * 5/9
    return temp_c

print("\nTemperature Conversion Program")
print("1. Convert Celsius to Fahrenheit")
print("2. Convert Fahrenheit to Celsius")
option = input("Enter your choice (1 or 2): ")

if option == '1':
    temp_c = float(input("Enter temperature in Celsius: "))
    temp_f = celsius_to_fahrenheit(temp_c)
    print(f"{temp_c}°C is {temp_f:.1f}°F")
elif option == '2':
    temp_f = float(input("Enter temperature in Fahrenheit: "))
    temp_c = fahrenheit_to_celsius(temp_f)
    print(f"{temp_f}°F is {temp_c:.1f}°C")
else:
    print("Invalid choice. Please enter 1 or 2.")

# Number guessing game
import random
target_num = random.randint(1, 9)

while True:
    guessed_num = int(input("Guess a number between 1 and 9: "))
    if guessed_num == target_num:
        print("Well guessed!")
        break
    else:
        print("Wrong guess. Try again!")

# Print pattern using nested loops
for row in range(1, 6):
    for col in range(row):
        print("*", end=" ")
    print()

for row in range(4, 0, -1):
    for col in range(row):
        print("*", end=" ")
    print()

# Reverse a word
user_word = input("Enter a word: ")
reversed_word = user_word[::-1]
print("Reversed word:", reversed_word)

# Count even and odd numbers
number_input = input("Enter numbers separated by spaces: ")
number_list = [int(value) for value in number_input.split()]

even_total = 0
odd_total = 0

for value in number_list:
    if value % 2 == 0:
        even_total += 1
    else:
        odd_total += 1

print(f"Number of even numbers: {even_total}")
print(f"Number of odd numbers: {odd_total}")

# Print items and their types
mixed_list = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class": "V", "section": "A"}]
for data in mixed_list:
    print(f"Item: {data}, Type: {type(data)}")

# Print numbers 0 to 6 except 3 and 6
for val in range(7):
    if val == 3 or val == 6:
        continue
    print(val, end=' ')
print()  # For newline

# Fibonacci sequence up to 50
num1, num2 = 0, 1
while num1 <= 50:
    print(num1, end=' ')
    num1, num2 = num2, num1 + num2
print()

# FizzBuzz from 1 to 50
for count in range(1, 51):
    if count % 3 == 0 and count % 5 == 0:
        print("FizzBuzz")
    elif count % 3 == 0:
        print("Fizz")
    elif count % 5 == 0:
        print("Buzz")
    else:
        print(count)

# Generate 2D array based on row and column multiplication
rows = int(input("Enter number of rows (m): "))
cols = int(input("Enter number of columns (n): "))
matrix = [[i * j for j in range(cols)] for i in range(rows)]
print("Generated 2D Array:")
print(matrix)

# Accept multiple lines and print in lowercase
print("Enter your lines (press Enter twice to finish):")
line_collection = []
while True:
    single_line = input()
    if single_line.strip() == "":
        break
    line_collection.append(single_line.lower())

print("\nOutput (in lowercase):")
for lower_line in line_collection:
    print(lower_line)

# Filter binary numbers divisible by 5
binary_input = input("Enter comma-separated 4-digit binary numbers: ")
binary_items = [val.strip() for val in binary_input.split(',')]

filtered_bin = [binary for binary in binary_items 
                if len(binary) == 4 and int(binary, 2) % 5 == 0]

print(','.join(filtered_bin))

# Count digits and letters
user_input = input("Enter a string: ")
alpha_count = 0
digit_count = 0

for ch in user_input:
    if ch.isalpha():
        alpha_count += 1
    elif ch.isdigit():
        digit_count += 1

print(f"Letters {alpha_count}")
print(f"Digits {digit_count}")

# Validate password based on multiple rules
import re

def validate_password(user_password):
    if len(user_password) < 6 or len(user_password) > 16:
        return False, "Password must be 6-16 characters long"

    if not re.search("[a-z]", user_password):
        return False, "Password needs at least 1 lowercase letter"

    if not re.search("[A-Z]", user_password):
        return False, "Password needs at least 1 uppercase letter"

    if not re.search("[0-9]", user_password):
        return False, "Password needs at least 1 number"

    if not re.search("[$#@]", user_password):
        return False, "Password needs at least 1 special character ($, #, or @)"

    return True, "Password is valid"

# Get user input
input_password = input("Enter your password: ")

# Validate and show result
is_valid_pwd, result_msg = validate_password(input_password)
print(result_msg)
