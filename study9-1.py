## 커피 종류를 아메리카노,카페라떼,카푸치노,에스프레소중 하나를 선택 할 수 있도록 하자.
## 그리고 로제,리사,지수,제니라는 손님 4명의 주문을 받아보자.
def coffee_machine(button): ##매개변수명은 button으로 , 함수 내부에서 쓰일 것이다. 실제 값은  함수밖의 coffee를 받을 예정
    print()
    print("#1.(자동으로)뜨거운 물을 준비한다.")
    print("#2.(자동으로)종이컵을 준비한다.")
    if button ==1:  ##coffee 변수의 수가 만약 1이라면 아메리카노
        print("#3.(자동으로)아메리카노를 탄다.")
    elif button ==2: ## 2라면 카페라떼
        print("#3.(자동으로)카페라떼를 탄다.")
    elif button ==3: ##생략
        print("#3.(자동으로)카푸치노를 탄다.")
    elif button ==4: ##생략
        print("#3. (자동으로)에소프레소를 탄다.")
    else:
        print("잘못 입력하셨습니다.")
    print("#4.(자동으로)물을 붓는다.")
    print("#5.(자동으로)스푼으로 젓는다.")
    print()        
coffee = int(input("로제님 어떤 커피를 드릴까요 ?1,아메리카노, 2.카페라떼, 3.카푸치노, 4.에스프레소 중 선택: "))
coffee_machine(coffee) ## 해당 커피 번호를 매개변수 값으로 넣고 함수 결과를 호출
print("로제손님 ~ 커피 여기있습니다.")

coffee = int(input("리사님 어떤 커피를 드릴까요 ?1,아메리카노, 2.카페라떼, 3.카푸치노, 4.에스프레소 중 선택: "))
coffee_machine(coffee) ## 해당 커피 번호를 매개변수 값으로 넣고 함수 결과를 호출
print("리사손님 ~ 커피 여기있습니다.")

coffee = int(input("지수님 어떤 커피를 드릴까요 ?1,아메리카노, 2.카페라떼, 3.카푸치노, 4.에스프레소 중 선택: "))
coffee_machine(coffee)## 해당 커피 번호를 매개변수 값으로 넣고 함수 결과를 호출
print("지수손님 ~ 커피 여기있습니다.")

coffee = int(input("제니님 어떤 커피를 드릴까요 ?1,아메리카노, 2.카페라떼, 3.카푸치노, 4.에스프레소 중 선택: "))
coffee_machine(coffee)## 해당 커피 번호를 매개변수 값으로 넣고 함수 결과를 호출
print("제니손님 ~ 커피 여기있습니다.")


