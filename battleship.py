

def can_fit(max_ship_size, board_size, board):

    # Check horizontal orientation
    for current_row in range(board_size):

        for start_column in range(board_size - max_ship_size + 1):

            ship_fits = True
            end_column = start_column + max_ship_size - 1

            for current_column in range(start_column, end_column):
                if board[current_row][current_column] == '-':
                    ship_fits = False

            if ship_fits:
                return (start_column, current_row)

    # Check vertical orientation
    for current_column in range(board_size):

        for start_row in range(board_size - max_ship_size + 1):

            ship_fits = True
            end_row = start_row + max_ship_size - 1

            for current_row in range(start_row, end_row):
                if board[current_row][current_column] == '-':
                    ship_fits = False

            if ship_fits:
                return (current_column, start_row)


