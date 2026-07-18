# Problem: Find Angle MBC
# Platform: HackerRank
# Concept: Math / Trigonometry

import math

AB = int(input())
BC = int(input())

angle = math.degrees(math.atan(AB / BC))

print(str(round(angle)) + chr(176)) #char(176) represents degree symbol
