import random
def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Пожалуйста, введите положительное число.")
        except ValueError:
            print("Пожалуйста, введите целое число.")
def random_set(size, range_min, range_max):
    random_set = set()
    while len(random_set) < size:
        random_set.add(random.randint(range_min, range_max))
    return random_set
def main():
    size = get_integer_input("Введите размер каждого множества (максимум 10000): ")
    if size > 10000:
        print("Размер множества не должен превышать 10000.")
        return
    set1 = random_set(size, 1, 10000)
    set2 = random_set(size, 1, 10000)
    i = sorted(set1.intersection(set2))
    print("Числа, которые находятся как в первом, так и во втором множестве (в порядке возрастания):")
    print(i)
main()
