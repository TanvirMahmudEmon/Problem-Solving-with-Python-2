# Problem link: http://cpbook.subeen.com/2013/01/sort-them-all.html
# Accepted, Solved by Tanvir Mahmud Emon
# Python: 2.7.8

tc = input()
for i in range(tc):
    a,b,c=map(int,raw_input().split())
    if a>b:
        a,b = b,a
    if a>c:
        a,c = c,a
    if b>c:
        b,c = c,b
    print "Case %r:"%(i+1),a,b,c
