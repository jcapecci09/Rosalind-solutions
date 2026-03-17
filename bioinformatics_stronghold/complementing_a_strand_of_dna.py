"""Produces the complement strand of DNA

This could be performed easily with biopython, but I opted to create my own 
solution

TODO grab input file from rosalind, Test script, write corresponding dataset in comments

Author: Jimmy Capecci
"""
import argparse
import sys


def main():

    # Define parser for command line interface
    parser = argparse.ArgumentParser(description='Finds complement of DNA')
    parser.add_argument('-i', '--input', help='input file', required=True)
    parser.add_argument('-o', '--output', help='output file', required=True)

    # Define infile and outfile
    args = parser.parse_args(sys.argv[1:])
    infile = args.input
    outfile = args.output

    # Create dictionary that maps amino acids to reverse complements
    d = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    # Read contents from input file and create complement strand
    with open(infile, 'r') as f:

        # Read DNA strand and strip new line
        dna = f.readline().strip()

        # Find the complement
        complement = ''
        for base in dna:
            complement += d[base]

    # Write output
    with open(outfile, 'w') as f:
        f.write(complement[::-1])

if __name__ == '__main__':
    main()
