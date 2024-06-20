






def readfile(filename:str):
    with open(filename, 'r') as f:
        text = f.read().splitlines()
    return text

def calculate_matching(line):
    nums   = line.split(":")[1].split("|")
    winnum = set(map(int, nums[0].split()))
    mynum  = set(map(int, nums[1].split()))
    return len(list(winnum & mynum))

def calculate(line_arr):
    copies = [0 for i in range(len(line_arr))]
    for i in range(len(copies)):
        matching = calculate_matching(line_arr[i])
        copies[i] += 1
        for j in range(i+1,i+1+matching):
            copies[j] += copies[i]
    return sum(copies)


def main():
    filename = "test2.txt"
    text_arr =readfile(filename)
    total  = calculate(text_arr)
    print(total)

if __name__ == '__main__':
    main()




