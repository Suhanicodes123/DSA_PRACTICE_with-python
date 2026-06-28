Problem:Find Runner Up score
Concept:Using List Properties
Platform:Hackerrank


n = int(input())
    arr = map(int, input().split())
    arr = list(set(arr))
    arr.sort()
    
    print(arr[-2])
