# objective:
# Create a function that takes length and width and finds the perimeter of a rectangle.

def find_perimeter(length, width):
    return 2*(length + width)


print(find_perimeter(6,7))

# or

x = lambda length,width: 2*(length + width)