class NapSack:

    def Calculate_matrix(self,Size,V,W):
        Matrix = []
        temp = [] 
        for x in range(0,Size+1):
            temp.append(0)
        for x in range(0,len(V)+1):
            Matrix.append(temp)
        del(temp)

        for x in Matrix:
            print(x)

        for i in range(1,len(Matrix)):
            for j in range(1,len(Matrix[i])):
                '''remsize = j - V[i-1]
                if(remsize<0):
                    Matrix[i][j] = Matrix[i-1][j]
                else:
                    Matrix[i][j] = max(Matrix[i-1][j],W[i-1]+Matrix[i-1][remsize])
                '''
                Matrix[i][j] = i+j
                print(i,j)
        for x in Matrix:
            print(x)

    def Read_File(self,Filename):
        fi = open(Filename)
        self.Values = []
        self.Weights =[] 
        for x in fi:
            line = x.split(" ")
            self.Values.append(int(line[1]))
            self.Weights.append(int(line[2]))

        print(self.Values)
        print(self.Weights)
            

    def __init__(self):
        self.Read_File("Inp1.txt")
        self.Calculate_matrix(5,self.Values,self.Weights)

temp = NapSack()