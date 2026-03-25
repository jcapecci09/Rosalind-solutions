
import subprocess
import sys

dna =  'ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG'
introns = ['ATCGGTCGAA', 'ATCGGTCGAGCGTGT']
introns =  sorted(introns, key=len, reverse=True)

print(dna)

for intron in introns:
    dna = dna.replace(intron, '')


