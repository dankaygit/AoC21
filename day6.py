from data_import import DataImporter

importer = DataImporter("day6.csv", sep=",")
fish_timers = importer.read_single_line("int")
print(fish_timers)


# <editor-fold desc="Part A, Naive Approach">
def grow_population(fish_timers):
    """Returns fish_timers one day later from input fish_timers, as defined by the population growth rules"""
    new_timers = []
    for fish in fish_timers:
        if fish == 0:
            new_timers.append(6)
            new_timers.append(8)
        else:
            new_timers.append(fish - 1)

    return new_timers


## Brute forcing the numbers by just keeping track of the timer number of each fish.
## This will not work in Part B
previous_timers = fish_timers
new_timers = []

for i in range(80):
    print(i)
    new_timers = grow_population(previous_timers)
    previous_timers = new_timers

print(len(new_timers))


# </editor-fold>

# PART B

def compute_spawning_days(self_spawn_day, num_days):
    """
    Takes the fish' own spawn_day and computes the dates, at which this fish will spawn new children fish
    starting from its own self_spawn_day up until the date of num_days. Returns a list of spawning_days
    :param self_spawn_day: The day the mother fish itself was spawned
    :param num_days: The total number of days to consider
    :return: List of dates when the mother fish spawns children
    """
    spawning_days = []
    first_spawn_day = self_spawn_day + 9
    for day in range(first_spawn_day, num_days + 1):
        if (day - first_spawn_day) % 7 == 0:
            spawning_days.append(day)
    return spawning_days


def spawn_dict_init(fish_timers):
    """
    Returns a dictionary with the corresponding spawn dates for the fish_timers as string keys,
    And the number of fish spawned on those dates as the values.
    Day 0 corresponds to fish with initial timer 0, day 1 to fish with timer 1, etc...
    """

    daily_spawns = {}
    for fish in fish_timers:
        # We start the day count 8 days before the number of evolution epochs, so that we can apply the same logic to
        # The fish we start with as well as the fish they will spawn. Their spawn date is equal to their current
        # timer, given that if someone has timer value 0 then that must mean that they have been spawned 8 days
        # earlier, which we call day 0, the earliest possible date.

        self_spawn_day = fish
        day = str(self_spawn_day)  # dict needs strings as keys (I think?)
        if day not in daily_spawns.keys():
            daily_spawns[day] = 1
        else:
            daily_spawns[day] += 1

    return daily_spawns


def fill_spawning_dates(daily_spawns):
    """
    :param daily_spawns: dictionary of spawns for each day in num_days, filled with mother and children fish of the initial fish timer list
    :return: daily_spawns for all fish that will be spawned in the future until num_days
    """
    for self_spawn_day in range(num_days):
        if str(self_spawn_day) not in daily_spawns.keys(): continue
        num_spawns_today = daily_spawns[str(self_spawn_day)]

        spawning_days = compute_spawning_days(self_spawn_day, num_days)

        for spawn_day in spawning_days:
            spawn_day = str(spawn_day)
            if spawn_day not in daily_spawns.keys():
                daily_spawns[spawn_day] = num_spawns_today
            else:
                daily_spawns[spawn_day] += num_spawns_today
    return daily_spawns


def count_total_fish(daily_spawns):
    """

    :param daily_spawns: dict filled with spawn numbers from initial fish
    :return: total number of fish spawned over the entire period, including initial fish
    """
    total_fish = 0
    for day in daily_spawns.keys():
        total_fish += daily_spawns[day]
    return total_fish

# Putting it all together. The real work lies in the functions above
# First we test the correctness of the code using the same number of evolution_epochs as in Part A and compare it with
# The naive approach

previous_days = 8
evolution_epochs = 80
num_days = evolution_epochs + previous_days

initial_daily_spawns = spawn_dict_init(fish_timers)
daily_spawns = fill_spawning_dates(initial_daily_spawns)
total_fish = count_total_fish(daily_spawns)
print(total_fish)

## Part B solution:
previous_days = 8
evolution_epochs = 256
num_days = evolution_epochs + previous_days

initial_daily_spawns = spawn_dict_init(fish_timers)
daily_spawns = fill_spawning_dates(initial_daily_spawns)
total_fish = count_total_fish(daily_spawns)
print(total_fish)