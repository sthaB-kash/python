str = input("enter any string:>\n")
vowel = 0
for ch in str:
    if ch in ['a', 'e', 'i', 'o', 'u']:
        print(ch)
        vowel += 1

print(f'No. of vowels in the string\'{str}\' is {vowel}')
