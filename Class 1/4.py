# T= 테스트 수 , W = 한층 방 수 H = 호텔 높이 N = 손님 순번
T = int(input())
H = []
W = []
N = []
for i in range(T): 
    h, w, n = map(int, input().split())
    H.append(h)
    W.append(w)
    N.append(n)

for i in range(T):
    level = N[i]%H[i]
    room = N[i]//H[i] + 1

    if level ==0 :
        level = H[i]
        room = room -1
        
    roomnum = level*100 + room
    print(roomnum) 