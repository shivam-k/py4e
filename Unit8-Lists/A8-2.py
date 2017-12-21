## for the first part
lst = ['1', '43', '3', '65', '4']
def chop(t):
    lent = len(t)
    del t[lent-1]
    del t[0]

chop(lst)
print(lst)

## for the second part
lst = ['1', '43', '3', '65', '4']
def middle(t):
    le = len(t)
    g = t[1:le-1]
    return(g)

print(middle(lst))
