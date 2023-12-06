# User gives an input string and doubles each letter
# Example: Apple Output: AAppppllee
string = str(input("Enter a string: "))
newString=""

for char in string:
    newString += char*2

print(newString)