banks_f = open("input.txt", "r")

joltage: int = 0

for bank in banks_f:
    joltages: list[str] = list(bank.strip())
    to_remove: int = len(joltages) - 12 # maximum amount of characters we can remove

    batteries: list[str] = []

    for j in joltages:
        while to_remove > 0 and batteries and batteries[-1] < j:
            # can still remove digits, has a previous digit to compare to, and if said previous digit is smaller than j
            batteries.pop()
            to_remove -= 1
        batteries.append(j)

    joltage += int("".join(batteries[:12])) # trim off excess smaller numbers

print(joltage)