def Problema1(K):
    count = 0
    for x in range(1, K):
        count += (K - 1) // x
    return count


print(Problema1(5))
