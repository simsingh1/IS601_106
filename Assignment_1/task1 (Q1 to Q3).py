# Name - Simranjit Singh
# UCID - ss2267
# Date - 17th Feb 2024

# Question 1: Filter and print odd values from the lists
def odd_values(num, arr):
    print(f'Output for arr{num}:')
    # Filter odd values using list comprehension and print them
    print(*[x for x in arr if x % 2 != 0], sep=', ')
    print('End of odd values\n')

# Function calls for Question 1
odd_values(1, [89, 52, 36, 24, 17, 99, 82, 73, 61, 48])
odd_values(2, [89, 52, 36, 24, 17, 99, 82, 73, 61, 48])
odd_values(3, [15, 13, 16, 12, 17, 11, 18, 10, 19, 9])

# Question 2: Calculate and print the sum of list values
def sum_values(num, arr):
    print(f'Output for arr{num}:')
    # Sum the values in the list and print the total
    total = sum(arr)
    print(total)
    print('End of sum values\n')

# Function calls for Question 2
sum_values(1, [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
sum_values(2, [17, 19, 15, 16, 14, 18, 13, 12, 11, 20])
sum_values(3, [55, 66, 77, 88, 99, 11, 22, 33, 44])

# Question 3: Convert negative values to positive and calculate the sum
def converted_sum_values(num, arr):
    print(f'Output for arr{num}:')
    # Convert negative numbers to positive and sum all values
    total = sum(abs(x) for x in arr)
    print(total)
    print('End of converted sum values\n')

# Function calls for Question 3
converted_sum_values(1, [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100])
converted_sum_values(2, [5, -8, 13, -21, 34, -55, 89, -144, 233])
converted_sum_values(3, [-7, 12, -15, 18, -21, 24, -27, 30, -33])
converted_sum_values(4, [11, -22, 33, -44, 55, -66, 77, -88, 99])
converted_sum_values(5, [-3, 6, -9, 12, -15, 18, -21, 24, -27, 30])