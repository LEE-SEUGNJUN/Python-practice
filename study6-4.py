i,k= 0,0
guguLine=""
for i in range(9,1,-1):
    guguLine= guguLine + ("### %d 단 ###\t" %i) 
print(guguLine) ##단수를 거꾸로 출력하기위해 9부터 1보다 클때까지만 -1씩 for문을 돌림

for i in range(1,10,1): ##i는 행이므로 그대로 둔다
    guguLine=""
    for k in range(9,1,-1): ## k는 열을 바꿔 거꾸려 하려는 것이기 때문에 9부터1보다 클때까지 돌린다.
        guguLine = guguLine + str("%2d * %2d = %2d\t" %(k,i,k*i))
    print(guguLine) ## 가로로보기 편하도록 한번에 출력
