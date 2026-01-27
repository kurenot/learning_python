while True:
    print("enter first number")
    s=int(input())
    print("enter second number")
    m=int(input())
    print("enter operation")
    op=input()
    res=0
    if op=="+":
        res=s+m
    elif op=="-":
        res=s-m
    elif op=="*":
        res=s*m
    elif op=="/":
        res=s/m
    print(res)