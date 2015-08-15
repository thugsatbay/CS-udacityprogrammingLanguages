# Bonus Practice: Subsets

# This assignment is not graded and we encourage you to experiment. Learning is
# fun!

# Write a procedure that accepts a list as an argument. The procedure should
# print out all of the subsets of that list.

def Subsets(left,coming):
    if len(left)!=0:
        temp=left[0:1]
        left=left[1:]
        Subsets(left,coming)
        coming=coming+temp
        Subsets(left,coming)
    else:
        print coming
    
lss=[1,2,3,4]
print lss[0]
print len({})
Subsets(["A","B","C"],[])
