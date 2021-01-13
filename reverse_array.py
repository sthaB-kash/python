numbers = []
n = int(input("how many numbers in array:> "))
m = 1
while m <= n:
    numbers.append(int(input(f'{m}:')))
    m +=1
print(numbers)
numbers.reverse()
print(numbers)