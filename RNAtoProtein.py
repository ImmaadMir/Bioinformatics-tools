#Basic program that converts an RNA strand to a protein

#Insert your own file into inputfile
inputfile ="" 
f = open(inputfile, "r") 
seq = f.read() 
seq = seq.replace("\n", "")  
seq = seq.replace("\r", "")

def translate(seq):
	RNA_codon_table = {
	# U
	'UUU': 'F', 'UCU': 'S', 'UAU': 'Y', 'UGU': 'C', # UxU
	'UUC': 'F', 'UCC': 'S', 'UAC': 'Y', 'UGC': 'C', # UxC
	'UUA': 'L', 'UCA': 'S', 'UAA': 'stop', 'UGA': 'stop', # UxA
	'UUG': 'L', 'UCG': 'S', 'UAG': 'stop', 'UGG': 'W', # UxG
	# C
	'CUU': 'L', 'CCU': 'P', 'CAU': 'H', 'CGU': 'R', # CxU
	'CUC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R', # CxC
	'CUA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R', # CxA
	'CUG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R', # CxG
	# A
	'AUU': 'I', 'ACU': 'T', 'AAU': 'N', 'AGU': 'S', # AxU
	'AUC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S', # AxC
	'AUA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R', # AxA
	'AUG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R', # AxG
	# G
	'GUU': 'V', 'GCU': 'A', 'GAU': 'D', 'GGU': 'G', # GxU
	'GUC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G', # GxC
	'GUA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G', # GxA
	'GUG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'  # GxG
	}

# singleletter = {'Cys': 'C', 'Asp': 'D', 'Ser': 'S', 'Gln': 'Q', 'Lys': 'K',
# 'Trp': 'W', 'Asn': 'N', 'Pro': 'P', 'Thr': 'T', 'Phe': 'F', 'Ala': 'A',
# 'Gly': 'G', 'Ile': 'I', 'Leu': 'L', 'His': 'H', 'Arg': 'R', 'Met': 'M',
# 'Val': 'V', 'Glu': 'E', 'Tyr': 'Y', '---': '*'}
	protein = ''
	if len(seq)%3 == 0: 
		for i in range(0, len(seq), 3): 
			codon = seq[i:i + 3] 
			protein+= RNA_codon_table[codon] 
		print(protein) 

translate(seq)