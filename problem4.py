import os

# Specify the directory path
directory_path = '/'

try:
    # Get the list of all entries in the directory
    entries = os.listdir(directory_path)
    
    # Iterate over the entries and print them
    for entry in entries:
        print(entry)
except FileNotFoundError:
    print(f"The directory {directory_path} does not exist.")
except PermissionError:
    print(f"Permission denied to access {directory_path}.")
