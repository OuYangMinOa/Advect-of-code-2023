import math


def build_dict(s:str)->dict:
    output = {}
    for each in s[2:]:
        key   = each.split('=')[0].strip()
        value = each.split('=')[1].strip()[1:-1].split(",")
        value[1] = value[1].strip()
        output[key] = value
    return output

def get_all_information(temp, tree, instructions):
    now = 0 
    total = 0
    count_loop = 0
    count_to_z = 0
    switch_loop = False
    switch_z   = True
    while True:
        if ( now == len(instructions)):
            now = 0
        this_instruction = instructions[now]
        if (this_instruction == "L"):
            temp = tree[temp][0]
        else:
            temp = tree[temp][1]

        # if (temp[-1] == "Z" ):
        #     print("Z found", total, now)

        if (temp[-1] == "Z" and switch_z):
            print("Z found", count_to_z)
            switch_z = False
        
        if (now == len(instructions)-1 and temp[-1] == "Z"):
            if (switch_loop):
                break
            else:
                switch_loop = True

        if (switch_z):
            count_to_z += 1

        if (switch_loop):
            count_loop += 1
        now += 1
        total += 1

    return count_to_z, count_loop, total

def readfile(filename:str):
    with open(filename, 'r') as f:
        text = f.read().splitlines()
    return text

def main():
    filename = "test2.txt"
    text_arr = readfile(filename)
    instructions = text_arr[0]
    print(len(instructions))
    tree = build_dict(text_arr)
    all_answer = []
    for each in tree:
        if (each[-1] == "A"):
            print(each)
            args = get_all_information(each, tree ,instructions)                   
            print(args)
            all_answer.append(args[1])
    print(all_answer)
    print(
            math.lcm(*all_answer)
            )


if __name__ == '__main__':
    main()




