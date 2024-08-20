def generate_sequence(n):
    sequence = []
    num = 1
    while len(sequence) < n:
        sequence.extend([num] * num)
        num += 1
    return sequence[:n]

if __name__ == "__main__":
    n = int(input("Введите количество элементов: "))
    result = generate_sequence(n)
    print(" ".join(map(str, result)))
