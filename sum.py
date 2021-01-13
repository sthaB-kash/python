# The function is expected to return an integer.
# The function accepts an integer as parameter.

def logic(my_input):
    sum = 0
    while my_input > 0:
        num = int(input())
        sum += num
        my_input -= 1
    return sum

# Do not edit below

# Get the input
my_input = int(input())

# Print output returned from the logic function
print(logic(my_input))