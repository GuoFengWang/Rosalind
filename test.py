import re
import sys
d={}

with open('/Users/Andy/Desktop/Rosalind/rna_condon_table.txt','r')as file:
    for line in file:
        list=re.split('\s+',line.strip())
        for i in [0,2,4,6]:
            d[list[i]]=list[i+1]


seq=''
with open(sys.argv[1],'r')as file:
    for line in file:
        seq=line.strip()


i=0
pro=''
while i < len(seq):
    condon=seq[i:i+3]
    if d[condon] !='Stop':
        pro += d[condon]
    i += 3

with open('/Users/Andy/Desktop/Rosalind/result_pro.txt','w')as file:
    file.write(pro)


