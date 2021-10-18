
## 메인 코드 부분##

while(True):
    year = int(input("연도를 입력하세요 : "))
    if((year % 4 == 0) and (year %100 !=0)) or (year%400 ==0) :
        print("{:d}년은 윤년입니다.".format(year))
        break
    else :
        print("{:d}년은 윤년이 아닙니다.".format(year))
        