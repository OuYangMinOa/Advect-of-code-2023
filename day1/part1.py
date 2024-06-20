def readfile(filename):
    with open(filename, 'r') as f:
        return f.read().split("\n")

def file_first_last_number(s:str):
    n = len(s)
    first_num = 0
    last_num = 0
    for i in range(n):
        if s[i].isnumeric():
            first_num = int(s[i])
    for i in range(n-1,-1,-1):
        if s[i].isnumeric():
            last_num = int(s[i])
    return  first_num+ 10*last_num


def main():
    filename = "test2.txt" 
    input_arr = readfile(filename)
    total = 0
    for each_line in input_arr:
        total += file_first_last_number(each_line)
    print(total)
if __name__ == '__main__':
    main()
    
