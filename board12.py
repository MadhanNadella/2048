import random
# import deque from collections

maxindex=2048
sign = lambda a: ((a>0)-(a<0))
transpose= lambda m: [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def power(list): 
    
    return [2**number if number>0 else 0 for number in list]

def arrange(row, lor):
    isadd=0
    retrow=[0]*4
    ismax=0
    if(lor==1):
        ran=range(4)
        elem=0
        last=3
    elif(lor==-1):
        ran=range(-1,-5,-1)
        elem=-1
        last=-4
    for i in ran:
        if(row[i]!=0):
            if(isadd==0):
                isadd=row[i]
            elif(isadd==row[i]):
                retrow[elem]=isadd+1
                if(retrow[elem]==maxindex):
                    ismax=1
                isadd=0
                elem+=lor

            elif(isadd!=0 and row[i]!=isadd):
                retrow[elem]=isadd
                isadd=row[i]
                elem+=lor

    if(elem!=last+lor):
        retrow[elem]=isadd

    return retrow, ismax

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
        try:
            (p1, p2)= random.choices(empties)[0]
        except:
            pass
        self.matrix[p1][p2]=random.choices([1,2], weights=(9,1))[0]

    def rearrange_rows(self, lor):
        ismax=0
        for i in range(4):
            temp=ismax
            self.matrix[i],ismax = arrange(self.matrix[i], lor)
            ismax=max(ismax, temp)

        return ismax

    def rearrange_cols(self, lor):
        ismax=0
        mat=transpose(self.matrix)
        for i in range(4):
            temp=ismax
            mat[i], ismax =arrange(mat[i], lor)
            ismax=max(ismax, temp)
        self.matrix=transpose(mat)

        return ismax

    def printmatrix(self):
        for i in range(4):
            print(power(self.matrix[i]))