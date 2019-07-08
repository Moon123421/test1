x = input('Nucleotide: ')

def nucleotide(a):
    dic = {'A':'Adenine','C':'Cytosine','G':'Guanine','T':'Thymine','U':'Uracil'}
    return dic.get(a)

print(nucleotide(x))

