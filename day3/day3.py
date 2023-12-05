from itertools import chain

def get_numbers_with_positions(data:list[str]):
    numbers_with_positions = []

    for y, line in enumerate(data):
        number = ''
        positions_for_number = []
        for x, char in enumerate(line):
            if char.isdigit():
                number += char
                positions_for_number.append((x,y))
                if x == 139:
                    numbers_with_positions.append((int(number),positions_for_number))
            elif number != "":
                numbers_with_positions.append((int(number),positions_for_number))
                number = ""    
                positions_for_number = []
    return numbers_with_positions


        
def get_symbol_positions(data):
    positions = []
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if (not char.isdigit()) and char != '.':
                positions.append((x,y))
    return positions
            
def get_numbers_with_adjacent_symbols(numbers_w_pos: list, symbol_positions:list):
    sym = set(symbol_positions)
    hits = []
    for number, positions in numbers_w_pos:
        flattened_adjacent_positions = list(chain.from_iterable([adj(x,y) for x,y in positions]))
        unique_adj_c = set(flattened_adjacent_positions).difference(positions)
        if m := unique_adj_c.intersection(sym): 
            hits.append((number,list(m)[0]))
    return [num for num in hits]

def adj(x,y):
    return [(x+1,y),(x+1,y+1),(x,y+1),(x-1,y+1),(x-1,y),(x-1,y-1),(x,y-1),(x+1,y-1)]

def task1():
    with open('./day3/data.txt', encoding="utf-8") as f:
        data = f.read().splitlines()
        numbers_with_positions = get_numbers_with_positions(data)
        symbol_positions = get_symbol_positions(data)
        numbers = get_numbers_with_adjacent_symbols(numbers_with_positions, symbol_positions)
        print(sum([x for x,_ in numbers]))
task1()
        
#======================================================================================


def get_gear_positions(data):
    positions = []
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == '*':
                positions.append((x,y))
    return positions

def task2():
    with open('./day3/data.txt', encoding="utf-8") as f:
        data = f.read().splitlines()
        numbers_with_positions = get_numbers_with_positions(data)
        gear_positions = get_gear_positions(data)
        numbers_adjacent_to_gears = get_numbers_with_adjacent_symbols(numbers_with_positions, gear_positions)
        gear_dict = {}
        for num,gear in numbers_adjacent_to_gears:
            if gear in gear_dict:
                l = gear_dict[gear]
                l.append(num)
            else:
                gear_dict[gear] = [num]   
        total_sum = 0
        for gear,nums in gear_dict.items():
            if len(nums) == 2:
                total_sum += nums[0]*nums[1]
        print(total_sum)
task2()
        
