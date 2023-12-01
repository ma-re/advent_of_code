import re

# Get data
def get_data(path: str) -> list:
    data = [x.strip() for x in open(path)]
    return data

# Replace written numbers with digits
def replace_numbers_front(elem, reverse=False):
    replacement_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 
                    'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 
                    'eno': 1, 'owt': 2, 'eerht': 3, 'ruof': 4, 'evif': 5, 
                    'xis': 6, 'neves': 7, 'thgie': 8, 'enin': 9}
    ind = {}
    if reverse:
        elem = elem[::-1]

    for num in replacement_dict.keys():
        ind[num] = elem.find(num)
    
    existing_strings = {k: v for k, v in ind.items() if v != -1}
    
    if len(existing_strings) > 0:
        min_number = min(existing_strings, key=existing_strings.get)
        elem = elem.replace(min_number, str(replacement_dict[min_number]))
    return elem

# Calculate final count
def calculate(data: list, part_two=False) -> int:
    count = 0
    for elem in data:
        if part_two:
            elem_front = replace_numbers_front(elem)
            elem_back = replace_numbers_front(elem, reverse=True)
            front_numbers = re.findall("[0-9]", elem_front)
            back_numbers = re.findall("[0-9]", elem_back)
            count += int(front_numbers[0] + back_numbers[0])
        else:
            elem = re.findall("[0-9]", elem)
            count += int(elem[0] + elem[-1])
    return count            


data = get_data("data/day1.txt")
part_1 = calculate(data)
part_2 = calculate(data, part_two=True)
print("Part 1: ", part_1)
print("Part 2: ", part_2)
