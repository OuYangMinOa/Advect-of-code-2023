
str_text_dict = {
    "one": "1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9",
}


def readfile(filename:str):
    with open(filename, 'r') as f:
        return f.read().split("\n")

def str_to_test(s:str):
    new_s = ""
    index = 0
    while index < len(s):
        flag = True
        for each in str_text_dict.keys():
            if (each[0] == s[index]):
                each_len = len(each)
                if (each == s[index:index+each_len]):
                    new_s += str_text_dict[each ]
                    flag = False
                    break
        if (flag):
            new_s += s[index]
        index += 1
    print(s, new_s)
    return new_s


def file_first_last_number(s:str):
    s = str_to_test(s)
    n = len(s)
    first_num = 0
    last_num = 0
    for i in range(n):
        if s[i].isnumeric():
            first_num = int(s[i])
    for i in range(n-1,-1,-1):
        if s[i].isnumeric():
            last_num = int(s[i])
    return  first_num+ 10*last_num


def main():
    filename = "test2.txt" 
    input_arr = readfile(filename)
    total = 0
    for each_linein in input_arr:
        this = file_first_last_number(each_linein)
        print(this)
        total += this    
    print(total)
if __name__ == '__main__':
    main()
    
