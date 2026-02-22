def is_vowel(char):
    vowels = 'aeiouAEIOU'
    if char in vowels:
        return True
    else:
        return False

char = input("Enter a character: ")
if len(char) == 1 and char.isalpha():
    if is_vowel(char):
        print(char, "is a vowel.")
    else:
        print(char, "is a consonant.")