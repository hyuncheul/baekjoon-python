fir, sec = map(list, input().split())
fir.reverse()
sfir = ''.join(map(str,fir))
sec.reverse()
ssec = ''.join(map(str,sec))

if int(sfir) > int(ssec) : 
    print(sfir)
else: 
    print(ssec)