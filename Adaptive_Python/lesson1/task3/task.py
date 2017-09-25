import sys

def mkad_tracker(v, t):
    mkad = 109
    pos = v * t % mkad
    return pos

print(mkad_tracker(int(input()), int(input())))
