import math



class Ghost:
    def __init__(self, tree, start ):
        self.tree = tree
        self.start  = start
    def step(self, instruct):
        if (instruct == "L"):
            self.start = self.tree[self.start][0]
        else:
            self.start = self.tree[self.start][1]
    def is_z(self):
        return self.start[-1] == "Z"

def check_all_ghost(arr):
    for each in arr:
        if (not each.is_z()):
            return True
    return False


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
    ghosts = []
    for each in tree:
        if (each[-1] == "A"):
            ghosts.append(
                    Ghost(tree, each)
                    )
    print(len(ghosts))
    ## start step
    count = 0
    now   = 0 
    while check_all_ghost(ghosts):
        print(count, now)
        if ( now == len(instructions)):
            now = 0

        for each in ghosts:
            each.step(instructions[now])
        now += 1
        count += 1
    print(count)

if __name__ == '__main__':
    main()




