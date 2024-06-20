# part2 
from tqdm import tqdm
from multiprocessing import Pool
from ranges import RangeStage, SeedRange

def readfile(filename:str):
    with open(filename, 'r') as f:
        text = f.read().split("\n\n")
    return text

def remove_repucate(ranges:list[SeedRange]):
    output  = [ranges[0], ]
    for each in ranges[1:]:
        if (each == output[-1]):
            continue
        elif (output[-1].start + output[-1].range_length == each.start):
            output[-1].range_length += each.range_length
        else:
            output.append(each)
    return output
            


def range_seed_to_dest(ranges:list[SeedRange],s:str): 
    for each in s[1:]:
        new_ranges = []
        thisStage = RangeStage(each)
        for eachrange in ranges:
            new_ranges.extend(thisStage.compare_range(eachrange))
        print(len(new_ranges))
        ranges = new_ranges.copy()
        # ranges.sort(key = lambda x:x.start)
        # ranges = remove_repucate(ranges)
    return ranges

def my_seed_to_Seedrange(seeds):
    output = []
    for i in range(0, len(seeds),2):
        output.append(SeedRange(seeds[i], seeds[i+1]))
    return output 

def main():
    filename = "test2.txt"
    text_arr =readfile(filename)

    my_seed = list(map(int, text_arr[0][7:].split(" ")))
    seed_ranges =   my_seed_to_Seedrange(my_seed)
    answer = float("inf")

    for each in range_seed_to_dest(seed_ranges, text_arr):
        if (each.start < answer):
            answer = each.start

    print(answer)
    

if __name__ == '__main__':
    main()




