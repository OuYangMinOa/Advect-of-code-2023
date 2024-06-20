






def readfile(filename:str):
    with open(filename, 'r') as f:
        text = f.read().splitlines()
    return text

def num_to_point(num):
    return 2**(num - 1) if num > 0 else 0
 
def calculate(line):
    nums   = line.split(":")[1].split("|")
    winnum = set(map(int, nums[0].split()))
    mynum  = set(map(int, nums[1].split()))
    print(winnum, mynum,list(winnum & mynum))
    print(num_to_point(len(list(winnum & mynum))))
    return num_to_point(len(list(winnum & mynum)))

def main():
    filename = "test2.txt"
    text_arr =readfile(filename)
    total = 0
    for line in text_arr:
        total += calculate(line)
    print(total)

if __name__ == '__main__':
    main()




