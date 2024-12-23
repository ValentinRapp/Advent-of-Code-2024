import re

def element_exists_in_list(list, element) -> bool:
    try:
        list.index(element)
        return True
    except ValueError:
        return False

with open("input.txt", "r") as f:
    data = f.read()

matches = re.finditer("mul\\(\\d+,\\d+\\)", data)
dos = re.finditer("do\\(\\)", data)
donts = re.finditer("don't\\(\\)", data)

# part 1
# I rerwote this part after I lost the source code, this is why it looks so much better than the part 2

pairs = [[int(element) for element in re.findall(r"\d+", match.group())] for match in matches]

print(f"part 1: {sum([pair[0] * pair[1] for pair in pairs])}")

# part 2

matches = re.finditer("mul\\(\\d+,\\d+\\)", data)

parsed_numbers = []

matched_dos = [0]
matched_donts = []

for match in dos:
    matched_dos.append(match.span()[0])

for match in donts:
    matched_donts.append(match.span()[0])

for match in matches:
    index = match.span()[0]

    do = True
    while True:
        if element_exists_in_list(matched_donts, index):
            do = False
            break
        if element_exists_in_list(matched_dos, index):
            do = True
            break

        index -= 1

    if do:
        expr = match.group()
        numbers = re.findall(r"\d+", expr)
        parsed_numbers.append((int(numbers[0]), int(numbers[1])))

s = 0
for a, b in parsed_numbers:
    s += a * b

print(f"part 2: {s}")
