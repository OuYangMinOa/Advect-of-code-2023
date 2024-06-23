def readfile(filename:str):
    with open(filename, 'r') as f:
        text = f.read().splitlines()
    return text

def find_all_points(s):
    output = []
    no_galaxy_i = [True for i in range(0, len(s  ))]
    no_galaxy_j = [True for j in range(0, len(s[0]))]

    for i in range(len(s)):
        for j in range(len(s[0])):
            if (s[i][j] == "#"):
                output.append([i,j])
                no_galaxy_i[i] = False
                no_galaxy_j[j] = False
    return output, [i for i in range(len(s)) if no_galaxy_i[i]], [i for i in range(len(s[0])) if no_galaxy_j[i]]

def calculate_answer(s, factor=2):
    galaxys, gi, gj = find_all_points(s)
    print(gi, gj)
    output = 0
    for i in range(len(galaxys)-1):
        for j in range(i+1, len(galaxys)):
            this   = 0
            x1, y1 = galaxys[i]
            x2, y2 = galaxys[j]
            x1, x2 = min(x1,x2), max(x1,x2)
            y1, y2 = min(y1,y2), max(y1,y2)
            this += abs(x1-x2) + abs(y1-y2)
            for each in gi:
                if x1 <= each and each <= x2:
                    this += factor - 1
            for each in gj:
                if y1 <= each and each <= y2:
                    this += factor - 1
            output += this
    return output
            




def main():
    filename = "test2.txt"
    text_arr = readfile(filename)
    answer = calculate_answer(text_arr,1_000_000)
    print(answer)


if __name__ == '__main__':
    main()




