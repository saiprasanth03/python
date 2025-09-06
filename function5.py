def sec_lar(l):
    l=list(set(l))
    l.sort()
    maximum=l[-2]
    print(maximum)
l=[1,5,2,6,8,4,7,8]
sec_lar(l)