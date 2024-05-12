from Pila import Pila


def Problema4(grid):
    max_area = 0

    pila = Pila()

    def is_valid(r, c):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0])

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                temp_max = 0
                pila.push((r, c))
                while not pila.isEmpty():
                    u, v = pila.pop()
                    if is_valid(u, v) and grid[u][v] != 0:
                        temp_max += 1
                        grid[u][v] = 0
                        pila.push((u + 1, v))
                        pila.push((u, v + 1))
                        pila.push((u - 1, v))
                        pila.push((u, v - 1))
                    max_area = max(max_area, temp_max)
    return max_area


grid = [[1, 1, 0, 1], [1, 1, 0, 1], [1, 0, 1, 1]]

max_area = Problema4(grid)
print("Massima area di 1 contigua:", max_area)
