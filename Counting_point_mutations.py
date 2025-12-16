"""We will be calculating hamming distance: 
the number of mismatches between two sequences.
Author: Jimmy Capecci
This problem comes from https://rosalind.info/problems/hamm/
"""

# Open a text file containing two sequences on two lines
with open('rosalind_hamm (3).txt', 'r') as f:

    # Read first and second lines
    first = f.readline()
    second = f.readline()

    # intialize variables
    index = 0
    hamming_distance = 0

    # Look at each base of first sequence and compare it to each base of the second
    # Add 1 to the hamming distance if they are unequal
    for base in first: 
        if base != second[index]:
            hamming_distance += 1
        index += 1
    print(hamming_distance)
