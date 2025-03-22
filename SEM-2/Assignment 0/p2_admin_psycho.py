n=int(input(""))
c=0
pos=0
x=input()
height_list=list(map(int,x.split()))
l=list(height_list)
min_no=min(l)
for i in range(n):
    if (sorted(height_list)==height_list)or(len(l)==0):
        break
    elif min_no!=height_list[i]:
        height_list[height_list.index(min_no)],height_list[pos]=height_list[pos],min_no
        l.remove(min_no)
        min_no=min(l)
        pos+=1
        c+=1
print(height_list)
print(c)