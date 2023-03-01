#Objective:
# Create a function that takes a name and returns a greeting in the form of a string.

# One way of doing it
def hello_name(name):
    print(f"Hello {name}!")

# Other way of doing it0
def greeting(name):
    return "Hello {}!".format(name)  

#Running function
hello_name("Jack")
