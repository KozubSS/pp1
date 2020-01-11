import random

class matrix():

    @staticmethod
    def create(x,y):
        matrix = []
        value = 0
        for i in range(x):
            # create single row
            row = []
            for j in range(y):
                row.append(value)
            # add row to matrix
            matrix.append(row)
        return matrix

    @staticmethod
    def print(matrix):
        for row in matrix:
            print(row)

    @staticmethod
    def create_unit(x):
         return create_matrix(x, x)
        

    @staticmethod
    def fill_random(matrix, m, n):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = random.randrange(m,n)
        return matrix  
        
        
        
m = matrix.create(4,3)

mm = matrix.fill_random(m, 5, 9)
matrix.print(mm)



