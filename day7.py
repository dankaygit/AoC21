from data_import import DataImporter
importer = DataImporter("day7.csv", sep=",")
positions = importer.read_single_line("int")
print(positions)


def calculate_fuel_consumption(positions, target_position, part = 'A'):
    """

    :param positions:
    :param target_position:
    :param part:
    :return:
    """
    total_consumption = 0
    for sub in positions:
        N_steps = abs(target_position - sub)
        if part == 'A':
            total_consumption += N_steps
        else:
            total_consumption += int(N_steps*(N_steps+1)/2)
    return total_consumption


def find_min_fuel_consumption(positions, part = 'A'):
    """

    :param positions:
    :return:
    """
    min_fuel_consumption = calculate_fuel_consumption(positions, positions[0], part = part)
    for target_position in range(min(positions), max(positions)):
        consumption = calculate_fuel_consumption(positions, target_position, part = part)
        if consumption < min_fuel_consumption:
            min_fuel_consumption = consumption
    print (min_fuel_consumption)
    return min_fuel_consumption


find_min_fuel_consumption(positions, part = 'A')
find_min_fuel_consumption(positions, part = 'B')