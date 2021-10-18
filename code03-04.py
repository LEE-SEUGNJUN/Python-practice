sel = int(input("입력 진수 결정(16/10/8/2) : "))

if sel != 16 or sel != 10 or sel != 8 or sel != 2:
    while(True) : 
        print("16,10,8,2 중 하나만 입력하세요")
        sel = int(input("입력 진수 결정(16/10/8/2) : "))
        if sel == 16 or sel == 10 or sel == 8 or sel == 2 :
            break
    

num = input("값입력: ")

if sel == 16:
    num10 = int(num,16)
if sel == 10:
    num10 = int(num,10)
if sel == 8:
    num10 = int(num,8)
if sel == 2:
    num10 = int(num,2)

print("16진수 ==> ",hex(num10))
print("10진수 ==>", num10)
print("8진수 ==>",oct(num10))
print("2진수 ==>",bin(num10))