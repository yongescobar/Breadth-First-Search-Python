'''
Created on Jun 24, 2016

@author: Escobar
Code used for HackerRank Challenge: https://www.hackerrank.com/challenges/bfsshortreach/submissions/code/22102378
'''

'''
Outputs a graph in form of Dictionary type {vertex : {vertices connected to}} given an input from console of the following format:

First line of each test case has two integers N, denoting the number of nodes in the graph and M, denoting the number of edges in the graph. 
The next  lines each consist of two space separated integers x y, where  and  denote the two nodes between which the edge exists. 
The last line of a testcase has an integer S, denoting the starting position.

Example: 

4 2
1 2
1 3
1

4 vertices and 2 edges
Those 2 edges connect vertex 1 to vertex 2 and vertex 1 to vertex 3
Start from vertex 1
graphConstructor outputs: {1: {2,3}, 2:{1}, 3:{1}, 4: set()}

Note that if a vertex is not connected to any other vertex, then it's value is an empty set
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

'''
Outputs a graph in form of Dictionary type {vertex : {vertices connected to}} given an input from console of the following format:

The first line contains T, denoting the number of test cases. 
First line of each test case has two integers N, denoting the number of nodes in the graph and M, denoting the number of edges in the graph. 
The next  lines each consist of two space separated integers x y, where  and  denote the two nodes between which the edge exists. 
The last line of a testcase has an integer S, denoting the starting position.

Input Example:

2
4 2
1 2
1 3
1
3 1
2 3
2

2 test cases where the first case has the graph {1: {2,3}, 2:{1}, 3:{1}, 4: set()} starting from vertex 1 
and the second case has graph {1: set(), 2: {3}, 3: {2} } starting from vertex 2

Outputs shortest distance from the starting vertex to rest of vertices. Each edge is of length 6. 
If there is no path from the starting vertex to a vertex, then the distance value is -1

Output example of 1st case:

6 6 -1

This means distance between vertex 1 to vertex 2 is 6, to vertex 3 is 6, and there is no path vertex 4. 

'''
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


'''
Note in Eclipse console, if input is entered by paste, the first output gets printed before input reaches its end. 
Simply press "Enter" to resume the rest of the output
'''

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
    