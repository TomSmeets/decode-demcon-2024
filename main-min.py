import sys

t = []
def a(a,b):a.append(b)

# Read text file
for l in open(sys.argv[1]):
    s = l.split(" ")
    a(t,(s[0], int(s[1]), int(s[2])))

# Solve
i = 0
while t!=[]:
    c,p,t = t,[],[]
    print("Plan",i)
    i+=1
    while len(c) > 0:
        r = min(c, key=lambda x: x[2])
        print("  ", r[0], r[1], r[1])
        a(p,r)
        d = []
        [a((d,t)[s[1] <= r[2]],s) for s in c if s != r]
        c = d
