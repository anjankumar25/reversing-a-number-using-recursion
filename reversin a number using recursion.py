def aa(a):
    if a==0:
        return
    e=a%10
    print(e)
    aa(a//10)
aa(12344)