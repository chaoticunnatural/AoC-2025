banks_f = open("input.txt", "r")

joltage = 0

for bank in banks_f:
    powers = list(bank.strip()) # '12344' into ['1', '2', '3', '4', '4'] and remove spaces/newlines

    best = 0
    n = len(powers)

    for b1 in range(n): # b1 is index of first digit
        for b2 in range(b1+1, n): # b2 is index of second digit, has to come after b1
            possible_best = int(powers[b1] + powers[b2])
            if possible_best > best:
                best = possible_best

    joltage += best

print(joltage)

