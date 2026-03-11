d = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

with open('rosalind_revc (1).txt', 'r') as f:
    dna = f.readline().strip()
    complement = ''
    for base in dna:
        complement += d[base]
print(complement[::-1])
