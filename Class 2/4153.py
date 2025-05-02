#입력받는다 000이 들어오기 전까지
X =[]
Y =[]
Z =[]
res = []

token = True
while(token):
    x, y, z = map(int, input().split())
    if x == 0 and y == 0 and z ==0:
        token = False
    
    else: 
        X.append(x)
        Y.append(y)
        Z.append(z)
rig = 'right'
wrg = 'wrong'

for i in range(len(X)):
    side = sorted([X[i],Y[i], Z[i]])
    if side[2]*side[2] == side[1]*side[1] + side[0]*side[0]:
        res.append(rig)
    else: res.append(wrg)


for result in res:
    print(result)