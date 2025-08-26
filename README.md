# week-4-python-assignment
Python File Processor
This program is a simple command-line utility written in Python that reads the contents of a text file, modifies the text, and saves the result to a new file. It's designed to be a clear example of basic file input/output (I/O) and robust error handling.

Features
Reads Content: Reads the entire content of a specified source file.

Converts to Uppercase: Transforms all text to uppercase.

Writes to New File: Creates and writes the modified content to a specified destination file.

Handles Errors Gracefully: Includes a try...except block to catch and handle common issues like FileNotFoundError, providing a user-friendly message instead of crashing.

How to Run
Make sure you have Python installed on your computer.

Save the Python code (the process_file_with_error_handling() function and the if __name__ == "__main__": block) into a file named file_processor.py.

Open your terminal or command prompt.

Navigate to the directory where you saved the file.

Run the program by typing the following command:

python file_processor.py

The program will then prompt you to enter the name of the source file and the destination file.