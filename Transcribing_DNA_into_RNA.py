
# Opens DNA sequence and converts all thymines to uracil
with open('rosalind_rna.txt', 'r') as file:
    new_sequence = ''
    sequence = file.readline()
    for letter in sequence:
        if letter == 'T':
            letter = 'U'
        new_sequence += letter
    print(new_sequence)