# Read three numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = num1

# We check if the second number is larger than current largest_number
# and update largest_number if needed.
if num2 > largest_number:
    largest_number = num2

# We check if the third number is larger than current largest_number
# and update largest_number if needed.
if num3 > largest_number:
    largest_number = num3

# Print the result
print("The largest number is:", largest_number)
