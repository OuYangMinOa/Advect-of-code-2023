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

def get_game_minimal_sets(this_game_sets:list):
    this_minimal_sets = Cubes(0,0,0)
    for game_sets in this_game_sets:
        this_Cubes = Cubes.from_game_set(game_sets)
        this_minimal_sets.compare_and_min(this_Cubes)
    return this_minimal_sets.get_multiply()




def main():
    filename = "test2.txt"
    total = 0
    for each_line in readfile(filename):
        _ , game_sets = parse_each_line(each_line)
        total += get_game_minimal_sets(game_sets)
    print(total)



if __name__ == "__main__":
    main()
