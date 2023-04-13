#факториал
def factiorial(n: int):
    assert n >= 0, "Факториал отр. неопределен"
    if n == 0:
        return 1
    return factiorial(n-1) * n

# print(factiorial(5))

#Алгоритрм Евклида
def gcd(a, b):
    return (a if b == 0 else gcd(b, a % b))

# print(gcd(10, 16))

#быстрое возведение в степень
def pow(a: float, n: int):
    if n == 0:
        return 1
    elif n % 2 == 1: # нечетное
        return pow(a, n - 1) * a
    else: # n - четное
        return pow(a ** 2, n // 2)

# генерация перестановок
def gen_bin(M, prefix=""):
    if M == 0:
        print(prefix)
        return
    for digit in "0", "1":
         gen_bin(M-1, prefix+digit)

def generate_number(N:int, M:int, prefix=None):
    """ Генерирует все числа (с лидирующими нулями) в N-ричной системе счисления (N <= 10) длины M """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_number(N, M-1, prefix)
        prefix.pop()


# generate_number(3, 4)  # для произвольной СС
# gen_bin(3)  # для двоичной СС

def find(number, A):
    """ Ищет number в A и возвращает True, если такой есть
        False, если такого нет
    """
    for x in A:
        if number == x:
            return True
    return False


def generate_permutations(N:int, M:int=-1, prefix=None):
    """ Функция генерирует перестановки N чисел в M позициях,
    с префиксом prefix
    """
    M = N if M == -1 else M  # по умолчанию N чисел в N позициях
    prefix = prefix or []
    if M == 0:
        print(*prefix)
        return
    for number in range(1, N + 1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M - 1, prefix)
        prefix.pop()

# generate_permutations(3)

