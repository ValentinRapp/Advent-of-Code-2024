import re

def is_valid_page(page: int, pages: list[int], rules: list[list[int]]) -> bool:
    must_be_before = [rule[1] for rule in rules if (rule[0] == page and rule[1] in pages)]
    must_be_after = [rule[0] for rule in rules if (rule[1] == page and rule[0] in pages)]

    is_before = True
    for element in pages:
        if element == page:
            is_before = False
            continue
        if is_before and element in must_be_after:
            continue
        if not is_before and element in must_be_before:
            continue
        return False
    
    return True

def reorder_pages(pages: list[int], rules: list[list[int]]) -> list[int]:
    ordered_pages = pages.copy()
    
    changed = True
    while changed:
        changed = False
        for _ in range(len(ordered_pages) - 1):
            for rule in rules:
                if rule[0] in ordered_pages and rule[1] in ordered_pages:
                    
                    x_index = ordered_pages.index(rule[0])
                    y_index = ordered_pages.index(rule[1])
                    
                    if x_index > y_index:
                        ordered_pages[x_index], ordered_pages[y_index] = ordered_pages[y_index], ordered_pages[x_index]
                        changed = True
                        break
            if changed:
                break
    
    return ordered_pages

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

rules = [lines[i] for i in range(lines.index(""))]
rules = [[int(element) for element in re.findall(r"\d+", rule)] for rule in rules]

updates = [lines[i] for i in range(lines.index("") + 1, len(lines))]
updates = [[int(element) for element in re.findall(r"\d+", pages)] for pages in updates]

# Part 1
part1 = sum(pages[len(pages) // 2] for pages in updates if all(is_valid_page(page, pages, rules) for page in pages))
print(f"part1: {part1}")

# Part 2
part2_updates = [pages for pages in updates if not all(is_valid_page(page, pages, rules) for page in pages)]
part2 = sum(reordered[len(reordered) // 2] for reordered in [reorder_pages(pages, rules) for pages in part2_updates])
print(f"part2: {part2}")