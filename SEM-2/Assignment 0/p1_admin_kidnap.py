t=int(input(""))
for i in range(t):
    x=input()
    nxs=tuple(map(int,x.split()))
    n,x,s=nxs
    for j in range(s):
        swap_input=input()
        ab=tuple(map(int,swap_input.split()))
        if x in ab:
            if x == ab[0]:
                x = ab[1]
            else:
                x = ab[0]
    print(x)