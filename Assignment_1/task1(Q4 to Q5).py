# Name - Simranjit Singh
# UCID - ss2267
# Date - 17th Feb 2024

# Question 4: Remove empty strings from lists and print the result
def empty_str(num, arr):
    print(f'Output for arr{num}:')
    # Remove empty strings from the list
    filtered_list = [x for x in arr if x]
    print(filtered_list)
    print('End of empty str values\n')
    
# Function calls for Question 4
empty_str(1, ['apple', '', 'banana', '', 'cherry'])
empty_str(2, ['', 'dog', '', 'cat', ''])
empty_str(3, ['hello', '', 'world', '', ''])
empty_str(4, ['', '', '', '', ''])
empty_str(5, ['one', '', 'two', '', 'three'])

# Question 5: Find and print the smallest value in a list
def print_smallest(arr):
    # Check if the list is not empty to avoid ValueError
    if arr:
        print('The smallest value is:', min(arr))
    else:
        print('The list is empty.')

# Example function call for Question 5
print_smallest([4, 2, 15, 11, 23, 0])
