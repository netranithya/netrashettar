file_name = input("Enter the file name: ")
try:
    with open(file_name, 'r') as file:
        file_contents = file.read()
        print("File contents:")
        print(file_contents)
except FileNotFoundError:
    print(f"File '{file_name}' not found.")

