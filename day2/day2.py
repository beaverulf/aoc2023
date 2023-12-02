import re

max = { 'red':12, 'green':13, 'blue':14 }

def is_valid_game(line: str) -> int:
    id = re.compile(r'\bGame (?P<id>\d+)\b').search(line).group('id')
    for round in extract_rounds(line):
        for color,q in get_cubes(round):
            if q > max[color]:
                return 0
    return int(id) 

def extract_rounds(game_line:str):
    rounds = game_line.split(':')[1].split(';')
    return map(lambda line: line.strip(), rounds)
              
def get_cubes(round: str) -> list:
    matches = re.compile(r'(?P<quantity>\d+) (?P<color>\w+)').finditer(round)
    return list(map(lambda m: (m.group('color'), int(m.group('quantity'))), matches))

        
def find_minimum_cubes(game_line:str):
    min_color = { 'red':0, 'green':0, 'blue':0}
    for round in extract_rounds(game_line):
        cubes_for_round = get_cubes(round)
        for color,q in cubes_for_round:
            if q >= min_color[color]:
                min_color[color] = q
    return (min_color['red'] * min_color['green'] * min_color['blue'])

with open('./day2/data.txt', encoding="utf-8") as f:
    data = f.read().splitlines()
    total_task1 = sum(map(is_valid_game, data))
    total_task2 = sum(map(find_minimum_cubes, data))
    print(total_task1,total_task2)


       

