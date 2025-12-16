with open('codons.txt', 'r') as f, \
     open('new_codons.txt', 'w') as f1:
    new_document = ''
    for line in f:
        parts = line.strip().split(' ')
        f1.write(
            f"'{parts[0]}':'{parts[1]}',"
            f"'{parts[7]}':'{parts[8]}',"
            f"'{parts[14]}':'{parts[15]}',"
            f"'{parts[21]}':'{parts[22]}',\n")

    


