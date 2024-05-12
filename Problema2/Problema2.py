def Problema2(attrezzatture, K):
    giorni = max(attrezzatture, key=lambda x: x[3])[3]
    totale = 0
    for i in range(1, giorni + 1):
        costoGiorno = 0
        for j in range(0, len(attrezzatture)):
            if i >= attrezzatture[j][2] and i <= attrezzatture[j][3]:
                costoGiorno += attrezzatture[j][1]
        if costoGiorno < K:
            totale += costoGiorno
        else:
            totale += K
    return totale


print(
    Problema2(
        [
            ["MARTELLONE", 10, 1, 3],
            ["TRAPANO", 5, 1, 5],
            ["SEGACCIO", 3, 4, 7],
            ["MARTELLONE", 10, 5, 10],
        ],
        15,
    )
)
