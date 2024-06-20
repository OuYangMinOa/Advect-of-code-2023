from tqdm import tqdm
from multiprocessing import Pool


def readfile(filename:str):
    with open(filename, 'r') as f:
        text = f.read().split("\n\n")
    return text

def build_each(s:str):
    lines = s.split("\n")[1:]
    this_trans = {i:i for i in range(100)}
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

def build_seed_to_destination(s:str):
    func_list = []
    for each in s[1:]:
        func_list.append(build_each(each))
    def func(seed):
        for each in func_list:
            seed = each(seed)
        return seed
    return func

def get_answer(s,seed):
    return build_seed_to_destination(s)(seed)

def main():
    filename = "test2.txt"
    text_arr =readfile(filename)

    my_seed = list(map(int, text_arr[0][7:].split(" ")))
    temp_min = 1e12
    pool = Pool(16) 
    for i in range(0, len(my_seed),2):
        input_arr = [(text_arr,j) for j in range(my_seed[i], my_seed[i]+my_seed[i+1]) ]
        result = pool.starmap(get_answer,input_arr)
        temp_min = min(temp_min,min(result))
            
        print(temp_min)

if __name__ == '__main__':
    main()




