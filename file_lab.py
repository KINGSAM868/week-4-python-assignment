# Import the necessary modules.
import os

def process_file_with_error_handling():
    """
    Reads a text file, converts its content to uppercase, and writes the
    result to a new destination file.
    
    The program includes robust error handling for common file-related issues
    such as FileNotFoundError.
    """
    
    # Prompt the user for the source and destination filenames.
    source_filename = input("Enter the name of the source file to read: ")
    destination_filename = input("Enter the name of the new destination file to write: ")
    
    try:
        # Use a 'with' statement for safe file handling.
        # This ensures the file is automatically closed, even if errors occur.
        with open(source_filename, 'r') as source_file:
            # Read the entire content of the source file.
            content = source_file.read()
            print(f"Successfully read content from '{source_filename}'.")
            
        # Convert the content to uppercase.
        modified_content = content.upper()
        
        # Open the destination file in write mode ('w').
        # If the file exists, its content will be overwritten.
        # If it doesn't exist, a new file will be created.
        with open(destination_filename, 'w') as dest_file:
            # Write the modified, uppercase content to the new file.
            dest_file.write(modified_content)
            print(f"Successfully wrote uppercase content to '{destination_filename}'.")
            print("Process completed!")
            
    # Handle the specific error if the source file does not exist.
    except FileNotFoundError:
        print(f"Error: The file '{source_filename}' was not found. Please check the filename and try again.")
        
    # Handle other potential I/O errors, such as permission issues.
    except IOError as e:
        print(f"An I/O error occurred: {e}")
        
    # A general exception handler for any other unexpected errors.
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function to start the program.
if __name__ == "__main__":
    process_file_with_error_handling()
