from itertools import chain
import time

def tuple_from_line(line): return tuple([int(x) for x in line.split(" ") if x.isdigit()])

def recursive_parse(value,tuples,tuples_list,i):
    if i == 6: return derive_value_fast(value,tuples)
    value = derive_value_fast(value,tuples)
    return recursive_parse(value,tuples_list[i+1],tuples_list,i+1)
        
def derive_value(value, tuples:list):
    t = time.time()

    for dest,src,m in tuples:
        #print(value,dest,src+m)
        if src <= value <= src+m:
            return value+(dest-src)
    derive_time += (time.time() - t)
    return value

def derive_value_fast(value, tuples):
    for dest,src,m in tuples:
        if src <= value <= src+m:
            return value+(dest-src)
    return value


def map_name(i):
    match i:
        case 0:
            print("seed-to-soil map:")
        case 1:
            print("soil-to-fertilizer map:")
        case 2:
            print("fertilizer-to-water map:")
        case 3:
            print("water-to-light map:")
        case 4:
            print("light-to-temperature map:")
        case 5:
            print("temperature-to-humidity map:")
        case 6:
            print("humidity-to-location map:")
        case _:
            None
def parse_maps(data)-> list[list[tuple[int,int,int]]]:
    maps = []
    tuples = []
    for i,line in enumerate(data):
        if i == 0 or "map:" in line: continue
        if line == "":
            if len(tuples) > 0:
                maps.append(sorted(tuples, key=lambda x: x[1]))
                tuples = []
            continue
        tuples.append(tuple_from_line(line))
    maps.append(sorted(tuples, key=lambda x: x[1])) #flush after last line
    return maps

def task1(data):
    seeds = [int(x) for x in  data[0].split(" ") if x.isdigit()]
    maps = parse_maps(data)
    locations = []
    for seed in seeds:
        locations.append((seed,recursive_parse(seed,maps[0],maps,0)))
    return min(locations, key=lambda x: x[1])[1]

def parse_seeds(base,tot):
    t = time.time()
    l= list(range(base, base+tot))
    print("Creating seed range",time.time()-t)
    return l

        
def parse_seed_pairs(data):
    seeds = [int(x) for x in  data[0].split(" ") if x.isdigit()]
    return [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]


def main():
    with open('./day5/example.txt', encoding="utf-8") as f:
        data = f.read().splitlines()
        task1_score= task1(data)
        print("Task 1",task1_score)

main()