def remove_duplicates(values):
    unique = []
    for num in values:
        if num not in unique:
            unique.append(num)
    print(values)
    print(unique)


num = int(input('how many numbers? : '))
print(f'enter {num} different numbers: \n')
numbers = list()
for n in range(num):
    numbers.append(int(input(f'num {n+1}: ')))

print(numbers)
remove_duplicates(numbers)


