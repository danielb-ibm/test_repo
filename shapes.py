import math

# computing the area of a circle by multplying pi and the radius squared
def computeAreaCircle(radius):
    area = math.pi * radius**2
    return area

# computing the circumference of a circle by multplying pi and the radius x 2
def computeCircumferenceCircle(radius):
    circumference = 2 * math.pi *radius
    return circumference

# computing the area of a trapezoid by dividing the sum of the shorter base
# and the longer base by 2 and multplying them by the height
def computeAreaTrapezoid(shorter_base, longer_base, height):
    areaT = 1/2 * (longer_base + shorter_base) * height
    return areaT

# computing the perimeter of a trapezoid by summing up the length of its four sides
def computePerimeterTrapezoid(side1,side2,side3,side4):
    perimeter = sum((side1,side2,side3,side4))
    return perimeter

# computing the surface area of a cylinder by multplying pi and the radus by 2
# and multplying them by the sum of the radius and the height
def surfaceAreaCylinder(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

# computing the volume of the cylinder by multplying pi and the radius
# squared and the height
def volumeCylinder(radius, height):
    volume = math.pi * radius**2 * height
    return volume

# computing the surface area of a sphere by multplying pi by 4 and the radius
# squared
def surfaceAreaSphere(radius):
    area_sphere = 4 * math.pi * radius**2
    return area_sphere

# computing the volume of a sphere by multplying pi by 4/3 and the radius cubed
def volumeSphere(radius):
    volume_sphere = 4/3 * math.pi * radius**(3)
    return volume_sphere

# computing the surface area of a pyramid by multplying the edge length by 2
# and adding them to the edge length
# multplied by the square root of the sume of the edge length square
# and the height squared multplied by 4 
def surfaceAreaPyramid(edge_length,height):
    total_surface_area = edge_length**2 + edge_length*(math.sqrt(edge_length**2 + 4 * (height**2)))
    return total_surface_area

# computing the volume of a pyramid by diving the product of the length,
# height and width by 3
def volumeofPyramid(width, length, height):
    volume_pyramid = 1/3 * width * length * height
    return volume_pyramid
