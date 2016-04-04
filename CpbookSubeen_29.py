# Problem link: http://cpbook.subeen.com/2013/01/digital-trivuz.html
# Accepted, Solved by Tanvir Mahmud Emon
# Python: 2.7.8

tc = input()
import sys
for i in range(1,tc+1):
    a,b=map(int,raw_input().split())
    print "Case %r:"%(i)
    for j in range(1,b+1):
        for k in range(1,j+1):
            sys.stdout.write("%d"%(a))
        print "\n",
