'''
Created on Jun 24, 2016

@author: Escobar
Code used for HackerRank Challenge
'''


def graphConstructor() :
    graphData = input().split()
    numNodes = int(graphData[0])
    numEdges = int(graphData[1])
    
    graph = {}
    
    for i in range(1,numNodes+1) :
        graph[i] = set()
    
    for i in range(numEdges) :
        rawEdge = input().split()
        graph[int(rawEdge[0])].add(int(rawEdge[1]))
        graph[int(rawEdge[1])].add(int(rawEdge[0]))
    
    return graph

def bfsDistance(graph, start) :
    
    distance = {}
    parent = {}
    testDistance ={}
    
    for i in range(1,len(graph)+1) :
        distance[i] = 0
        parent[i] = 0
        testDistance[i] = 0
    
    Q = list()  
    
    distance[start] = 0
    Q.append(start)
    
    while len(Q) is not 0 :
        current = Q.pop()
        
        for j in graph[current] :
            testDistance[j] = distance[current] + 6
            
            if((testDistance[j] < distance[j]) | (distance[j] == 0)) :
                distance[j] = testDistance[j]
                parent[j] = current
                Q.append(j)
                
    return distance     


testCases = int(input())

for i in range(testCases) :
    graph = graphConstructor()
    startNode = int(input())
    distance = bfsDistance(graph, startNode)
      
    distanceResult = list()
    
    for i in range(1,len(distance)+1) :
        if(i != startNode) :
            if(distance[i] != 0) :
                distanceResult.append(distance[i])
            else :
                distanceResult.append(-1)
                
    print(" ".join(map(str,distanceResult)))
    