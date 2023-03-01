# Objective:
# Checking for symmetry for a given string

# Notes
# accessing key pairs:

# pairs = {
#  "{":"}",
#  "(":")",
#  "[":"]"
# }

# print(pairs["{"])

# _____________________________________________________________________________________

# newstring = "{([])}"
# print(pairs[newstring[0]])


def  checkSymmetry(givenInput):
  pairs = {
    "{":"}",
    "(":")",
    "[":"]"
  }
  outPut = True
  #check for even length
  if len(givenInput) % 2 != 0:
    outPut = False
    return outPut
  else:
    for i in range(int(len(givenInput)/2)): #loop that traverse first half
      if givenInput[i] == "{" or givenInput[i] == "(" or givenInput[i] == "[":
        if pairs[givenInput[i]] == givenInput[len(givenInput)-1-i]:
          outPut = True
        else:
          outPut = False
          break
  return outPut

            
print(checkSymmetry("{[()]}"))
print(checkSymmetry("{(([])[])[]}"))


print(checkSymmetry("{([])}"))