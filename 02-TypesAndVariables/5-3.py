###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
ax = input('a=')
bx = input('b=')
cx = input('c=')

a=int(ax)
b=int(bx)
c=int(cx)

cuboid_volume = a * b * c
cuboid_surface_area = 2*(a*b + b*c + c*a)

print(f'Objetosc wynosi {cuboid_volume}')
print(f'Pole powierzchni wynosi {cuboid_surface_area}')