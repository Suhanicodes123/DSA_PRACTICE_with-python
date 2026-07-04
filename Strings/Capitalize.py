Problem:Capitalize!
Concept:Strings
Platform:Hackerrank


def solve(s):
    return ' '.join(word.capitalize()for word in s.split(' ')) #makes the first letter of word capital
