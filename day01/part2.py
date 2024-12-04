import re

with open("input.txt", "r") as file:
    file_content = file.readlines()

lists = [re.findall(r"\d+", line) for line in file_content]
lists = [[int(i) for i in pair] for pair in lists]

list1 = [lists[i][0] for i in range(len(lists))]
list2 = [lists[i][1] for i in range(len(lists))]

similarities = [list2.count(element) * element for element in list1]

print(sum(similarities))