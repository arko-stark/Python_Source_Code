# step 1 : function that prints out a board
def display_board(board):
    line1 = [board[7],'|',board[8],'|',board[9]]
    line2 = ['------']
    line3 = [board[4],'|',board[5],'|',board[6]]
    line4 = ['------']
    line5 = [board[1], '|', board[2], '|', board[3]]
    print(''.join(line1))
    print(''.join(line2))
    print(''.join(line3))
    print(''.join(line4))
    print(''.join(line5))

test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)
