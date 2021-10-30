def vlqh(asd):
    if asd ==0:
        return 0
    elif asd==1:
        return 1
    else :
        return vlqh(asd-1) + vlqh(asd-2)
while(True):
    asd=int(input("피보나치 수열 F(N)의 N값을 입력하세요--> "))
    print("F(%d) = %d " % (asd,vlqh(asd)))    