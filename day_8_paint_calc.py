import math

def paint_area_calc(width, heigth):
  coverage = 5
  cans = (width * heigth)/coverage
  return math.ceil(cans)

wall_width = int(input("Wall width in meter: "))
wall_heigth = int(input("Wall heigth in meter: "))

cans = paint_area_calc(wall_width, wall_heigth)

print(f"You need {cans} cans of paint.")