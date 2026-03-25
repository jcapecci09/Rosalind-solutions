"""Translates RNA into protein uses a dictionary. This process can be performed
using Biopython but I wanted to implement it myself.

corresponding dataset: rosalind_prot.txt
Author: Jimmy Capecci
"""

import toolkit
import argparse
import sys


# I achieved this from codon_table.txt and the function in toolkit.py
# Some people acheived this by using zip(), but I found that 
# A little complicated for me right now
codons = toolkit.codon_table()


def translation(rna: str) -> str:
    """Transalates an rna seq using codons
    dictionary. 

    :param rna: Rna sequence
    :return:  Protein sequence
    """
    
    protein = ''

    # create range of index every 3 indices
    # Ex: 0, 3, 6, 9
    for item in range(0, len(rna), 3):
        protein += codons[rna[item:item+3]]
    
    return protein

def main():

    # Set input files
    args = toolkit.create_parser('Converts RNA into protein sequence')
    infile = args.input

    # Open rna seq file and convert it to protein sequence
    with open(infile, 'r') as f:
        rna_seq = f.readline().strip()

    # Translate rna to protein and remove the STOP part
    prot = translation(rna_seq)[:-4]

    # Write protein sequence to outfile or to terminal
    toolkit.output(prot, args)

if __name__ == '__main__':
    main()