import os

def list_directory_contents(directory_path):
    try:
        # Get the list of all files and directories
        contents = os.listdir(directory_path)
        print(f"Contents of the directory '{directory_path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"Error: The directory '{directory_path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access '{directory_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Specify the directory you want to list
directory_path = input("Enter the directory path: ")
list_directory_contents(directory_path)
