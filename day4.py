## Preparation and Import

import numpy as np
from data_import import DataImporter
importer = DataImporter("day4.csv")
data = importer.read()

random_nums = [int(i) for i in data[0].split(",")]

"""0 will give us problems later so let's just rename 0 to -1 both in the random nums and in the boards
We only need -1 to become 0 again when we compute the points at the end, so we can just do that 
for the final board at the end"""

random_nums[random_nums.index(0)] = -1

# We define a function to prepare the starting boards from the raw data
def get_start_boards(data):
    start_boards = []
    board = []
    for line in data[2:]:
        if line == "":
            start_boards.append(board)
            board = []
        else:
            row = line.split()
            if "" in row: row.remove("")
            board.append([int(i) for i in row])
    return (start_boards)

## PART A ##

# 0 will give us problems later so let's just rename 0 to -1 both in the random nums and in the boards
start_boards = get_start_boards(data)
boards = np.array(start_boards)
boards[np.where(boards == 0)] = -1

points = 0

for num in random_nums:
    # Set all numbers in a board to 0 if it's num, which means striking it out
    boards[np.where(boards == num)] = 0
    # Now we need to find out whether a whole row or column is 0 yet
    for board in boards:
        if 0 in board.sum(axis=0) or 0 in board.sum(axis=1):
            board[np.where(board == -1)] = 0 # Now reset the original 0s to compute the correct sum, in case there were any
            points = board.sum() # Compute the sum of the board
            break
    if points > 0:
        points *= num
        break

print(points)

## Part B

boards = get_start_boards(data)
points = 0

# Setting 0s to -1
for board in boards:
    for row in board:
        if 0 in row:
            row[row.index(0)] = -1

for num in random_nums:
    npboards = np.array(boards)
    ## Set all numbers in a board to 0 if it's num, which means striking it out
    npboards[np.where(npboards == num)] = 0
    ## Now we need to find out whether a whole row or column is 0 yet.
    ## But now, in part B, we want to find the last board that wins, so instead of breaking the loops
    ## We need to remove the boards that won already
    boards = npboards.tolist()
    ind_to_delete = []
    for board in boards:
        if 0 in np.array(board).sum(axis=0) or 0 in np.array(board).sum(axis=1):
            ind_to_delete.append(boards.index(board))

    ind_to_delete.sort()

    # This is crucial: if you start by deleting the boards from the beginning of the list,
    # The indices afterwards will be wrong. Therefore delete from the largest indices backwards,
    # i.e. sort the indices from biggest to lowest
    for ind in ind_to_delete[::-1]:
        if len(boards) == 1: break
        boards.pop(ind)

    # It can happen in the penultimate round, that the last board hasn't won yet and the winning number
    # still needs to be drawn. Therefore, we just let the loop run further, until the final winning number is drawn
    # and only then we compute the points for the board
    if len(boards) == 1 and (0 in np.array(boards[0]).sum(axis=0) or 0 in np.array(boards[0]).sum(axis=1)):
        board = np.array(boards[0])
        board[np.where(board == -1)] = 0
        #         print (board)
        points = np.array(board).sum() * num
        #         print (points)
        break

print(points)
