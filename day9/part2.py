
def readfile(filename:str):
    with open(filename, 'r') as f:
        text = f.read().splitlines()
    return text

def build_sub_arr(arr):
    return [ arr[i+1] - arr[i] for i in range(len(arr)-1)]

def all_zero(arr):
    for each in arr:
        if (each!=0):
            return False
    return True

def get_final_answer(arr):
    sub_2d = [arr,]
    while True:
        this_sub = build_sub_arr(sub_2d[-1])
        sub_2d.append(this_sub)
        if (all_zero(this_sub)):
            break
    # print(sub_2d)
    
    for i in range(len(sub_2d)-2,-1,-1):
        this_answer = sub_2d[i][0] - sub_2d[i+1][0]
        sub_2d[i].insert(0,this_answer)
    # print(sub_2d)
    return sub_2d[0][0]



def main():
    filename = "test2.txt"
    text_arr = readfile(filename)
    total = 0
    for eachline in text_arr:
        eachline = list(map(int,eachline.split()))
        answer = get_final_answer(eachline)
        total += answer
    print(total)
if __name__ == '__main__':
    main()





