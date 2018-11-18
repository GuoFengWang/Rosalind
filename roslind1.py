with open('/Users/Andy/Desktop/newcancer.expr.txt','r')as file:
    d={}
    con=file.readlines()
    a=con[0].split()[1:]
    b=[i for i in range(1,110)]
    for j,k in zip(a,b):
        d[j]=k
    print(d)

    with open('/Users/Andy/Desktop/map.txt','w')as file:
        for i in a:
            file.write(i+'\t'+str(d[i])+'\n')








