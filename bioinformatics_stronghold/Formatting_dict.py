
codon_d = {}
with open('misc/codon_table.txt', 'r') as f:

    for line in f:
        codons = line.strip().split()
        codon_d[codons[0]] = codons[1]
        codon_d[codons[2]] = codons[3]
        codon_d[codons[4]] = codons[5]
        codon_d[codons[6]] = codons[7]

