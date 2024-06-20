
def readfile(filename:str):
    with open(filename, 'r') as f:
        text = f.read().splitlines()
    return text

def is_symbol(s:str):
    if (not s.isnumeric() and  (not s == ".")): # Not a number and not a '.'
        return True
    return False

def check_around_have_symbol(s,i,j):
    for x in range(i-1,i+2):
        for y in range(j-1,j+2):
            if (x>=0) and (y>=0) and (x<len(s)) and (y<len(s[0])):
                if ( is_symbol(s[x][y]) ):
                    return True
    return False

def calculate_around_number(s,arr):
    total, mut = 0, 1
    for i,j in arr:
        thisnum = get_around_number(s,i,j)
        total += thisnum
        mut *= thisnum

        print(thisnum)
    print(total, mut)
    return total, mut

def get_around_number(s,i,j):
    output = s[i][j]
    ## go left
    for y in range(j-1,-1,-1):
        if (s[i][y].isnumeric()):
            output = s[i][y] + output
        else:
            break
    ## go right
    for x in range(j+1,len(s[0]) ):
        if (s[i][x].isnumeric()):
            output = output + s[i][x]
        else:
            break
    return int(output)



def get_around_number_pos(s,i,j):
    output = []
    same_word = []
    for x in range(i-1,i+2):
        for y in range(j-1,j+2):
            if (x>=0) and (y>=0) and (x<len(s)) and (y<len(s[0])):
                if ( s[x][y].isnumeric() ):
                    if ( [x,y-1] not in same_word):
                        output.append( [x,y] )
                    same_word.append([x,y])
    return output

def calculate_total_star(s:str):
    total = 0
    temp  = 0
    flag  = False
    stars = []
    for i in range(len(s)):
        for j in range(len(s[0])):
            ## print(i,j,s[i][j], check_around_have_symbol(s,i,j))
            if (s[i][j] == "*"):
                stars.append([i,j])
            if ( s[i][j].isnumeric()):
                temp = temp*10+int(s[i][j])
                flag = any((flag,check_around_have_symbol(s,i,j)))
            else:
                if (flag):
                    total += temp
                temp = 0
                flag = False
    return total, stars
            
def calculate_star(s,stars,total=0):
    for i,j in stars:
        number_arr = get_around_number_pos(s,i,j)
        if (len(number_arr) >= 2):
            tol, mut = calculate_around_number(s,number_arr)
            total += mut
    return total

def main():
    filename = "test2.txt"
    text_arr =readfile(filename)
    total,stars = calculate_total_star(text_arr)
    print(calculate_star(text_arr,stars,0))
    

if __name__ == '__main__':
    main()





