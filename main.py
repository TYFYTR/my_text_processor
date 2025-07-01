# Step 1 - Open and read the input file

# This line opens the file using a context manager
with open('input.txt', 'r') as file:
    # Reads the entire file content into a variable
    text = file.read()

# This line prints the file content to the terminal
print(text)