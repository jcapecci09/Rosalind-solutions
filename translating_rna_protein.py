# I achieved this from codons.txt in formatting_dict.py
# Some people acheived this by using zip(), but I founmd that 
# A little complicated for me right now
codons =  {'UUU':'F','CUU':'L','AUU':'I','GUU':'V',
'UUC':'F','CUC':'L','AUC':'I','GUC':'V',
'UUA':'L','CUA':'L','AUA':'I','GUA':'V',
'UUG':'L','CUG':'L','AUG':'M','GUG':'V',
'UCU':'S','CCU':'P','ACU':'T','GCU':'A',
'UCC':'S','CCC':'P','ACC':'T','GCC':'A',
'UCA':'S','CCA':'P','ACA':'T','GCA':'A',
'UCG':'S','CCG':'P','ACG':'T','GCG':'A',
'UAU':'Y','CAU':'H','AAU':'N','GAU':'D',
'UAC':'Y','CAC':'H','AAC':'N','GAC':'D',
'UAA':'','CAA':'Q','AAA':'K','GAA':'E',
'UAG':'','CAG':'Q','AAG':'K','GAG':'E',
'UGU':'C','CGU':'R','AGU':'S','GGU':'G',
'UGC':'C','CGC':'R','AGC':'S','GGC':'G',
'UGA':'','CGA':'R','AGA':'R','GGA':'G',
'UGG':'W','CGG':'R','AGG':'R','GGG':'G'}


def translation(rna: str) -> str:
    """Transalates an rna seq using codons
    dictionary. 

    :param rna: Rna sequence
    :return:  Protein sequence
    """
    
    protein = ''

    # create range of idnex every 3 indices
    # Ex: 0, 3, 6, 9
    for item in range(0, len(rna), 3):
        protein += codons[rna[item:item+3]]
    
    return protein


# Open rna seq file and convert it to protein sequence
with open('rosalind_prot.txt', 'r') as f:
    rna_seq = f.readline().strip()
    print(translation(rna_seq))
