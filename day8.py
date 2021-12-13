import string

import numpy as np
from data_import import DataImporter
importer = DataImporter("day8.csv", ncols=14)
data = importer.read()
data = data[:-1] # As usual we have this last empty line, wherever it comes from

# print(data)

def sort_string(string):
    sorted_chars = sorted(string)
    return "".join(sorted_chars)

def find_mapping(signals):
    mapping = {}
    numbers = {}
    for i in range(len(signals)):
        signals[i] = sort_string(signals[i])

    for s in string.ascii_letters[:7]:
        mapping[s] = s

    ## First we identify the easy numbers
    for sig in signals:
        sig = sort_string(sig)
        if len(sig) == 2:
            numbers['one'] = sig
            # signals.remove(sig)
        elif len(sig) == 3:
            numbers['seven'] = sig
            # signals.remove(sig)
        elif len(sig) == 4:
            numbers['four'] = sig
            # signals.remove(sig)
        elif len(sig) == 7:
            numbers['eight'] = sig
            # signals.remove(sig)

    signals.remove(numbers['one'])
    signals.remove(numbers['four'])
    signals.remove(numbers['seven'])
    signals.remove(numbers['eight'])
    for sig in signals:
        sig = sort_string(sig)
        print(sig)
        if len(sig) == 5:
            three_test = set(sig) - set(numbers['seven'])
            five_test = set(sig).intersection(numbers['four'])
            two_test = set(sig).intersection(numbers['one'])
            if len(three_test) == 2:
                numbers['three'] = sig
                print('three')
                # signals.remove(sig)
            elif len(five_test) == 3:
                numbers['five'] = sig
                # mapping['f'] = [f for f in set(numbers['one']) - set(numbers['two'])][0]
                # signals.remove(sig)
            else:
                numbers['two'] = sig
                # signals.remove(sig)
        else: # at this point the only remaining length should be 6
            nine_test = set(sig) - set(numbers['seven']).union(set(numbers['four']))
            zero_test = set(numbers['one']) - set(sig)
            if len(nine_test) == 1:
                numbers['nine'] = sig
                mapping['g'] = [g for g in nine_test][0]
                # signals.remove(sig)
            elif len(zero_test) == 0:
                numbers['zero'] = sig
                # signals.remove(sig)
            else:
                numbers['six'] = sig
                # signals.remove(sig)

    print(numbers)

    ## Now we identify the easy letters
    mapping['a'] = [a for a in (set(numbers['seven']) - set(numbers['one']))][0] #
    mapping['d'] = [d for d in set(numbers['eight']) - set(numbers['zero'])][0]
    mapping['b'] = [b for b in set(numbers['four']) - set([mapping['c'], mapping['d'], mapping['f']])][0]
    mapping['e'] = [e for e in set(numbers['two']) - set(numbers['three'])][0]

    inverse_map = {val:key for key,val in numbers.items()}
    print(inverse_map)
    return(inverse_map)

# mapping = find_mapping(data[0][:10])
# code = data[0][-4:]
#
# for digit in code:
#     digit = sort_string(digit)

# PART A
counters = {
    'one': 0,
    'four': 0,
    'seven': 0,
    'eight': 0
}
counter = 0
for line in data:
    counter += 1
    print(counter)
    signal = line[:10]
    coded_digits = line[-4:]
    mapping = find_mapping(signal)
    for code in coded_digits:
        code = sort_string(code)
        digit = mapping[code]
        if digit in counters.keys():
            counters[digit] += 1

total_sum = 0
for digit in counters.keys():
    total_sum += counters[digit]

print(total_sum)

# Part B
digs = {
    'zero': 0,
    'one' : 1,
    'two' : 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

total_sum = 0
counter = 0
for line in data:
    counter += 1
    print(counter)
    signal = line[:10]
    coded_digits = line[-4:]
    mapping = find_mapping(signal)
    num = ''
    for code in coded_digits:
        code = sort_string(code)
        digit = mapping[code]
        num += str(digs[digit])
    total_sum += int(num)

print(total_sum)