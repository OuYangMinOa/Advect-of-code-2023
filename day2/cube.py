from dataclasses import dataclass

@dataclass
class Cubes:
    red:int
    blue:int
    green:int
    @staticmethod
    def from_game_set(s:str):
        Cubes_dict = {
            'red':0,
            'blue':0,
            'green':0,
                }
        for each_pair in s.split(","):
            each_pair = each_pair.strip().split(" ")
            numbers = int(each_pair[0])
            colors = each_pair[1]
            Cubes_dict[colors] = numbers
        return Cubes(*Cubes_dict.values())
    def __lt__(self, other):
        return (self.red < other.red or 
                self.blue < other.blue or 
                self.green < other.green )

    def compare_and_min(self, other):
        if self.red < other.red:
            self. red = other.red
        if self.blue < other.blue:
            self.blue  = other.blue
        if self.green < other.green:
            self.green = other.green
    def get_multiply(self):
        return self.red * self.green * self.blue


