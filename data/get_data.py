import re
GENOME = 'href\=\"(.*genomic.fa.gz)\"'
ANNOTATIONS = 'href\=\"(.*annotations.gff3.gz)\"'
PROTEINS = 'href\=\"(.*protein.fa.gz)\"'

with open('wormbase_downloads.html', 'r') as infile:
	read_data = infile.read()	

genome_files = re.findall(GENOME, read_data)
annotation_files = re.findall(ANNOTATIONS, read_data)
protein_files = re.findall(PROTEINS, read_data)

with open('./genomes/genomes.txt', 'w') as outfile:
	outfile.write('\n'.join(genome_files) + '\n')

with open('./annotations/annotations.txt', 'w') as outfile:
	outfile.write('\n'.join(annotation_files) + '\n')

with open('./proteins/proteins.txt', 'w') as outfile:
	outfile.write('\n'.join(protein_files) + '\n')
