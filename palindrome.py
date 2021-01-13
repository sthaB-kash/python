print("Check palindrome")
string = input("Enter a string: ")
if string == string[::-1]:
    print(f'the string\'{string}\' is Palindrome')
else:
    print(f'the string \'{string}\' is not Palindrome')
