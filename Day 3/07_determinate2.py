from sympy import Matrix

# Define the custom determinant function
def determinant(matrix):
    num_rows = len(matrix)
    
    # Check if the matrix is square
    for row in matrix:
        if len(row) != num_rows:
            print("Given matrix is not a square matrix")
            return None
    
    # Base case for 2x2 matrix
    if num_rows == 2:
        simple_determinant = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        return simple_determinant
    
    # Recursive case for larger matrices
    else:
        det = 0
        for i in range(num_rows):
            minor = []
            for j in range(1, num_rows):
                minor_row = []
                for k in range(num_rows):
                    if k != i:
                        minor_row.append(matrix[j][k])
                minor.append(minor_row)
            det += ((-1)**i) * matrix[0][i] * determinant(minor)
        return det

# Convert the sympy Matrix to a list of lists
M = Matrix([[1, 55], [2, 5]]).tolist()

# Print the determinant
print(determinant(M))
