Problem:Alphabet rangoli
Concept:Strings/Printing pattern
Platform:Hackerrank


def print_rangoli(size):
    alpha='abcdefghijklmnopqrstuvwxyz'
    width=4 * size - 3
    lines=[]
    
    for i in range(size):
        s = "-".join(alpha[size - 1:i:-1] + alpha[i:size])
        lines.append(s.center(width, "-"))
        
    print("\n".join(lines[::-1] + lines[1:]))
    