i,k= 0,0
guguLine=""
for i in range(2,10,):
    guguLine= guguLine + ("### %d 단 ###\t" %i)   
print(guguLine)## 2,3,4...9단을 가로로 한번에 출력하기위해 guguLine에 더하기만하다가 한번에 출력

for i in range(1,10,1):
    guguLine="" ## 위에서 출력된 guguLine을 초기화시킴
    for k in range(2,10): ##2단부터 9단까지
        guguLine = guguLine + str("%2d * %2d = %2d\t" %(k,i,k*i)) 
    print(guguLine) ##안에있는 for문이 i가 한번 돌때 9번 돌으므로 가로로 한번에 출력하기위해 k를 앞에 쓰고 guguLine을 한번에 출력한다.
                    ##i는 행으로갈수록 +1  k는 열로 갈수록 +1 