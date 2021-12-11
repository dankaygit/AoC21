import numpy as np
from data_import import DataImporter
importer = DataImporter("day5.csv", ncols=2, sep = "->")
data = importer.read()
data = data[:-1] # As usual we have this last empty line, wherever it comes from

## Data Prep
def prepare_coordinates(data):
    i = 0
    clean_coords = []
    for line in data:
        new_line = []
        i+= 1
        for point in line:
            new_point = point.strip()
            new_point = new_point.split(",")
            new_point = [int(xy) for xy in new_point]
            new_line.append(new_point)
        clean_coords.append(new_line)
    return(clean_coords)

coords = prepare_coordinates(data)

## PART A

# This function produces a list of points corresponding to the line defined by the start and end points given in the coords
def calculate_line(points, noDiags = False):
    x1,y1 = points[0]
    x2,y2 = points[1]

    # For Part A we need not consider diagonal lines, so we return an empty list
    if noDiags:
        if x1!= x2 and y1!= y2: return []

    xs = [i for i in range(min(x1,x2), max(x1,x2) + 1)]
    ys = [i for i in range(min(y1,y2), max(y1,y2) + 1)]
    if x1 == x2:
        if y1 == y2: return points
        else:
            xs = [x1 for i in ys]
    elif y1 == y2:
        ys = [y1 for i in xs]
    if (x1 > x2 and y1 < y2) or (x1 < x2 and y1 > y2):
        ys = ys[::-1]

    return [[item[0],item[1]] for item in zip(xs,ys)]

# Here we count the number of times a specific point is hit, by adding the coordinates as keys to a dictionary
# and the update the number of times the point has come up in the value of the dict.

def day5(coords, part='A'):

    diags = True
    if part == 'B': diags = False

    point_map = {}
    for points in coords:
        for point in calculate_line(points, noDiags = diags):
            if str(point) not in point_map.keys():
                point_map[str(point)] = 1
            else:
                point_map[str(point)] += 1

    point_counter = 0
    for key in point_map:
        if point_map[key] > 1:
            point_counter += 1

    print(point_counter)

# Part A
day5(coords, 'A')

# Part B
day5(coords, 'B')
