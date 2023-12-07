import itertools as it
import time

def tuple_from_line(line): return tuple([int(x) for x in line.split(" ") if x.isdigit()])
    
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

def parse_seed_ranges(data):
    seeds = [int(x) for x in  data[0].split(" ") if x.isdigit()]
    return [range(start,start+amount-1) for start, amount in it.batched(seeds,2)]


def locate(seed_ranges:list[range],maps: list[list[tuple[int, int, int]]]):
    locations = []
    intervals:list[range] = []
    for sr in seed_ranges:
        print("Seed range",sr)
        for _map in maps:
            for dest,src,m in _map:
                print()
                if src <= sr.start < sr.stop <= src+m:
                    print("full overlap")
                    print(src, "<=", sr.start, "<", sr.stop, "<", src+m)
                    print(range(sr.start - src + dest, sr.stop - src + dest))
                    print(range(src, src+m))
                    intervals.append(range(src, src+m))
                    break
                if src <= sr.start <= src+m < sr.stop:
                    print("[ ) overlap")
                    print(src, "<=", sr.start, "<=", src+m, "<", sr.stop)
                if sr.start < sr.stop < src < src+m: #no overlap
                    print("no overlap")
                    intervals.append()
                
                    None
                
                    None
        print(intervals)
    print(min(map(lambda x: x.start, intervals)))
                    

def task2(data):
    seed_ranges = parse_seed_ranges(data)
    maps = parse_maps(data)
    return locate(seed_ranges,maps)
    
    
def main():
    with open('./day5/example.txt', encoding="utf-8") as f:
        data = f.read().splitlines()
        task2_score = task2(data)
        print("Task 2",task2_score)
main()
