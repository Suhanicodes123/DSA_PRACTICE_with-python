Problem = The merge tools
Platform = Hackerrank
Concept = Strings/sets


def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i+k]

        seen = set()
        result = ""

        for ch in substring:
            if ch not in seen:
                seen.add(ch)
                result += ch

        print(result)
