
def counter(letter: str, input: str):

    count = 0 
    print(input)
    for line in input:
        print(line)
        if letter == line:
            count += 1
    return count
            
with open('rosalind_dna (3).txt', 'r') as file:
    data = file.readline()
    print(f'{counter('A', data)} {counter('C', data)} {counter('G', data)} {counter('T', data)}')