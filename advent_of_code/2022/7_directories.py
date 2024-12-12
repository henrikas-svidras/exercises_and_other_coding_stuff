## 7th task of aaocd
from utils.inputs import get_data_set, get_test_data_set
import time
import typing

data = get_data_set(2022,7, raw=True)
# data = """
# $ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k
# """
def process_data(data=data):
    return data.split("\n$")

class Dir:
    def __init__(self, name, above):
        self.level = above.level +1 if above else 0
        self.above = above
        self.name = name
        self.below = dict()
        self.size = None
    
    def add_dir(self, name):
        if not name in self.below: 
            self.below[name] = Dir(name, self)

    def add_file(self, name, size):
        if not name in self.below: 
            self.below[name] = File(self, name, size)

    def get_size(self):
        if self.size is None:
            self.size = 0
            for obj in self.below.values():
                self.size += obj.get_size()
        
        return self.size

    def get_obj(self, name):
        return self.below[name]
    
    
    def __str__(self):
        return f"- {self.name} ({self.get_size()})"
    
    def print_tree(self, prefix=""):
        ans = 0
        for below in self.below.values():
            print(prefix, below)
            if isinstance(below, Dir):
                below.print_tree(prefix+"\t")
        return ans
            

    
class File:
    def __init__(self, dir, name, size):
        self.dir = dir
        self.name = name
        self.size = size
    
    def get_size(self):
        return self.size
    
    def __str__(self):
        return f"{self.name} ({self.size})"
    
    def __repr__(self):
        return f"{self.name}"

def get_wrong_size(directory):
    ans = 0
    if directory.get_size() < 100000:
        ans+=directory.size
    for subdir in directory.below.values():
        if isinstance(subdir, Dir):
            ans+= get_wrong_size(subdir)
    
    return ans

def get_super_wrong_size(directory):
    ans = []
    ans+=[directory.size]
    for subdir in directory.below.values():
        if isinstance(subdir, Dir):
            ans+= get_super_wrong_size(subdir)
    
    return ans


def part1(inp):
    top_dir = Dir("/", None)
    current_dir = top_dir
    for line in inp:
        print(line)
        if line[1:3] == "cd":
            if line[4:] == "..":
                current_dir = current_dir.above
            elif line[4:] == "/":
                current_dir = top_dir
            else:
                current_dir.add_dir(line[4:])
                current_dir = current_dir.get_obj(line[4:])
        
        if line[1:3] == "ls":
            for obj in line[4:].split("\n"):
                if not obj:
                    continue
                size, name = obj.split(" ")
                if size == "dir":
                    continue
                current_dir.add_file(name, int(size))        
    print(top_dir)
    top_dir.print_tree(prefix="\t")
    ans = get_wrong_size(top_dir)
    ans2 = sorted(get_super_wrong_size(top_dir))
    print(ans2)
    top = ans2.pop()
    free_space = 70000000 - top
    needed_space = 30000000 - free_space
    val = float("inf")
    while len(ans2)!=0:            
        next_val = ans2.pop()
        if next_val < needed_space:
            break
        val = next_val



    
    return ans, val


def part2(inp):

    return "n/a"
        
start = time.time()

res1 = part1(process_data())
print(f"Part 1 took: {(time.time() - start):.2f}s")
print(f"Result of part 1: {res1} ")

res2 = part2(process_data())
print(f"Part 2 took: {(time.time() - start):.2f}s")
print(f"Result of part 2: {res2}")

