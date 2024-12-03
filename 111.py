def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Пожалуйста, введите целое число.")

def create_matrix(size):
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            value = get_integer_input(f"Введите элемент для позиции ({i + 1}, {j + 1}): ")
            row.append(value)
        matrix.append(row)
    return matrix
def sort(matrix):
    size = len(matrix)
    for i in range(size):
        for j in range(i + 1, size):
            if matrix[0][j] > matrix[0][i]:
                for k in range(size):
                    matrix[k][i], matrix[k][j] = matrix[k][j], matrix[k][i]
def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))
def main():
    M = get_integer_input("Введите размер матрицы M (целое число): ")
    matrix = create_matrix(M)
    print("Исходная матрица:")
    print_matrix(matrix)
    sort(matrix)
    print("Отсортированная матрица:")
    print_matrix(matrix)
main()