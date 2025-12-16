import re



with open('rosalind_gc (1).txt', 'r') as f:
   
    # format data
    rosalind = []
    genes = []
    gene_accumulator = ''
    rosalind.append(f.readline().strip('>').strip())
   
    for line in f:
        line = line.strip()
        if 'Rosalind' in line:
            rosalind.append(line)
            genes.append(gene_accumulator)
            gene_accumulator = ''
         
        else:
            gene_accumulator += line
    genes.append(gene_accumulator)

    gc_contents = []
    for gene in genes:
        length_of_gene = len(gene)
        gc_content = gene.count('G') + gene.count('C')
        gc_contents.append(gc_content/length_of_gene * 100) 

    max_index = gc_contents.index(max(gc_contents))

    print(rosalind[max_index])
    print(gc_contents[max_index])
    print(gc_contents)
      
