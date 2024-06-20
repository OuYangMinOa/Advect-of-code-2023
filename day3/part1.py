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

def calculate(s:str):
    total = 0
    temp  = 0
    flag  = False
    for i in range(len(s)):
        for j in range(len(s[0])):
            ## print(i,j,s[i][j], check_around_have_symbol(s,i,j))
           if ( s[i][j].isnumeric()):
               temp = temp*10+int(s[i][j])
               flag = any((flag,check_around_have_symbol(s,i,j)))
           else:
               if (flag):
                   print(temp)
                   total += temp
               temp = 0
               flag = False
    return total
            
    

def main():
    filename = "test2.txt"
    text_arr =readfile(filename)
    print(calculate(text_arr))

if __name__ == '__main__':
    main()




