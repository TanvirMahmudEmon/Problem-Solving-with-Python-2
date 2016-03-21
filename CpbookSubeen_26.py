# Problem link: http://cpbook.subeen.com/2013/01/great-grading-scheme.html
# Accepted, Solved by Tanvir Mahmud Emon
tc = input()
for i in range(tc):
    m = input()
    if m >= 80 and m <= 100:
        print "Case %r: A+"%(i+1)
    elif m >=75 and m <= 79:
        print "Case %r: A"%(i+1)
    elif m >=70 and m <= 74:
        print "Case %r: A-"%(i+1)
    elif m >=65 and m <= 69:
        print "Case %r: B+"%(i+1)
    elif m >=60 and m <= 64:
        print "Case %r: B"%(i+1)
    elif m >=55 and m <= 59:
        print "Case %r: B-"%(i+1)
    elif m >=50 and m <= 54:
        print "Case %r: C"%(i+1)
    elif m >=45 and m <= 49:
        print "Case %r: D"%(i+1)
    else:
        print "Case %r: F"%(i+1)
