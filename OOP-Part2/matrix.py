class Matrix:
    def __init__(self, data):
        self.data = [row[:] for row in data]

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])

    def size(self):
        return len(self.data), len(self.data[0])

    def __add__(self, other):
        if self.size() != other.size():
            raise ValueError("Matrices must be the same size to add them")
        result = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[0])):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Matrix(result)

    def __mul__(self, other):
        if len(self.data[0]) != len(other.data):
            raise ValueError("Matrices cannot be multiplied due to incompatible sizes")
        rows_self, cols_self = self.size()
        rows_other, cols_other = other.size()
        result = []
        for i in range(rows_self):
            row = []
            for j in range(cols_other):
                dot_product = sum([self.data[i][k] * other.data[k][j] for k in range(cols_self)])
                row.append(dot_product)
            result.append(row)
        return Matrix(result)

    __rmul__ = __mul__


class SquareMatrix(Matrix):
    def __pow__(self, power):
        if not isinstance(power, int):
            raise TypeError("Exponent must be an integer")
        if power < 0:
            raise ValueError("Exponent must be non-negative")
        if power == 0:
            # Return identity matrix if exponent is zero
            rows, cols = self.size()
            return SquareMatrix.identity(rows)
        elif power == 1:
            # Return the matrix if exponent is one
            return self
        else:
            # Compute the matrix raised to the power using matrix multiplication
            result = self
            for i in range(1, power):
                result = result * self
            return result

    @staticmethod
    def identity(size):
        # Create an identity matrix of the given size
        data = [[0] * size for _ in range(size)]
        for i in range(size):
            data[i][i] = 1
        return SquareMatrix(data)


m = SquareMatrix([[1, 0], [0, 1]])
print(isinstance(m, Matrix))
m = SquareMatrix([[1, 1], [0, 1]])
print(m ** 0)
print(m ** 2)