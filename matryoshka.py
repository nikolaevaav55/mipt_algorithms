def matryoshka(n):
    if n == 1:
        print("matryoshka")
    else:
        print("Верх матрешки n=", n - 1)
        matryoshka(n-1)
        print("Низ матрешки n=", n - 1)

matryoshka(4)