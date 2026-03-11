# Open multi-fasta file
with open('rosalind_cons (2).txt', 'r') as f:
    fastas = []

    # collect fastas 
    string = ''
    for line in f:

        # If line contains '> its a header 
        # len(string) > 0  is so first line is skipped
        if '>' in line and len(string) > 0:
            fastas.append(string) # Add fasta to list
            string = '' # reset string 

        # strip new lines
        line = line.strip()

        # If not header build fasta string
        if '>' not in line:
            string += line
    
    # append last fasta
    fastas.append(string)

# Fill lists with zeros
a = [0 for _ in range(len(fastas[0]))]
c = [0 for _ in range(len(fastas[0]))]
t = [0 for _ in range(len(fastas[0]))]
g = [0 for _ in range(len(fastas[0]))]

# Create a dictionary with each base 
profile = {'A': a, 'C': c, 'T':t, 'G':g}

# Iterate through each fasta 
for fast in fastas:
    index = 0

    # For each letter in the 
    # fasta add it to the profile
    for letter in fast:
        profile[letter][index] += 1
        index += 1

# Build a consensus string
consensus = ''
for i in range(len(fastas[0])):

    # Create dictionary that will hold values for
    # Each base at each position 
    col = {
        'A': a[i],
        'C': c[i],
        'G': g[i],
        'T': t[i]
    }

    # Build consensus string by finding the max value 
    consensus += max(col, key=col.get)

# print results
print(consensus)
print('A:', *profile['A']) # * unpacks list so rosalind doesn't freak out and tell me i'm incorrect
print('C:', *profile['C'])
print('G:', *profile['G'])
print('T:', *profile['T'])

