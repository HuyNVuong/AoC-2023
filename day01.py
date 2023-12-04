import re

def line_to_value(line: str) -> int:
    numbers = re.sub(r'[a-z]+', '', line)
    return int(numbers[0]) * 10 + int(numbers[-1])
    
def str_to_int(num_str: str, reversed = False) -> int:
    if num_str == 'one':
        return 1
    elif num_str == 'two':
        return 2
    elif num_str == 'three':
        return 3
    elif num_str == 'four':
        return 4
    elif num_str == 'five':
        return 5
    elif num_str == 'six':
        return 6
    elif num_str == 'seven':
        return 7
    elif num_str == 'eight':
        return 8
    elif num_str == 'nine':
        return 9
    
    return int(num_str[-1] if reversed else num_str[0])

def line_to_value_2(line: str) -> int:
    regex_str = 'one|two|three|four|five|six|seven|eight|nine'
    number_strs = re.findall(re.compile(f'({regex_str}|[1-9]+)'), line)
    number_strs_reverse = re.findall(re.compile(f'({regex_str[::-1]}|[1-9]+)'), line[::-1])
    return str_to_int(number_strs[0]) * 10 + str_to_int(number_strs_reverse[0][::-1], True)

with open('./data/day01.txt', 'r') as file:
    lines = file.read().split('\n')
    total_sum = sum([line_to_value(line) for line in lines])
    print(total_sum)
    total_sum_2 = sum([line_to_value_2(line) for line in lines])
    print(total_sum_2)