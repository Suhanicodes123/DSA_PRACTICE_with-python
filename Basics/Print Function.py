Problem:Print Function
Concept:Use of Print function in Loops
Platform:Hackerrank

#print integers from 1 to n without spaces
    n = int(input())
    for i in range(1,n+1):
        print(i,end="")
        i+=1
