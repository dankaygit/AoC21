import numpy as np
from data_import import DataImporter
importer = DataImporter("day5.csv", ncols=2, sep = "->")
data = importer.read()
data = data[:-1] # As usual we have this last empty line, wherever it comes from

## Data Prep
def prepare_coordinates(data):
    """Returns a list of coordinates, consisting of a list of two points [x_start, y_start], [x_end, y_end]"""
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


# This function produces a list of
def calculate_line(points, noDiags = False):
    """Returns a list of points corresponding to the line defined by the start and end points given in points.
    If noDiags is set to True, diagonal lines are ignored by returning an empty list"""
    x1,y1 = points[0]
    x2,y2 = points[1]

    # For Part A we need not consider diagonal lines, so we return an empty list
    if noDiags:
        if x1!= x2 and y1!= y2: return []

    xs = [i for i in range(min(x1,x2), max(x1,x2) + 1)]
    ys = [i for i in range(min(y1,y2), max(y1,y2) + 1)]

    if x1 == x2:
        if y1 == y2: return points # If start and end point are the same, there's nothing to do
        else:
            xs = [x1 for i in ys]
    elif y1 == y2:
        ys = [y1 for i in xs]
    if (x1 > x2 and y1 < y2) or (x1 < x2 and y1 > y2):
        ys = ys[::-1]
    return [[item[0],item[1]] for item in zip(xs,ys)]

def draw_map(coords, part='A'):
    """Returns a dict with all coords as keys and the corresponding number of times it's hit as values
    For part = 'A' diagonals are ignored, while for part = 'B' they are included."""
    diags = True
    if part == 'B': diags = False

    point_map = {}
    for points in coords:
        for point in calculate_line(points, noDiags = diags):
            if str(point) not in point_map.keys():
                point_map[str(point)] = 1
            else:
                point_map[str(point)] += 1
    return point_map

def count_danger_points(point_map):
    """This function returns the number of points hit more than once in the point_map"""
    point_counter = 0
    for key in point_map:
        if point_map[key] > 1:
            point_counter += 1

    print(point_counter)

# Part A

coords = prepare_coordinates(data)
mapA = draw_map(coords, 'A')
count_danger_points(mapA)

# Part B
mapB = draw_map(coords, 'B')
count_danger_points(mapB)
