""" Transcribes DNA sequence to RNA (Thymine to uracil)

Author: Jimmy Capecci
"""

import argparse
import sys

def main():

    # Set up parser for command-line interface
    parser = argparse.ArgumentParser(description='Converts DNA to RNA')
    parser.add_argument('-i', '--input', help='input file', required=True)
    parser.add_argument('-o', '--output', help='output file', required=True)

    # define infile and outfile
    args = parser.parse_args(sys.argv[1:])
    infile = args.input
    outfile = args.output

    # Opens DNA sequence and converts all thymines to uracil
    # This could be performed with string method replace, but I opted to do it myself
    with open(infile, 'r') as file:
        new_sequence = ''
        sequence = file.readline()
        for letter in sequence:
            if letter == 'T':
                letter = 'U'
            new_sequence += letter
    
    # Write RNA sequence to outfile
    with open(outfile, 'w') as f:
        f.write(new_sequence)

if __name__ == '__main__':
    main()