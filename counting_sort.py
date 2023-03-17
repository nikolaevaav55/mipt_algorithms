'''
 `A` ——> the input list of integers to be sorted
 `k` ——> a number such that all integers are in range `0…k-1`
'''


def countsort(A, k):
    # создает целочисленный список размера `n` для хранения отсортированного списка
    output = [0] * len(A)

    # создает целочисленный список размером `k + 1`, инициализированный всеми нулями
    freq = [0] * (k + 1)

    # , используя значение каждого элемента в списке ввода в качестве индекса,
    # сохраняет счетчик каждого целого числа в `freq[]`
    for i in A:
        freq[i] = freq[i] + 1

    # вычисляет начальный индекс для каждого целого числа
    total = 0
    for i in range(k + 1):
        oldCount = freq[i]
        freq[i] = total
        total += oldCount

    # копирует в список выходов, сохраняя порядок входов с одинаковыми ключами
    for i in A:
        output[freq[i]] = i
        freq[i] = freq[i] + 1

    # скопировать список вывода обратно в список ввода
    for i in range(len(A)):
        A[i] = output[i]


if __name__ == '__main__':
    A = [4, 2, 10, 10, 1, 4, 2, 1, 10]

    # диапазон элементов списка
    k = 10

    countsort(A, k)
    print(A)
