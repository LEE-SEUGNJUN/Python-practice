num1= input("16진수 하나 입력 : ")

if( '0'<=num1<='9' ) or ('A'<= num1<= 'F') :
    print("10진수 ==> ",int(num1,16))
else :
    print("16진수가 아닙니다.")