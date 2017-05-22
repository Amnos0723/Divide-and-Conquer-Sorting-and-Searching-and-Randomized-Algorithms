# Hello World program in Python
 
import random   

def minCut(graphDic):
    if len(list(graphDic.keys()))==1:
        for vert in list(graphDic.keys()):
            try:
                graphDic[vert].remove(vert)
            except ValueError:
                pass
        return graphDic
        
    else:
        vert1=random.choice(list(graphDic.keys()))
        vert2=random.choice(graphDic[vert1])
        print(vert1,vert2)
        for vert in graphDic[vert1]:
            for i in range(0,len(graphDic[vert])):
                if graphDic[vert][i]==vert1: graphDic[vert][i]=vert2
        del graphDic[vert1]
        print(graphDic)
        return minCut(graphDic)
        
graphDic={1:[2,3,5],2:[1,3,4],3:[1,2,4],4:[2,3],5:[1]}

print(minCut(graphDic))

'''
vert1=3
vert2=2
for vert in graphDic[vert1]:
    for i in range(0,len(graphDic[vert])):
        if graphDic[vert][i]==vert1: graphDic[vert][i]=vert2
del graphDic[vert1]       
print(vert1,vert2,graphDic)

for i in range(0,100000):
    minCut(graphDic)
'''     
