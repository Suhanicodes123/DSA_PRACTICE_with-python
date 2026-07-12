def palindrome(s):
    if len(s) <=1:
        return True #a string of len 0 or 1 is a palindrome


    if s[0] != s[-1]:
        return False #if first and last char are diff, it is not a palindrome


    return palindrome(s[1:-1]) #if first and last char are same remove them and check other chars

#ex:
print(palindrome("madam"))
