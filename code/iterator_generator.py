"""
Example of using iterators and generators in Python to process a large file
without loading the entire file into memory at once.
This is useful for handling large datasets efficiently.
"""

def take_n(n, itr):
    result = []
    for i in range(n):
        try:
            result.append(next(itr))
        except StopIteration:
            break
    return result

def find_my_pattern(line):
    # Check if line contains pattern
    if "smitin" in line:
        return True

with open('my_huge_file.txt', 'r') as FILE:
    results = take_n(3, filter(find_my_pattern,
                            (line for line in FILE)))

# Bonus, if you read my article on functional programming
# and function composition, this can be written even more clearly:



with open('my_huge_file.txt', 'r') as FILE:
     results =  (take_n(3, (line for line in FILE if find_my_pattern(line))))

     print (results)

with open('my_huge_file.txt', 'r') as FILE:
    results = take_n(3, filter(find_my_pattern,
                            (line for line in FILE)))
    print (results)

