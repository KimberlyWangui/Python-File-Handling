file_name = input("Enter the name of the file to read:(including .txt) ")

try:
    file = open(file_name, "r")
    original_content = file.read()
    print("Original Content:", original_content)
    file.close()
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
    