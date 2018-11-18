import sys
d={}

def parse_Fastafile(filename):
    with open(filename,'r')as file:
        for line in file:
            if line[0]=='>':
                header=line.strip()[1:]
                d[header]=[]
            else:
                d[header].append(line.strip())

        for key,value in d.items():
             d[key]=''.join(value)
    return d


dic=parse_Fastafile(sys.argv[1])
for id,num in dic.items():
    A=num.count('A')
    T=num.count('T')
    G=num.count('G')
    C=num.count('C')
    gc_content=float(G+C)/float(A+T+C+G)*100
    dic[id]=gc_content
print(dic)

print(max(dic,key=dic.get))
print(dic[max(dic,key=dic.get)])










