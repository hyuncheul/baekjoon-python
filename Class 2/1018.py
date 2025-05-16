X, Y = map(int, input().split())
board = []
for i in range(X):
    line = list(input())
    board.append(line)

startW = 0
startB = 0

for i in range(X):
    for j in range(Y):
        if (i+j)%2 == 0:
            dot1 = 'W'
            dot2 = 'B'
        else:
            dot1 = 'B'
            dot2 = 'W'      

        if board[i][j] != dot1:
            startW += 1
        if board[i][j] != dot2:
            startB += 1

print(min(startB, startW))

