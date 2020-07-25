def GCD(a,b):
    if a == 0:
        return a
    if b == 0:
        return b
    if a == b:
        return(a)
    if a > b:
        return(GCD(a-b,b))
    return(GCD(a,b-a))

def simplifyfraction(a,b):
    m = GCD(a,b)
    print(str(int(a/m))+'/'+str(int(b/m)))

