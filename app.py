user_word = input("Your word: ")

if user_word[0] == user_word[-1:]:
    print(f'Your word is a Palindrome')
else:
    print(f'Your word is not a Palindrome')