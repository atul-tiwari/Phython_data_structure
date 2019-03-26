import numpy as np
class NapSack:

    def path_finding(self):
        limit = self.dirction.shape
        path = []
        backtrack =limit[1]-1
        x = limit[0]-1
        while(x>0):
            direction_val = self.dirction[x,backtrack] 
            if (direction_val =='D'):
                backtrack-=1
                path.append(x)
                x-=1
            elif(direction_val == 'L'):
                backtrack-=1
                print(x,backtrack)
            else :
                x-=1
        temp =[]
        print (path)
        for x in path:
            temp.append("Item "+str(x))
        
        path= temp
        path.append("total weight = "+str(self.base_matrix[limit[0]-1,limit[1]-1]))
        print (path)

    # Creating The Base Matrix 
    def _create(self,Size_of_napsack,noOfItems):

        self.base_matrix = np.array([[0] * (Size_of_napsack+1)]) 
        
        self.dirction = np.array([['O'] * (Size_of_napsack+1)]) 

        for x in range(0,noOfItems):
            current_item = self.Data_mat[x]
            tempArr = []
            tempArr.append(0)
            tempArr_dir = []
            tempArr_dir.append('O')
            for y in range (1,Size_of_napsack+1):
                rem_size = y - current_item[0]
                old_value = max(self.base_matrix[x,y],tempArr[-1])
                if (rem_size >=0 ):
                    new_value = self.Data_mat[x,1]+self.base_matrix[x,rem_size]
                    if(new_value>old_value):
                        tempArr.append(new_value)
                        tempArr_dir.append('D')
                    else:
                        tempArr.append(old_value)
                        tempArr_dir.append('L')
                else:
                    tempArr.append(old_value)
                    tempArr_dir.append('U')

            self.base_matrix = np.append(self.base_matrix,[tempArr],axis=0)
            self.dirction = np.append(self.dirction,[tempArr_dir],axis=0)
        
        print(self.dirction)
        print(self.base_matrix)

    
    # Constructor Class
    def __init__(self,Size_of_napsack,arr_item,arr_weight):

        arr = []
        noOfItems = len(arr_item)
        for x in range(0,noOfItems):
            arr.append([arr_item[x],arr_weight[x]])

        self.Data_mat = np.array(arr)

        print(self.Data_mat)
        self._create(Size_of_napsack,noOfItems)
        self.path_finding()
        
       
size = 10                  # size of napsack
arr_item =    [ 5,4,6,3]  # sapce taking of each Item
arr_weight =  [ 10,40,30,50]  # weight of each item
obj = NapSack(size,arr_item,arr_weight)
