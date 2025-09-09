import os

def read_file(filename):
    """
    Read content from a file with error handling
    Returns content as string if successful, None otherwise
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to read the file '{filename}'.")
    except IsADirectoryError:
        print(f"Error: '{filename}' is a directory, not a file.")
    except UnicodeDecodeError:
        print(f"Error: Unable to decode the file '{filename}'. It may be a binary file.")
    except Exception as e:
        print(f"An unexpected error occurred while reading '{filename}': {str(e)}")
    return None

def write_file(filename, content):
    """
    Write content to a file with error handling
    Returns True if successful, False otherwise
    """
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Successfully wrote to '{filename}'")
        return True
    except PermissionError:
        print(f"Error: Permission denied to write to the file '{filename}'.")
    except IsADirectoryError:
        print(f"Error: '{filename}' is a directory, not a file.")
    except Exception as e:
        print(f"An unexpected error occurred while writing to '{filename}': {str(e)}")
    return False

def modify_content(content):
    """
    Modify the content of the file (example modifications)
    """
    if content is None:
        return None
    
    # Count lines and words
    lines = content.split('\n')
    word_count = sum(len(line.split()) for line in lines)
    
    # Add a header with statistics
    modified = f"# File Statistics: {len(lines)} lines, {word_count} words\n\n"
    
    # Add line numbers to each line
    for i, line in enumerate(lines, 1):
        modified += f"{i:3}: {line}\n"
    
    return modified

def main():
    print("=" * 50)
    print("FILE READER AND MODIFIER PROGRAM")
    print("=" * 50)
    
    # Get filename from user
    filename = input("Please enter the filename to read: ").strip()
    
    # Read the file
    content = read_file(filename)
    
    if content is None:
        print("Unable to read the file. Please check the filename and try again.")
        return
    
    # Modify the content
    modified_content = modify_content(content)
    
    # Create output filename
    base_name, ext = os.path.splitext(filename)
    output_filename = f"{base_name}_modified{ext}"
    
    # Write the modified content
    write_file(output_filename, modified_content)
    
    # Show a preview of the modified content
    print("\nPreview of modified content (first 10 lines):")
    print("-" * 50)
    lines = modified_content.split('\n')
    for line in lines[:10]:
        print(line)
    
    if len(lines) > 10:
        print("... (content truncated)")
    
    print(f"\nOriginal file size: {len(content)} characters")
    print(f"Modified file size: {len(modified_content)} characters")
    print(f"Output file: {output_filename}")

if __name__ == "__main__":
    main()