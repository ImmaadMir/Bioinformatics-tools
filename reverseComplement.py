#Basic program to find the reverse complement of a DNA seq

#Enter DNA seq at dna
dna = ''
rev = ''
for c in dna:
    if c == 'A':
        rev = 'T' + rev
    elif c == 'C':
        rev = 'G' + rev
    elif c == 'G':
        rev = 'C' + rev
    elif c == 'T':
        rev = 'A' + rev
print rev
