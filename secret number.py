secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
guess= -1
while(secret_number!= guess):
    guess=int(input("Enter the input integer: "))
    if(guess != secret_number):
         print("Ha ha! You're stuck in my loop!. Try again!")

if(guess ==secret_number):
     print("Well done muggle! You are free now") 
