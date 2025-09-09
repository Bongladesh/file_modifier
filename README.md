# File Modifier Program

A Python program that demonstrates file handling with comprehensive error handling. This program reads a file, adds line numbers and statistics, and creates a modified version.

## Features

- **File Reading**: Safely reads text files with error handling
- **Content Modification**: Adds line numbers and file statistics
- **File Writing**: Creates new modified files with "_modified" suffix
- **Error Handling**: Handles common file-related errors gracefully
- **User Feedback**: Provides previews and statistics about the processed files

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Bangladsh/file_modifier.git
Navigate to the project directory:

bash
cd file-modifier-project
Usage
Run the program:

bash
python file_modifier.py
Enter the filename when prompted:

text
Please enter the filename to read: sample.txt
The program will process the file and create a modified version

Example
Input file (sample.txt):

text
Hello world!
This is a test file.
Python file handling example.
Output file (sample_modified.txt):

text
# File Statistics: 3 lines, 10 words

  1: Hello world!
  2: This is a test file.
  3: Python file handling example.
Error Handling
The program handles these error scenarios:

❌ File not found errors

❌ Permission denied errors

❌ Directory inputs instead of files

❌ Encoding issues with binary files

❌ Other unexpected errors
