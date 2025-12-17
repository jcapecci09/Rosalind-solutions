



with open('rosalind_subs (1).txt', 'r') as f:
    sequence = f.readline()
    motif= f.readline().strip()

print(motif)
print(sequence)

motif_length  = len(motif)

for index in range(len(sequence)):
    subseq = sequence[index:index+motif_length]

    if subseq == motif:
        print(index + 1)
