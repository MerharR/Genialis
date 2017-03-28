import csv

data=list()
with open('pathways.txt') as f:
    reader=csv.reader(f, delimiter='.')
    #data=list(reader)
    for row in reader:
        data.append(row)

my_paths=list()
for j in range(0, len(data)):
    data1=list()
    pod=str()
    for i in range(len(data[j][-1])):
        if data[j][-1][i]!='\t':
            pod= pod + str(data[j][-1][i])
        if data[j][-1][i] == '\t':
            data1=data1 + [pod]
            pod=str()
    data1=data1 + [pod]
    data1=data1[1:len(data)]
    my_paths=my_paths + [data1]

data2=list()

with open('leukemia.txt') as g:
    reader=csv.reader(g, delimiter='\t')
    for row in reader:
        data2.append(row)
        
#set S are paths in my_paths, set L is data2

#we still have to determine parameter p, which controls the weight of the step, lets assume p=1
p=1

#N=number of genes in data2
#N_H=number of genes in one path

ES=list()
N=len(data2)-1

for x in range(0, len(my_paths)):
    N_R=0
    P_hit=0
    P_miss=0
    vs=list()
    N_H=len(data2[0])-1
    for i in range(0, len(my_paths[x])):
        for j in range(1, len(data2)):
            if len(my_paths[x]) <73:
                if my_paths[x][i]==data2[j][0]:
                    N_R=N_R + int(data2[j][i+1])
    for k in range(0, len(my_paths[x])):
        if len(my_paths[x]) <73:
            for m in range(1,len(data2)):
                if my_paths[x][k]==data2[m][0]:
                    if N_R!=0:
                        P_hit=P_hit + int(data2[m][k+1])/N_R
                if my_paths[x][k]!= data2[m][0]:
                    P_miss = P_miss + 1/(N-N_H)
                    #print(P_hit-P_miss)
            vs=vs+ [abs(P_hit-P_miss)]
    if vs!=list():
        ES=ES + [max(vs)]
