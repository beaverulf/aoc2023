import itertools as it 
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

def task2(data):
    seeds = parse_seed_ranges(data)
    maps = parse_maps(data)
    minval = 9999999999999999999999
    for sr in seeds:
        locations = []
        t1 = time.time()
        print("Doing sr",sr)
        for seed in sr:
            locations.append((seed,recursive_parse(seed,maps[0],maps,0)))
        x = min(locations, key=lambda x: x[1])[1]
        if x <= minval:
            minval = x
        print("current lowerst",minval)
        print("took",time.time() - t1)
    return minval

def parse_seeds(base,tot):
    t = time.time()
    l= list(range(base, base+tot))
    print("Creating seed range",time.time()-t)
    return l

def parse_seed_ranges(data):
    seeds = [int(x) for x in  data[0].split(" ") if x.isdigit()]
    return [range(start,start+amount) for start, amount in it.batched(seeds,2)]
        


def main():
    with open('./day5/example.txt', encoding="utf-8") as f:
        data = f.read().splitlines()
        task2_score= task2(data)
        print("Task 2",task2_score)

main()