def readfile(filename:str):
    with open(filename, 'r') as f:
        text = f.read().splitlines()
    return text

def find_better_count(time,distance):
    output = 0
    halft  = time//2
    if (time%2 == 0):
        if ( halft**2 > distance ):
            output += 1
        else:
            return output
    else:
        if ( halft  * (halft + 1) > distance ):
            output += 2
        else:
            return output
    for i in range(halft-1,0,-1):
        if ( i * (time - i) <= distance ):
            return output
        output += 2
    return output



def main():
    filename = "test2.txt"
    text_arr =readfile(filename)
    Time = list(map(int, text_arr[0][6:].split()))
    Distance  = list(map(int, text_arr[1][9:].split()))
    print(f"{Time=} {Distance=}")
    answer = 1
    for t,d in zip(Time ,Distance ):
        this    = find_better_count(t,d)
        print(f"{this=}")
        answer *= this
    print(answer )

if __name__ == '__main__':
    main()




