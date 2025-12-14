
class origami:
    
    def __init__(self, origamiCoor,AdjacencyMatrix,Creases,layers):
            self.origamiCoor =  origamiCoor
            self.AdjacencyMatrix = AdjacencyMatrix
            self.Creases = Creases
            self.layers = layers

Origami=origami([[0,0], [1,0], [0,1], [1,1]],[[0,-1,1,0],[-1,0,0,-1],[1,0,0,1],[0,-1,1,0]], [[0,2,2,0], [0,0,0,4],[2,0,0,1],[0,4,1,0]],[[0,4,2,0],[4,0,0,4],[2,0,0,1],[0,4,1,0]])

def nodeWeight():
    #initialize variables
    first = 0
    second = 0
    i=0 #cell of origamiCoor, AdjacencyMatrix, and crease
    
    while i<= len(Origami.origamiCoor)-1:
     j=0
     #tracks the sum of all the integers in the cell i of the AdjacencyMatrix
     testCell=0 
     #the sum of all the integers in the cell with the largest sum of the AdjacencyMatrix
     bigCell=0 
     #the sum of all the integers in the cell with the 2nd largest sum of the AdjacencyMatrix
     smallCell=0 
    
     while j<= len(Origami.AdjacencyMatrix[i])-1:
           #checks the weightage of each point
           testCell += Origami.AdjacencyMatrix[i][j]
           bigCell+= Origami.AdjacencyMatrix[first][j]
           smallCell+= Origami.AdjacencyMatrix[second][j]
           j+=1
        
    #replaces the holding largest value and 2nd largest
     if testCell > bigCell:
         second = first
         first = i
     #replaces the second largest value
     if testCell >= smallCell and bigCell >= testCell and Origami.AdjacencyMatrix[i][first] == 1 and Origami.Creases[i][first]==1 :
         second = i
     
    
     
     i+=1
     
     
    #checks the folding 
    
    print(Origami.layers)
    print(first)
    print(second)
    
    
    
    
    
    try:
        #finds slope of crease in plane
        m=(Origami.origamiCoor[first][1]-Origami.origamiCoor[second][1])/(Origami.origamiCoor[first][0]-Origami.origamiCoor[second][0])
        print(m)
        
            self.layers = [[0,4,2,0], [4,0,0,4], [2,0,0,1], [0,4,1,0]]
        
        