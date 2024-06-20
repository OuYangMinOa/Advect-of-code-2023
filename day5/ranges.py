from dataclasses import dataclass


@dataclass
class SeedRange:
    start:int
    range_length:int
    def __eq__(self, other):
        return self.start == other.start and self.range_length == other.range_length


class RangeStage:
    def __init__(self,s:str):
        self.each_mapping = []
        lines = s.split("\n")[1:]
        print(s.split("\n")[0])
        for each in lines:
            if (each == ""):
                break
            nums = each.split(" ")
            destination, source, range_length = int(nums[0]), int(nums[1]), int(nums[2])
            self.each_mapping.append( (destination, source, range_length) )
        self.each_mapping.sort(key = lambda x:x[1])
        # print(self.each_mapping)


    def compare_range(self,other:SeedRange)->list[SeedRange]:
        output = []
        start  = other.start
        end    = other.start + other.range_length
        while start<end:
            min_s = end 
            # between ranges
            flag = True
            for d,s,r in self.each_mapping:
                if (s <= start and start < s + r): # between a range
                    if (s + r <= end): # s <= start < s+r < end 
                        output.append(SeedRange( d + (start-s),  r - (start-s)))
                        start = s + r
                        flag = False
                        break
                    elif (end < s + r ):  # s <= start < end < s + r
                        output.append(SeedRange( d + (start-s),  (end - start) ))
                        start = end 
                        flag = False
                        break
                elif ( start < s and s < end and s < min_s): # find the closest s ( start < s1 < s2 < s3 )
                    min_s = s 
            ## No between
            if (flag): # start < min_s < ... < end
                output.append(SeedRange(start,min_s - start))
                start = min_s
        return output

    def compare_seed(seed):
        for d,s,r in self.each_mapping:
            if (self.s <= seed) and (seed < self.r + self.s):
                return self.d + (seed - self.s)
        return seed

if __name__ == "__main__":
    pass




