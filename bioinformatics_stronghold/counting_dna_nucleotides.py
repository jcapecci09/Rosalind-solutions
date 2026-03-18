"""Counts the respective number of nucleotides appearing in a dna string. 
Only works if input dna string is on one line. 

Example Output: 214 191 199 212

Where numbers correspond to the following:
A C G T

Author: Jimmy Capecci
"""

import argparse
import sys

def counter(letter: str, input: str) -> str:
    """Returns the number of times letter appears in the input

    :param letter: Letter to find in input
    :param input: Input dna string
    :return: Number of times letter appears in input as a string
    """

    # Simply counts occurences of letter in input
    count = 0 
    for line in input:
        if letter == line:
            count += 1
    return str(count)

def main():

    # set up parser
    parser = argparse.ArgumentParser(description='Counts the respective number of times a nucleotides appears in a dna string')
    parser.add_argument('-i', '--input', help='input file', required=True)
    parser.add_argument('-o', '--output', help='output file', required=True)

    # Define infile and outfile
    args = parser.parse_args(sys.argv[1:])
    infile = args.input
    outfile = args.output
    
    # Input file to read dna string
    with open(infile, 'r') as file:
        data = file.readline()
    
    # Output file to write occurences to
    with open(outfile, 'w') as f:
        f.write(f'{counter('A', data)} {counter('C', data)} {counter('G', data)} {counter('T', data)}\n')

if __name__ == '__main__':
    main()
