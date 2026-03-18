
import argparse
import sys

def counter(letter: str, input: str):
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
            
    with open(infile, 'r') as file:
        data = file.readline()
    
    with open(outfile, 'w') as f:
        f.write(f'{counter('A', data)} {counter('C', data)} {counter('G', data)} {counter('T', data)}\n')

if __name__ == '__main__':
    main()