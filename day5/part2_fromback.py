# part2 from back
from tqdm import tqdm
from multiprocessing import Pool


def readfile(filename:str):
    with open(filename, 'r') as f:
        text = f.read().split("\n\n")
    return text



def build_each(s:str):
    lines = s.split("\n")[1:]
    def func(seed):
        for each in lines:
            if (each == ""):
                break
            nums = each.split(" ")
            destination, source, range_length = int(nums[0]), int(nums[1]), int(nums[2])
            if (source <= seed) and (seed < range_length + source):
                return destination + (seed - source)
        return seed
    return func

def build_reverse(s:str):
    lines = s.split("\n")[1:]
    print(s.split("\n")[0])
    def func(dest):
        for each in lines:
            if (each == ""):
                continue 
            nums = each.split(" ")
            destination, source, range_length = int(nums[0]), int(nums[1]), int(nums[2])
            if (destination <= dest) and (dest < range_length + destination):
                return source + (dest - destination)
        return dest
    return func
    
def build_destination_to_seed(s:str):
    func_list = []
    for each in s[-1:0:-1]:
        func_list.append(build_reverse(each))
    def func(dest):
        for each in func_list:
            dest = each(dest)
        return dest
    return func


def build_seed_to_destination(s:str):
    func_list = []
    for each in s[1:]:
        func_list.append(build_each(each))
    def func(seed):
        for each in func_list:
            seed = each(seed)
        return seed
    return func

def build_check_in_seed(my_seed):
    def func(seed):
        for i in range(0,len(my_seed),2):
            if (my_seed[i] <= seed and seed < my_seed[i] + my_seed[i+1]):
                return True
        return False
    return func



def main():
    filename = "test2.txt"
    text_arr =readfile(filename)
    my_seed = list(map(int, text_arr[0][7:].split(" ")))
    print(my_seed )
    transform = build_destination_to_seed(text_arr)
    check_in_seed = build_check_in_seed(my_seed)

    start = 20283850
    while True:
        result = transform(start)
        if ( check_in_seed(result) ):
            print(start)
            break
        start += 1







if __name__ == '__main__':
    main()


