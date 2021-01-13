print("<<know the file extension>>")
file_name = input("enter your file name:> ")
index = 0
for ch in file_name:
    index += 1
    if ch == '.':
        break
print(f'Your file extension is: {file_name[index:]}')
