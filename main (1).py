import random   

def removeDup(key,lis):
    result=[item for item in lis if item!=key]
    return result
        
    
def minCut(graphDic):
    if len(list(graphDic.keys()))==2:
        return graphDic
    else:
        vert1=random.choice(list(graphDic.keys()))
        vert2=random.choice(graphDic[vert1])
        while vert2==vert1:
            vert2=random.choice(graphDic[vert1])
        ##print(vert1,vert2)
        for vert in graphDic[vert1]:
            graphDic[vert2].append(vert)
            for i in range(0,len(graphDic[vert])):
                if graphDic[vert][i]==vert1: graphDic[vert][i]=vert2
        del graphDic[vert1]
        ##print(graphDic)
        for vert in list(graphDic.keys()):
            graphDic[vert]=removeDup(vert,graphDic[vert])
        ##print(graphDic)
        return minCut(graphDic)

alist = [line.rstrip() for line in open('123.txt')]

graphdic={}
for i in range(len(alist)):
    alist[i]=alist[i].split('\t')
    graphdic[alist[i][0]]=alist[i][1:]
#print(graphDic)
#minCut(graphDic)

result=[]
for i in range(0,1000):
    graphDic=dict(graphdic)
    temp=minCut(graphdic)
    result.append(min([len(temp[key])for key in temp.keys()]))    
print(min(result))
