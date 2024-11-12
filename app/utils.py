import re

def is_mutant(dna):
    n = len(dna)
    if any(len(row) != n for row in dna):
        raise ValueError("La matriz debe ser NxN.")
    if not all(re.fullmatch(r"[ATCG]+", row) for row in dna):
        raise ValueError("La matriz contiene caracteres no válidos.")
    
    def check_sequence(x, y, dx, dy):
        letter = dna[x][y]
        count = 0
        for _ in range(4):
            if 0 <= x < n and 0 <= y < n and dna[x][y] == letter:
                count += 1
                x += dx
                y += dy
            else:
                break
        return count == 4
    
    sequences_found = 0
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    for i in range(n):
        for j in range(n):
            for dx, dy in directions:
                if check_sequence(i, j, dx, dy):
                    sequences_found += 1
                    if sequences_found > 1:
                        return True
    return False
