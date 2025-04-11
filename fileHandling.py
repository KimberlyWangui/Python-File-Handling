file = open("example.txt", "r")
original_content = file.read()
file.close()

modified_content = original_content + "\nThis is a new line added to the file."

file1 = open("modified_example.txt", "w")
file1.write(modified_content)
file1.close()

file2 = open("modified_example.txt", "r")
print(file2.read())
file2.close()
