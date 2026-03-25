"""A toolkit containing fuctions that reoccur throughout each script

Author: Jimmy Capecci
"""
import argparse
from __future__ import annotations

def output(out, arguments):
    """If output file is specefied writes to the file. If not 
    the function will  print to terminal

    :param out: What to write or print
    :param arguments: input arguments to check if  output file exists
    """

    # Write to output file 
    if arguments.output:
        with open(arguments.output, 'w') as f:
            f.write(out + '\n')
    
    # If it doesnt exist print to terminal
    else:
        print(out)


def codon_table() -> dict[str, str]:
    """Returns codon dicitonary  to map codon to amino acid

    :return: Codon table as dictionary
    """

    # In rosalind Im giving text showing the codon table
    # However, I need to copy this text in a file and turn it into  
    # A usable dictionary for translation

    # Parse text file and turn codon table into dictionary
    codon_d = {}
    with open('misc/codon_table.txt', 'r') as f:

        for line in f:
            codons = line.strip().split()
            codon_d[codons[0]] = codons[1]
            codon_d[codons[2]] = codons[3]
            codon_d[codons[4]] = codons[5]
            codon_d[codons[6]] = codons[7]
    return codon_d


def create_parser(desc: str) -> argparse.ArgumentParser:
    """Allows scripts to be easily interfaced with the command line. 

    :param desc: Description describing the python script
    :return: An argument parser for command line interface
    """

    # Set up parser and add arguments
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-i', '--input', help='input file', required=True)
    parser.add_argument('-o', '--output', help='output file')

    return parser.parse_args()
