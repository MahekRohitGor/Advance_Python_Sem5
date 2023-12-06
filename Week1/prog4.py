# Create a class for object dist containing feet and inches
# Add 3 instances of distance and display the ans
# d1 = 5 feet 6 inches d2 =3 feet 4 inches d3 = 3 feet 5 inches
# Add the d1+d2+d3 = 11 feet 3 inches

class Distance: # Create a class distance
    def __init__(self, feet=0, inches=0): 
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        total_feet = self.feet + other.feet
        total_inches = self.inches + other.inches

        if total_inches >= 12:  # If inches >= 12 
            total_feet += total_inches // 12
            total_inches = total_inches % 12

        return Distance(total_feet, total_inches)

    def __str__(self):
        return f"{self.feet} feet {self.inches} inches"


# Create instances of Distance
d1 = Distance(5, 6)
d2 = Distance(3, 4)
d3 = Distance(3, 5)

# Add distances
result = d1 + d2 + d3

# Display the result
print(f"d1 = {d1}")
print(f"d2 = {d2}")
print(f"d3 = {d3}")
print(f"d1 + d2 + d3 = {result}")
