"""
Calculates the expected offspring that express the dominant phenotype.
Given 6 integers corresponding to number of breeding pairs per each allele type. 

1. AAAA
2. AAAa
3. AAaa
4. AaAa
5. Aaaa
6. aaaa

TODO Add dataset from rosalind, test, write corresponding dataset in comments

Author: Jimmy Capecci
"""

import argparse
import sys

def main():

    # set up praser for command line interface
    parser = argparse.ArgumentParser(description='Calculates expected offspring that express dominant phenotype')
    parser.add_argument('-i', '--input', help='input file', required=True)
    parser.add_argument('-o', '--output', help='output file', required=True)

    # Define infile and outfile
    args = parser.parse_args(sys.argv[1:])
    infile = args.input
    outfile = args.output

    # Open input data 
    with open(infile, 'r') as f:

        # Turn data into list spliting by spaces 
        str_parents = f.readline().strip().split(' ')

        # Turn each into integer 
        parents = [int(i) for i in str_parents]

    # intiate expected value 
    expected_value = 0

    # First 3 allele types will have same probability of 1
    first_3 = parents[0:3]

    # Calculate expected value for firts 3 allele types 
    for num in first_3:
        expected_value += (num * 2)

    # calculate expected value for next two allele types
    # AaAa corresponds to 75% chance of expressing dominant phenotype 
    expected_value += (parents[3] * 2 * 0.75)
    expected_value += (parents[4] * 2 * 0.5)

    # Open outfile and write expected value
    with open(outfile, 'w') as f:
        f.write(expected_value)

if __name__ == '__main__':
    main()
