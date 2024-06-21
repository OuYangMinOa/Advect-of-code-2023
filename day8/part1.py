
def build_dict(s:str)->dict:
    output = {}
    for each in s[2:]:
        key   = each.split('=')[0].strip()
        value = each.split('=')[1].strip()[1:-1].split(",")
        value[1] = value[1].strip()
        output[key] = value
    return output

def readfile(filename:str):
    with open(filename, 'r') as f:
        text = f.read().splitlines()
    return text


def main():
    filename = "test2.txt"
    text_arr = readfile(filename)
    instructions = text_arr[0]
    tree = build_dict(text_arr)
    now  = 0
    count = 0
    temp = "AAA"
    while temp != "ZZZ":
        if ( now == len(instructions)):
            now = 0
        this_instruction = instructions[now]
        if (this_instruction == "L"):
            temp = tree[temp][0]
        else:
            temp = tree[temp][1]
        print(temp, count, now ,this_instruction)

        now += 1
        count += 1
    print(count)


if __name__ == '__main__':
    main()




