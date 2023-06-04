m = int(input("Enter a number : \t"))
n = int(input("Enter a number : \t"))
opr = input("What operation you want to perform? \
            \n + for addition \
            \n - for subtraction\
            \n * for multiplication\
            \n / for division\n")


def operation(arguement):
    if arguement == '+':        
        print(m,' + ',n,' = ',m+n)

    elif arguement == "-":
            print(m,' - ',n,' = ',m-n)

    elif arguement == "*":
            print(m,' * ',n,' = ',m*n)
    
    elif arguement == "/":
            print(m,' / ',n,' = ',m/n)

    else :
            print("Wrong operation selected\n")

operation(opr)            