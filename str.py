# The function is expected to return a string.
# The function accepts string as parameter.

def logic(my_input):
    # Write your code here and remove pass statement
    # You can create other functions and call from here
    # Don't print anything. Just return the intended output
    words = my_input.split(' ')
    punc = ['.', ';', ':', '?', '!']
    val = 'arg'
    rel = " "
    space = ' '
    for word in words:
        for p in punc:
            index = word.find(p)

        if index == -1:
            word = word[1:-1]+word[0]+val
        else:
            word = word[1:index]+word[0]+ val +word[index:]
        rel = rel + word + space

    return rel

# Do not edit below

# Get the input
my_input = input()

# Print output returned from the logic function
print(logic(my_input))
