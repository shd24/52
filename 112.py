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
        r = []
        for j in range(size):
            value = get_integer_input(f"Введите элемент для позиции ({i + 1}, {j + 1}): ")
            r.append(value)
        matrix.append(r)
    return matrix

def is_local_minimum(matrix, i, j):
    value = matrix[i][j]
    n = []
    if i > 0:
        n.append(matrix[i - 1][j])
    if i < len(matrix) - 1:
        n.append(matrix[i + 1][j])
    if j > 0:
        n.append(matrix[i][j - 1])
    if j < len(matrix) - 1:
        n.append(matrix[i][j + 1])
    for neighbor in n:
        if value >= neighbor:
            return False
    return True
def count_local_minima(matrix):
    count = 0
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if is_local_minimum(matrix, i, j):
                count += 1
    return count
def main():
    size = 10
    matrix = create_matrix(size)
    print("Ваша матрица:")
    for row in matrix:
        print(' '.join(map(str, row)))
    local_minima_count = count_local_minima(matrix)
    print(f"Количество локальных минимумов в матрице: {local_minima_count}")
main()