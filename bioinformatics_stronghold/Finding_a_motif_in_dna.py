"""Find the starting position of motif in a sequence. There could be multiple
motifs in the sequence. 

Challenges:
I messed up once b/c I forgot to use strip() at first. Took me 5 mins to 
figure that out.
"""

import argparse
import sys


def main():

     # Set up parser
    parser = argparse.ArgumentParser(description='Returns longest motif')
    parser.add_argument('-i', '--input', help='input file', required=True)
    parser.add_argument('-o', '--output', help='output file', required=True)

    # define infile and outfile
    args = parser.parse_args(sys.argv[1:])
    infile = args.input
    outfile = args.output

    # Open the file and read the sequence and motif
    with open(infile, 'r') as f:
        sequence = f.readline()
        motif = f.readline().strip()

    # Explicitly set motif length
    motif_length  = len(motif)
    motif_positions = []

    # For every base in the sequence take the index
    for index in range(len(sequence)):

        # Take a subsequence thats the same size as the motif
        subseq = sequence[index:index+motif_length]

        # Is it the motif? Yes! save the position
        # Have to use + 1 b/c python index starts at 0
        if subseq == motif:
            motif_positions.append(index + 1)
    
    # Write to outfile
    with open(outfile, 'w') as f:
        for position in motif_positions:
            f.write(str(position) + '\n')


if __name__ == '__main__':
    main()