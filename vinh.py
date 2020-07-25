charboard = [
    ['V','i','n','h'],
    ['i','n','h','*'],
    ['n','h','*','*'],
    ['h','*','*','*']
]
width = len(charboard)
length = len(charboard[0])
target = ['V','i','n','h']
def checkmove(char,board,row,col):
    moves = [0,0,0,0] # len trai xuong phai
    if row > 0: # len
        if charboard[row-1][col] == char:
            moves[0] = 1
    if col > 0: # trai
        if charboard[row][col-1] == char:
            moves[1] = 1
    if row < width-1: # xuong
        if charboard[row+1][col] == char:
            moves[2] = 1
    if col < length-1: # phai
        if charboard[row][col+1] == char:
            moves[3] = 1
    return(moves)

def strvinh(board,row=0,col=0,i=1,path=[(0,0)]):
    if i == 4:
        print(path)
        return
    if checkmove(target[i],board,row,col) != [0,0,0,0]:
        if checkmove(target[i],board,row,col)[0] == 1:
            path.append((row-1,col))
            strvinh(board,row-1,col,i+1,path)
            path.pop()
        if checkmove(target[i],board,row,col)[1] == 1:
            path.append((row,col-1))
            strvinh(board,row,col-1,i+1,path)
            path.pop()
        if checkmove(target[i],board,row,col)[2] == 1:
            path.append((row+1,col))
            strvinh(board,row+1,col,i+1,path)
            path.pop()
        if checkmove(target[i],board,row,col)[3] == 1:
            path.append((row,col+1))
            strvinh(board,row,col+1,i+1,path)
            path.pop()
    return(path)

strvinh(charboard)