word_without_vowels = ""

user_word = input("Enter the word: ")# Prompt the user to enter a word
user_word = user_word.upper() # and assign it to the user_word variable.


for letter in user_word:
    if letter == 'A':
         continue
    elif letter == 'E':
         continue
    elif letter == 'I':
         continue
    elif letter == 'O':
         continue
    elif letter == 'U':
         continue
    else:
         word_without_vowels = word_without_vowels + letter
print(word_without_vowels.upper())         #Print the word assigned
