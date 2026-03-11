"""Finds the largest motif from a multi-fasta file. If multiple motifs are the same size 
the script will return only one randomly.

Author: Jimmy Capecci
"""

import sys
import argparse


def partition(seq: str, n:int) -> set:
    """Partitions a sequence into all 
    possibe sequences of size n

    :param seq: Sequence to be partitioned 
    :param n: Size of partitions
    :return: Set of all partitions
    """

    # Create set to store sequences, calcukate length of sequence
    # and initialize an index
    subseqs = set()
    total_length = len(seq)
    index = 0 

    # Loop through until all sub-sequences are found
    while True:

        # Find subsequence and add 1 to index to move
        # where the start of sequence will be
        subseqs.add(seq[index:index+n])
        index += 1

        # Stop conditon, once you reach the end 
        # Of the sequence break the loop
        if index+n == total_length + 1:
            break
    
    # return all unique subsequences in a set
    return subseqs


def main():

    # Set up parser
    parser = argparse.ArgumentParser(description='Returns longest motif')
    parser.add_argument('-i', '--input', help='input file', required=True)
    parser.add_argument('-o', '--output', help='output file', required=True)

    # what to read
    args = parser.parse_args(sys.argv[1:])

    # set infile and outfile
    infile = args.input
    outfile = args.output

    # Collect all dna sequences from fasta file
    with open(infile, 'r') as f:
        dna_strings = [] # Contains dna sequence
        dna_string = '' # Build dna sequence
        f.readline() # Read first line
        
        # for each line in the fasta file
        for line in f:

            # If it doesn't starts with '>' its part of a sequence add to sequence
            if not line.startswith('>'):
                dna_string += line.strip()
            
            # else add sequence to the list and reset sequence
            else:
                dna_strings.append(dna_string)
                dna_string = ''
        
        # Add the last sequence 
        dna_strings.append(dna_string)

    # Create list to compute lenghts of sequences
    lengths = []

    # Compute lengths of each sequence and add to list
    for dna in dna_strings:
        length = len(dna)
        lengths.append(length)

    # Find the smallest dna sequence
    index = lengths.index((min(lengths)))
    smallest_dna = dna_strings[index]

    # Intialize n to be the size of the smallest sequence
    n = len(smallest_dna)

    # Loop until we find the largets motif between the sequence
    while True:
        
        # Parititon smallest dna into n sized sequences
        substrings = partition(smallest_dna, n)

        # Intialize variable that will track loop
        truth = True

        # Compare each substring to the smallest dna substrings
        for dna in dna_strings:
            dna_substrings = partition(dna, n) # Partition into n sized sequences
            substrings = dna_substrings & substrings # Find the "blank" between sets

            # If substrings is empty then there are no motifs break loop
            if len(substrings) == 0:
                truth = False
                break

        # Subtract size
        n -= 1
        # we have either found the largest motif or there are no motifs
        if truth is True or n == 0:
            break
        
    
    # Write answer to outfile
    with open(outfile, 'w') as f:
        f.write(list(substrings)[0])

  
if __name__ == '__main__':
    main()            
