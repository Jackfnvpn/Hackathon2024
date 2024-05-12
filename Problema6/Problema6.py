def Problema6(m, buffet):
    max = 0
    d = {}
    numero_portate = 0
    for i in range(0, m):
        if buffet[i] not in d:
            d[buffet[i]] = 1
            numero_portate += 1
        else:
            d[buffet[i]] += 1

    for i in range(m, len(buffet)):
        if buffet[i] not in d:
            d[buffet[i]] = 1
        else:
            d[buffet[i]] += 1

        if d[buffet[i]] == 1:
            numero_portate += 1

        d[buffet[i - m]] -= 1
        if d[buffet[i - m]] == 0:
            numero_portate -= 1
        if numero_portate == m:
            max = numero_portate
            break
        elif numero_portate > max:
            max = numero_portate

    return max


print(
    Problema6(
        3,
        [
            "lasagna",
            "lasagna",
            "cannelloni",
            "salsiccia",
            "lasagna",
            "cannelloni",
            "lasagna",
        ],
    )
)
