Problem:Strings
Concept:Text Wrap
Platform:HackerRank


import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)  # textwrap.fill() is used to wrap the input string into lines of specified width. It takes the input string and the maximum width as arguments and returns a new string with the wrapped text