import random
import keyboard

sign = lambda a: ((a>0)-(a<0))
transpose= lambda m: [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def arrange(matrix, num, lor):
    row=matrix[num]
    if(lor==1):
        resrow=[]
        for i in range(1,4):
            if(row[i]!=0 and row[i]==row[i-1]):
                resrow.append(row[i]+1)
                row[i]=0;
        matrix[num]=resrow

    elif(lor==-1):
        resrow=[0]*4
        elem=-1
        for i in range(-2,1):
            if(row[i]!=0 and row[i]==row[i+1]):
                resrow[elem]=row[i]+1
                elem-=1
                row[i]=0;
        matrix[num]=resrow
    
    return matrix
class GameBoard:
    def __init__(self):
        self.matrix=[]
        for i in range(4):
            self.matrix.append([0,0,0,0])

    def generate_initial(self):
        (r1, c1)= (random.randint(0,3), random.randint(0,3))
        (r2, c2)= (random.randint(0,3), random.randint(0,3))
        while(r1==r2 and c1==c2):
            (r2, c2)= (random.randint(0,3), random.randint(0,3))

        (self.matrix[r1][c1], self.matrix[r2][c2])= random.choices([1,2], weights=(9,1), k=2)

    def regenrerate(self):
        empties=[]
        for i in range(4):
            for j in range(4):
                if(self.matrix[i][j]==0):
                    empties.append((i,j))
        (p1, p2)= random.choices(empties)
        self.matrix[p1][p2]=random.choices([1,2], weights=(9,1))

    def rearrange_rows(self, lor):
        for i in range(3):
            self.matrix= arrange(self.matrix,i, lor)

    def rearrange_col(self, lor):
        mat=transpose(self.matrix)
        for i in range(3):
            self.matrix=transpose(arrange(mat,i, lor))

    def printmatrix(self):
        for i in range(3):
            print(self.matrix[i], "\n")