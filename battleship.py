

def calc_cell_score(left, right):

    score = 0

    score += calc_ship_score(2, left, right)
    score += calc_ship_score(2, left, right)
    score += calc_ship_score(3, left, right)
    score += calc_ship_score(4, left, right)
    score += calc_ship_score(5, left, right)

    return score


def calc_ship_score(ship_size, left, right):

    open_cells = left + 1 + right

    score = open_cells - ship_size + 1

    # Score cannot be larger than (the minimum of left or right) plus 1
    if score > min(left, right) + 1:
        score = min(left, right) + 1

    # Score cannot be larger than the ship_size
    if score > ship_size:
        score = ship_size

    # Score is zero if the ship doesn't fit
    if ship_size == open_cells:
        score = 1

    # Score is zero if the ship doesn't fit
    if ship_size > open_cells:
        score = 0

    return score


print(calc_cell_score(0, 0))
print(calc_cell_score(0, 1))
print(calc_cell_score(0, 2))
print(calc_cell_score(0, 3))
print(calc_cell_score(0, 4))
print(calc_cell_score(1, 0))
print(calc_cell_score(1, 1))
print(calc_cell_score(1, 2))
print(calc_cell_score(1, 3))
print(calc_cell_score(1, 4))
print(calc_cell_score(2, 0))
print(calc_cell_score(2, 1))
print(calc_cell_score(2, 2))
print(calc_cell_score(2, 3))
print(calc_cell_score(2, 4))
print(calc_cell_score(3, 0))
print(calc_cell_score(3, 1))
print(calc_cell_score(3, 2))
print(calc_cell_score(3, 3))
print(calc_cell_score(3, 4))
print(calc_cell_score(4, 0))
print(calc_cell_score(4, 1))
print(calc_cell_score(4, 2))
print(calc_cell_score(4, 3))
print(calc_cell_score(4, 4))

"""
print('Fives')
print(calc_ship_score(5, 0, 0))
print(calc_ship_score(5, 0, 1))
print(calc_ship_score(5, 0, 2))
print(calc_ship_score(5, 0, 3))
print(calc_ship_score(5, 0, 4))
print(calc_ship_score(5, 1, 0))
print(calc_ship_score(5, 1, 1))
print(calc_ship_score(5, 1, 2))
print(calc_ship_score(5, 1, 3))
print(calc_ship_score(5, 1, 4))
print(calc_ship_score(5, 2, 0))
print(calc_ship_score(5, 2, 1))
print(calc_ship_score(5, 2, 2))
print(calc_ship_score(5, 2, 3))
print(calc_ship_score(5, 2, 4))
print(calc_ship_score(5, 3, 0))
print(calc_ship_score(5, 3, 1))
print(calc_ship_score(5, 3, 2))
print(calc_ship_score(5, 3, 3))
print(calc_ship_score(5, 3, 4))
print(calc_ship_score(5, 4, 0))
print(calc_ship_score(5, 4, 1))
print(calc_ship_score(5, 4, 2))
print(calc_ship_score(5, 4, 3))
print(calc_ship_score(5, 4, 4))

print('Fours')
print(calc_ship_score(4, 0, 0))
print(calc_ship_score(4, 0, 1))
print(calc_ship_score(4, 0, 2))
print(calc_ship_score(4, 0, 3))
print(calc_ship_score(4, 0, 4))
print(calc_ship_score(4, 1, 0))
print(calc_ship_score(4, 1, 1))
print(calc_ship_score(4, 1, 2))
print(calc_ship_score(4, 1, 3))
print(calc_ship_score(4, 1, 4))
print(calc_ship_score(4, 2, 0))
print(calc_ship_score(4, 2, 1))
print(calc_ship_score(4, 2, 2))
print(calc_ship_score(4, 2, 3))
print(calc_ship_score(4, 2, 4))
print(calc_ship_score(4, 3, 0))
print(calc_ship_score(4, 3, 1))
print(calc_ship_score(4, 3, 2))
print(calc_ship_score(4, 3, 3))
print(calc_ship_score(4, 3, 4))
print(calc_ship_score(4, 4, 0))
print(calc_ship_score(4, 4, 1))
print(calc_ship_score(4, 4, 2))
print(calc_ship_score(4, 4, 3))
print(calc_ship_score(4, 4, 4))

print('Threes')
print(calc_ship_score(3, 0, 0))
print(calc_ship_score(3, 0, 1))
print(calc_ship_score(3, 0, 2))
print(calc_ship_score(3, 0, 3))
print(calc_ship_score(3, 0, 4))
print(calc_ship_score(3, 1, 0))
print(calc_ship_score(3, 1, 1))
print(calc_ship_score(3, 1, 2))
print(calc_ship_score(3, 1, 3))
print(calc_ship_score(3, 1, 4))
print(calc_ship_score(3, 2, 0))
print(calc_ship_score(3, 2, 1))
print(calc_ship_score(3, 2, 2))
print(calc_ship_score(3, 2, 3))
print(calc_ship_score(3, 2, 4))
print(calc_ship_score(3, 3, 0))
print(calc_ship_score(3, 3, 1))
print(calc_ship_score(3, 3, 2))
print(calc_ship_score(3, 3, 3))
print(calc_ship_score(3, 3, 4))
print(calc_ship_score(3, 4, 0))
print(calc_ship_score(3, 4, 1))
print(calc_ship_score(3, 4, 2))
print(calc_ship_score(3, 4, 3))
print(calc_ship_score(3, 4, 4))

print('Twos')
print(calc_ship_score(2, 0, 0))
print(calc_ship_score(2, 0, 1))
print(calc_ship_score(2, 0, 2))
print(calc_ship_score(2, 0, 3))
print(calc_ship_score(2, 0, 4))
print(calc_ship_score(2, 1, 0))
print(calc_ship_score(2, 1, 1))
print(calc_ship_score(2, 1, 2))
print(calc_ship_score(2, 1, 3))
print(calc_ship_score(2, 1, 4))
print(calc_ship_score(2, 2, 0))
print(calc_ship_score(2, 2, 1))
print(calc_ship_score(2, 2, 2))
print(calc_ship_score(2, 2, 3))
print(calc_ship_score(2, 2, 4))
print(calc_ship_score(2, 3, 0))
print(calc_ship_score(2, 3, 1))
print(calc_ship_score(2, 3, 2))
print(calc_ship_score(2, 3, 3))
print(calc_ship_score(2, 3, 4))
print(calc_ship_score(2, 4, 0))
print(calc_ship_score(2, 4, 1))
print(calc_ship_score(2, 4, 2))
print(calc_ship_score(2, 4, 3))
print(calc_ship_score(2, 4, 4))
"""



