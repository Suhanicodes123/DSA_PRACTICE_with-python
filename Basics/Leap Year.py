#To know the input year is leap year or not

def is_leap(year): 
    if year % 4==0: #remainder when divided by 4 is 0
        print("True")
    elif year % 400==0: #remainder when divided by 400 is 0
        print("True")
    elif year % 100==0: #remainder when divided by 100 is 0
        print("True")
    else:
        print("False")
    
    return leap

year = int(input())
print(is_leap(year))