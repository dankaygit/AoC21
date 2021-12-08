from data_import import DataImporter

## Data import from our very own importer
importer = DataImporter("day1.csv")
lines = importer.read()

### Part A
#%%
increment_count = 0

previous_line = lines[0]
for line in lines[1:]:
    if line > previous_line: increment_count += 1
    previous_line = line

print (increment_count)
#%%### Part B
#%%

increment_count = 0

previous_sum = sum(lines[:3])
for i in range(1, len(lines)-2):
    window = lines[i:i+3]
    val = sum(window)
    if val > previous_sum: increment_count += 1
    previous_sum = val

print (increment_count)
#%%