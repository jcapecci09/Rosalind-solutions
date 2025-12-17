"""Find the starting position of motif in a sequence. there could be multiple
motifs in the sequence. 

Challenges:
I messed up once b/c I forgot to use strip() at first. Took me 5 mins to 
figure that out.
"""

# Open the file and read the sequence and motif
with open('rosalind_subs (1).txt', 'r') as f:
    sequence = f.readline()
    motif = f.readline().strip()

# Explicitly set motif length
motif_length  = len(motif)

# For every base in the sequence take the index
for index in range(len(sequence)):

    # Take a subsequence thats the same size as the motif
    subseq = sequence[index:index+motif_length]

    # Is it the motif? Yes! Print the position
    # Have to use + 1 b/c python idnex starts at 0
    if subseq == motif:
        print(index + 1)
