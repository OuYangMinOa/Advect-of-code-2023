
# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.


MAZE_DICT = {
        "|" : [0,2],
        "-" : [1,3],
        "L" : [1,2],
        "J" : [2,3],
        "7" : [0,3],
        "F" : [0,1],
        }

def readfile(filename:str):
    with open(filename, 'r') as f:
        text = f.read().splitlines()
    return text

def find_start_point(s):
    for i in range(len(s)):
        for j in range(len(s[0])):
            if (s[i][j] == "S"):
                return i,j
    raise ValueError("No initial point found")

def find_loop_coordinate(s:list[str]):
    x, y = find_start_point(s)
    sx, sy = x, y # starting point
    out_to_in = lambda x: (x+2)%4
    output = [[x,y],]

    last_pos = None   
    if ( s[x+1][y] in [pos for pos in MAZE_DICT if 2 in MAZE_DICT[pos]]):
        x = x + 1
        last_pos = 0
    elif( s[x-1][y] in [pos for pos in MAZE_DICT if 0 in MAZE_DICT[pos]]):
        x = x - 1
        last_pos = 2
    elif ( s[x][y+1] in [pos for pos in MAZE_DICT if 1 in MAZE_DICT[pos]]):
        y = y + 1
        last_pos = 3
    elif( s[x][y-1] in [pos for pos in MAZE_DICT if 3 in MAZE_DICT[pos]]): 
        y = y - 1
        last_pos = 1
    while (x,y) != (sx, sy):
        output.append([x,y])
        this_s = s[x][y]
        last_pos = out_to_in(last_pos)
        next_pos_arr = MAZE_DICT[this_s]
        index = ( next_pos_arr.index(last_pos) +1 ) % 2
        last_pos = next_pos_arr[index]
        if (last_pos == 0):
            x += 1
        elif(last_pos == 1):
            y += 1
        elif(last_pos == 2):
            x -= 1
        elif(last_pos == 3):
            y -= 1
    return output

def find_loop_length(s):
    length, width = len(s), len(s[0])
    coor_arr = find_loop_coordinate(s)
    print(len(coor_arr))

    def check_in_loop(x,y):
        output = False
        count = 0
        i,j = x+1, y+1
        while i<length and j<width:
            if ([i,j] in coor_arr and s[i][j] not in ["7","L"]):
                count+=1
            i += 1
            j += 1
        output = ( count%2 == 1 ) or output
        # count = 0
        # i,j = x-1, y+1
        # while i>=0 and j<width:
        #     if ([i,j] in coor_arr and s[i][j] not in ["7","L"]):
        #         count+=1
        #     i -= 1
        #     j += 1
        # output = ( count%2 == 1 ) or output
        # count = 0
        # i,j = x-1, y-1
        # while i>=0 and j>=0:
        #     if ([i,j] in coor_arr and s[i][j] not in ["7","L"]):
        #         count+=1
        #     i -= 1
        #     j -= 1
        # output = ( count%2 == 1 ) or output
        # count = 0
        # i,j = x+1, y-1
        # while i<length and j>=0:
        #     if ([i,j] in coor_arr and s[i][j] not in ["7","L"]):
        #         count+=1
        #     i += 1
        #     j -= 1
        # output = ( count%2 == 1 ) or output
        return output

    count = 0 
    for i in range(1,length-1):
        for j in range(1,width-1):
            if ([i,j] not in coor_arr):
                if (check_in_loop(i,j) ):
                    count += 1
                    s[i] = s[i][:j] + "I" + s[i][j+1:]
    # print('\n\n'+'\r\n'.join(s))
    return count

def main():
    filename = "test2.txt"
    text_arr = readfile(filename)
    # print('\n'.join(text_arr))
    answer = find_loop_length(text_arr)

    print(answer)






if __name__ == '__main__':
    main()




