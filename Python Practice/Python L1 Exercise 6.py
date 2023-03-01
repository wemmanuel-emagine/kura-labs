# objective:
# Create a function that finds the maximum range of a triangle's third edge, where the side lengths are all integers.

def next_edge(side1,side2):
    max_side = (side1 + side2) - 1
    print(max_side)

def next_edge2(*args):
    max_side = sum(args) -1 
    print(max_side)

next_edge(8,10)

next_edge2(10,11)