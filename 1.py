class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Матриці не однакового розміру")
        result = [[0 for _ in range(len(self.matrix[0]))] for _ in range(len(self.matrix))]
        
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(result)
        
    def __sub__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Матриці не однакового розміру")
        result = [[0 for _ in range(len(self.matrix[0]))] for _ in range(len(self.matrix))]
        
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return Matrix(result)
        
    def __mul__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError("Матриці нек множаться")
        res = [[0 for _ in range(len(other.matrix[0]))] for _ in range(len(self.matrix))]
        
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[0])):
                for k in range(len(self.matrix[0])):
                    res[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix(res)
matrix1=Matrix([[5,4], [7,9]])
matrix2=Matrix([[3,1], [2,5]])
matrix3=matrix1+matrix2
matrix4=matrix1-matrix2
matrix5=matrix1*matrix2
print("Додавання")
print(matrix3)
print("Віднімання")
print(matrix4)
print("Множення")
print(matrix5)