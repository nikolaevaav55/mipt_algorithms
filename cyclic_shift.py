def cyclic_shift_left(A:list, N:int):
    tmp = A[0]
    for k in range(N-1):
        A[k] = A[k+1]
    A[N-1] = tmp
    return A

def cyclic_shift_right(A: list, N: int):
    tmp = A[N-1]
    for k in range(N - 2, -1, -1):
        A[k + 1] = A[k]
    A[0] = tmp
    return A

A = [0, 1, 2, 3, 4, 5]
B = [0, 1, 2, 3, 4, 5]

print(cyclic_shift_right(A, 6))
print(cyclic_shift_left(B, 6))

