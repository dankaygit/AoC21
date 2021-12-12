from data_import import DataImporter
importer = DataImporter("day7.csv", sep=",")
positions = importer.read_single_line("int")
print(positions)

# PART A
def calculate_fuel_consumption(positions, target_position):
    total_consumption = 0
    for sub in positions:
        total_consumption += abs(target_position - sub)
    return total_consumption

min_fuel_consumption = calculate_fuel_consumption(positions, positions[0])
for target_position in range(min(positions), max(positions)):
    consumption = calculate_fuel_consumption(positions, target_position)
    if consumption < min_fuel_consumption:
        min_fuel_consumption = consumption

print(min_fuel_consumption)

# PART B
def calculate_new_fuel_consumption(positions, target_position):
    total_consumption = 0
    for sub in positions:
        N_steps = abs(target_position - sub)
        total_consumption += int(N_steps*(N_steps+1)/2) # The whole trick of part B is an arithmetic sum of the steps
    return total_consumption

min_fuel_consumption = calculate_new_fuel_consumption(positions, positions[0])
for target_position in range(min(positions), max(positions)):
    new_consumption = calculate_new_fuel_consumption(positions, target_position)
    if new_consumption < min_fuel_consumption:
        min_fuel_consumption = new_consumption

print(min_fuel_consumption)