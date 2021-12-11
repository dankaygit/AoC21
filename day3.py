## For Part A, don't try counting the binary numbers but rather try adding them
# bitwise and then checking whether the decimal sum of each position is higher or lower than len(data)/2

from data_import import DataImporter
importer = DataImporter("day3.csv")
data = importer.read()

## PART A

def binary_to_decimal(binary):
    decimal = 0
    for i in range(len(binary)):
        decimal += 2**i * binary[-(i+1)]
    return (decimal)

binaries = []
for code in data[:-1]: # There's again the problem of the empty line at the end.
    binary = []
    for num in code:
        binary.append(int(num))
    binaries.append(binary)

sums = [0 for i in range(len(binaries[0]))]
for i in range(len(binaries)):
    for j in range(len(binaries[0])):
        sums[j] += binaries[i][j]

# print(sums)

gamma = []
epsilon = []

for num in sums:
    bit = 0
    if num > len(binaries)/2: bit = 1
    gamma.append(bit)

for bit in gamma:
    if bit == 0:
        epsilon.append(1)
    else:
        epsilon.append(0)

gam_dec = binary_to_decimal(gamma)
eps_dec = binary_to_decimal(epsilon)

print(gam_dec*eps_dec)

## PART B

### Separate the lists into two each time

def find_most_common(binaries, least = False):

    new_binaries = binaries
    for i in range(len(binaries[0])):
        lows = []
        highs = []
        sum = 0
        N = len(new_binaries)
        for binary in new_binaries:
            if binary[i] == 0:
                lows.append(binary)
            else:
                highs.append(binary)
                sum += 1
        # print(lows[:5])
        # print(highs[:5])
        if len(new_binaries) == 1: return new_binaries
        if not least:
            if sum >= N/2 :
                new_binaries = highs
            else:
                new_binaries = lows
        else:
            if sum < N/2 :
                new_binaries = highs
            else:
                new_binaries = lows
        # print (len(new_binaries))
        # print(N/2, sum, new_binaries[:2])
    return(new_binaries)

oxy = find_most_common(binaries)[0]
co2 = find_most_common(binaries, least = True)[0]

life_support = binary_to_decimal(oxy) * binary_to_decimal(co2)

print(life_support)




