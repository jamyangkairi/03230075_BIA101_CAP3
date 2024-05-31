
# https://github.com/jamyangkairi/03230075_BIA101_CAP3
# JAMYANG CHOZOM 
# BBIA 
# 03230075
#REFERENCES
# https://www.geeksforgeeks.org/extract-numbers-from-a-text-file-and-add-them-using-python/
# https://www.sarthaks.com/3576170/write-python-program-to-read-text-file-and-print-only-the-sum-of-all-the-digits-from-the-file

# read the input.txt file

def read_input(file_path):

 # try code will execute block of statment if there is 
 #any mistake in the code instead of showing error in the terminal. that way we will know that we have made mistakes 
    try:    
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return []
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return []

def extract_digits(line):
    first_digit = None
    last_digit = None

    for char in line:
        if char.isdigit():
            first_digit = char
            break  
    
    for char in reversed(line):
        if char.isdigit():
            last_digit = char
            break 
    
    # Checking if both first and last digits are found
    if first_digit is not None and last_digit is not None:
        two_digit_number = int(first_digit + last_digit)
        return two_digit_number
    
    return None  # Return None if no digits are found

def process_lines(lines):
    total_sum = 0 
    results = []  
    
    for line in lines:  # Iterate through each line in the input lines
        two_digit_number = extract_digits(line) 
        if two_digit_number is not None:  
            results.append((line, two_digit_number))  
            total_sum += two_digit_number  
    
    return total_sum, results  # Return the total sum and the list of results

def print_results(file_path):
    input_lines = read_input(file_path)  # Read lines from  file

    if input_lines: 
        total_sum, results = process_lines(input_lines)  

        for line, num in results: 
            print(f"{line} -> {num}")

        print(f"Total sum: {total_sum}") 
    else:
        print("No lines") 

print_results('075.txt')




