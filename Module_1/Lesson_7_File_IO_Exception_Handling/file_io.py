# file_io.py

def write_to_file(filename, content):
    """Write content to a file and notify if successful."""
    try:
        with open(filename, 'w') as file:
            file.write(content)
            print(f"Successfully written to {filename}")
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")

def read_from_file(filename):
    """Read content from a file and return it."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return None
    except IOError as e:
        print(f"Error reading file {filename}: {e}")
        return None

if __name__ == "__main__":
    # Define filename and content
    filename = "sample.txt"
    content_to_write = "Hello, this is a sample file.\nIt contains multiple lines."
    
    # Write content to the file
    write_to_file(filename, content_to_write)
    
    # Read content from the file
    content_read = read_from_file(filename)
    if content_read is not None:
        print("Content of the file:")
        print(content_read)

def safe_division(a, b):
    """Return the division of a by b, handling division by zero."""
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None

if __name__ == "__main__":
    # File I/O demonstration as above
    # ...
    
    # Exception Handling demonstration for division
    result1 = safe_division(20, 4)
    result2 = safe_division(20, 0)
    
    print("Division result for 20 / 4:", result1)
    print("Division result for 20 / 0:", result2)
