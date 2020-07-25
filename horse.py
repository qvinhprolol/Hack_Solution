global size
size = 5
board1 =[[0 for i in range(size)] for j in range(size)]
def validsquare(board,row,col):
    valid = [0 for i in range(8)] #ma di len, trai, xuong, phai
    if row > 1 and col > 0: # len 2 trai 1
        if board[row-2][col-1] == 0:
            valid[0] = 1
    if row > 1 and col < size-1: # len 2 phai 1
        if board[row-2][col+1] == 0:
            valid[1] = 1
    if row > 0 and col > 1: # trai 2 len 1
        if board[row-1][col-2] == 0:
            valid[2] = 1
    if row < size-1 and col > 1: # trai 2 xuong 1
        if board[row+1][col-2] == 0:
            valid[3] = 1
    if row < size-2 and col > 0: # xuong 2 trai 1
        if board[row+2][col-1] == 0:
            valid[4] = 1
    if row < size-2 and col < size-1: # xuong 2 phai 1
        if board[row+2][col+1] == 0:
            valid[5] = 1
    if row > 0 and col < size-2: # phai 2 len 1
        if board[row-1][col+2] == 0:
            valid[6] = 1
    if row < size-1 and col < size-2: # phai 2 xuong 1
        if board[row+1][col+2] == 0:
            valid[7] = 1
    return(valid)

def knight(board,row,col,path=None):
    if path == None:
        board[row][col] = 1
        path = [(row,col)]
    if board == [[1 for i in range(size)] for j in range(size)]:
        print(path)
    if validsquare(board,row,col) != [0 for i in range(8)]:
        if validsquare(board1,row,col)[0] == 1:
            path.append((row-2,col-1))
            board[row-2][col-1] = 1
            knight(board,row-2,col-1,path)
            board[row-2][col-1] = 0
            path.pop()
        if validsquare(board1,row,col)[1] == 1:
            path.append((row-2,col+1))
            board[row-2][col+1] = 1
            knight(board,row-2,col+1,path)
            board[row-2][col+1] = 0
            path.pop()
        if validsquare(board1,row,col)[2] == 1:
            path.append((row-1,col-2))
            board[row-1][col-2] = 1
            knight(board,row-1,col-2,path)
            board[row-1][col-2] = 0
            path.pop()
        if validsquare(board1,row,col)[3] == 1:
            path.append((row+1,col-2))
            board[row+1][col-2] = 1
            knight(board,row+1,col-2,path)
            board[row+1][col-2] = 0
            path.pop()
        if validsquare(board1,row,col)[4] == 1:
            path.append((row+2,col-1))
            board[row+2][col-1] = 1
            knight(board,row+2,col-1,path)
            board[row+2][col-1] = 0
            path.pop()
        if validsquare(board1,row,col)[5] == 1:
            path.append((row+2,col+1))
            board[row+2][col+1] = 1
            knight(board,row+2,col+1,path)
            board[row+2][col+1] = 0
            path.pop()
        if validsquare(board1,row,col)[6] == 1:
            path.append((row-1,col+2))
            board[row-1][col+2] = 1
            knight(board,row-1,col+2,path)
            board[row-1][col+2] = 0
            path.pop()
        if validsquare(board1,row,col)[7] == 1:
            path.append((row+1,col+2))
            board[row+1][col+2] = 1
            knight(board,row+1,col+2,path)
            board[row+1][col+2] = 0
            path.pop()
    return(path)

knight(board1,0,0)