def deci_to_any(n,b):
    result=""
    while (n!=0):
        if n%b==10:
            result="A"+result
        elif n%b==11:
            result="B"+result
        elif n%b==12:
            result="C"+result
        elif n%b==13:
            result="D"+result
        elif n%b==14:
            result="E"+result
        elif n%b==15:
            result="F"+result
        else :
            result=(str(n%b)+result)
        n=n//b
    return result
asd=deci_to_any(61,2)
print(asd)