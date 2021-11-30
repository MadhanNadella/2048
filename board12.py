import random

max=12
sign = lambda a: ((a>0)-(a<0))
transpose= lambda m: [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def power(list): 
    return [2**number if number>0 else 0 for number in list]

def arrange(matrix, num, lor):
    row=matrix[num]

    if(lor==1):
        resrow=[]
        ismax=0
        for i in range(1,4):
            if(row[i]!=0 and row[i]==row[i-1]):
                resrow.append(row[i]+1)
                if(row[i]+1==max):
                    ismax=1
                row[i]=0
        matrix[num]=resrow

    elif(lor==-1):
        resrow=[0]*4
        elem=-1
        for i in range(-2,1):
            if(row[i]!=0 and row[i]==row[i+1]):
                resrow[elem]=row[i]+1
                if(row[i]+1==max):
                    ismax=1
                elem-=1
                row[i]=0;
        matrix[num]=resrow
    
    return matrix, ismax
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

    def regenerate(self):
        empties=[]
        for i in range(4):
            for j in range(4):
                if(self.matrix[i][j]==0):
                    empties.append((i,j))
        (p1, p2)= random.choices(empties)
        self.matrix[p1][p2]=random.choices([1,2], weights=(9,1))

    def rearrange_rows(self, lor):
        temp=self.matrix
        for i in range(3):
            self.matrix, ismax = arrange(self.matrix,i, lor)
        if(temp==self.matrix):
            ismax=-1
        return ismax

    def rearrange_cols(self, lor):
        temp=self.matrix
        mat=transpose(self.matrix)
        for i in range(3):
            self.matrix, ismax =transpose(arrange(mat,i, lor))
        if(temp==self.matrix):
            ismax=-1
        return ismax

    def printmatrix(self):
        for i in range(4):
            print(power(self.matrix[i]))