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
        #     seed = each(seed)
        # return seed
    return func


def main():
    filename = "test2.txt"
    text_arr =readfile(filename)

    my_seed = list(map(int, text_arr[0][7:].split(" ")))
    tranform_func = build_seed_to_destination(text_arr)
    destination = list(map(tranform_func,my_seed))
    print(destination)
    print(min(destination))


if __name__ == '__main__':
    main()




