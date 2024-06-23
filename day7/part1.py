from card import Card

def readfile(filename:str):
    with open(filename, 'r') as f:
        text = f.read().splitlines()
    return text

def calculate_answer(arr):
    output = 0
    for num, value in enumerate(arr):
        output += (num+1) * value[1]
    return output


def main():
    filename = "test2.txt"
    text_arr = readfile(filename)
    cards = list( [ each.split(" ")[0] for each in text_arr ])
    bids  = list( [ int(each.split(" ")[1]) for each in text_arr ])
    cb_arr :list = list( zip(cards, bids) )
    cb_arr.sort(key=lambda x : Card(x[0])) 
    print(f"{cb_arr}")
    print( calculate_answer(cb_arr) )

if __name__ == '__main__':
    main()




