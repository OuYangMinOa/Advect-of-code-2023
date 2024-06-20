from cube import Cubes

def readfile(filename:str):
    with open(filename, 'r') as f:
        text = f.read().splitlines()
    return text

def parse_each_line(lines):
    line_split = lines[5:].split(":")
    id = int(line_split[0])

    game_sets = line_split[1].split(';')
    return id, game_sets

def check_game_sets(base_game_Cubes:Cubes, this_game_sets:list, id :int):
    for game_sets in this_game_sets:
        this_Cubes = Cubes.from_game_set(game_sets)
        print(id,this_Cubes,this_Cubes > base_game_Cubes)
        if (this_Cubes > base_game_Cubes): # Check if any cube greater then base's
            return False
            break
    return True 

def main():
    filename = "test2.txt"
    base = Cubes(12,14,13)
    total = 0
    for each_line in readfile(filename):
        id, game_sets = parse_each_line(each_line)
        if (check_game_sets(base,game_sets,id)):
            total += id
            print(" >",id)
    print(total)



if __name__ == "__main__":
    main()

