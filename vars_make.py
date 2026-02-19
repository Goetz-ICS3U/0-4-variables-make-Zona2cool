"""
author: Zonaisha
date: 2026- 02- 16
Making Variables
"""


### Input
rad_circle = int(input("Enter Circle Radius: "))
length_rec = int(input("Enter Rectangle Length: "))
width_rec = int(input("Enter Rectangle Width: "))
sideLegnth_oct = int(input("Enter Octagon Side Length: "))


### Processing


#circle Calculations
circle_area = 3.14159*rad_circle**2
circle_perimeter = 2*3.14159*rad_circle


#rectangle Calculations
rec_area = length_rec*width_rec
rec_perimeter = 2*length_rec + 2*width_rec


#octagon Calculations
oct_area = 2*(1+2**0.5)*sideLegnth_oct**2
oct_perimeter = 8*sideLegnth_oct


### Output
print(f"The circle has an area of {circle_area} and a perimeter of {circle_perimeter}")
print(f"The rectangle has an area of {rec_area} and a perimeter of {rec_perimeter}")
print(f"The octagon has an area of {oct_area} and a perimeter of {oct_perimeter}")
