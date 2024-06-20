def readfile(filename:str):
    with open(filename, 'r') as f:
        text = f.read().splitlines()
    return text


def find_better_count(time,distance):
    print(time,distance)
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
    start, end = 1, halft
    f = lambda x: x * ( time - x ) - distance 
    while (1 < end-start):
        mid = (start + end) // 2
        if ( f(end)*f(mid) <0):
            start = mid
        elif( f(start)*f(mid) <0):
            end = mid
        if (f(mid) == 0):
            break
    if (f(mid) <= 0):
        mid += 1
    output += (halft  - mid)  *2
    return output



def main():
    filename = "test2.txt"
    text_arr =readfile(filename)
    Time = int(text_arr[0][6:].replace(" ",""))
    Distance  = int(text_arr[1][9:].replace(" ",""))
    print(f"{Time=} {Distance=}")

    print("answer:",find_better_count(30,200))
    print("answer:",find_better_count(15,40 ))
    print("answer:",find_better_count( 7,  9))
    print("answer:", find_better_count(Time ,Distance ))

if __name__ == '__main__':
    main()




