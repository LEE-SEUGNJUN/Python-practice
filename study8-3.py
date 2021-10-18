##입력받은 수가 숫자로만돼있는지,문자로만 돼있는지,문자+숫자인지 확인하는 코드이다. 특수문자는 잘모르겠다고 출력한다.
asd=input("값을 입력하세요 : ") ## 값을 입력받는다

if asd.isdigit()==True: ##입력받은 asd가 숫자인지를 판별한다
    print("숫자입니다")
elif asd.isalpha()==True:## 입력받은 asd가 문자인지를 판별한다
    print("문자입니다")
elif asd.isalnum()==True:## 입력받은 asd가 문자+숫자인지를 판별한다
    print("문자+숫자 입니다")
else :
    print("잘 모르겠습니다.") ##셋 다 아니면 잘 모르겠습니다를 출력