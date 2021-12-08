from data_import import DataImporter

# class Day2():
#
#     directions = {}
#     directions['forward'] = 0  # x-axis
#     directions['down'] = 1  # y-axis
#     directions['up'] = -1  # y-axis
#     coords = [0, 0]  # [x, y] coordinates
#
#     def __init__(self):
#         ## Data import from our very own importer
#         importer = DataImporter("day2.csv", ncols=2)
#         self.data = importer.read()
#         # self.directions = {}
#         # self.directions['forward'] = 0  # x-axis
#         # self.directions['down'] = 1  # y-axis
#         # self.directions['up'] = -1  # y-axis
#         # self.coords = [0, 0] # [x, y] coordinates
#
#     def coordinate(self, line, dir_dict = directions):
#         return abs(dir_dict[line[0]])
#
# day2 = Day2()
#
# for line in Day2.data:
#     coord = Day2.coordinate(line)
#     val = line[1]
#     if coord == -1: val *= -1
#
#     Day2.coords[coord] += val
#
# print (Day2.coords)

## Part A
## But without trying to be fancy with classes and dicts

importer = DataImporter("day2.csv", ncols=2)
data = importer.read()
coords = [0,0]

## Parse the data according to the rules
for line in data[:-1]:
    val = int(line[1])
    if line[0] == "forward":
        coords[0] += val
    elif line[0] == "down":
        coords[1] += val
    else:
        coords[1] -= val

print(coords, coords[0] * coords[1])

