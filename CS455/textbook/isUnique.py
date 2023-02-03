'''
1.1 isUnique

Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?

'''
def isUnique(str):
    
    for i in str:
        if str.count(i) > 1:
            return False
    return True


print(isUnique("aba"))
print(isUnique("abc"))