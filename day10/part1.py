
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
        for j in range(len(s)):
            if (s[i][j] == "S"):
                return i,j
    raise BaseException("No starting point error")

#   2
# 3   1
#   0

# x
# |
# +
#
# 
# 
# y - + 

def find_loop_length(s:list[str]):
    x, y = find_start_point(s)
    sx, sy = x, y # starting point
    count = 1
    out_to_in = lambda x: (x+2)%4

    last_pos = None   
    if ( s[x+1][y] in [pos for pos in MAZE_DICT if 0 in MAZE_DICT[pos]]):
        x = x + 1
        last_pos = 0
    elif( s[x+1][y] in [pos for pos in MAZE_DICT if 2 in MAZE_DICT[pos]]):
        x = x - 1
        last_pos = 2
    elif ( s[x][y+1] in [pos for pos in MAZE_DICT if 3 in MAZE_DICT[pos]]):
        y = y + 1
        last_pos = 3
    elif( s[x][y-1] in [pos for pos in MAZE_DICT if 1 in MAZE_DICT[pos]]): 
        y = y - 1
        last_pos = 1
    print(last_pos)
    while (x,y) != (sx, sy):
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
        count += 1
    return count//2

        




            





def main():
    filename = "test2.txt"
    text_arr = readfile(filename)

    answer = find_loop_length(text_arr)

    print(answer)






if __name__ == '__main__':
    main()




