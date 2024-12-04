## 6th task of 2015 aocd
from utils.inputs import get_data_set
import numpy as np

data = get_data_set(2015,6)

light_array = np.zeros(shape=(1000,1000), dtype=np.int8)
light_array[:,:] = -1
#data = ["turn on 0,0 through 999,999", "turn off 499,499 through 500,500"]

for instruction in data:
    func = instruction[:7]
    if func == "turn on":
        instr = instruction.replace("turn on ","")
    elif func == "turn of":
        instr = instruction.replace("turn off ","")
    elif func == "toggle ":
        instr = instruction.replace("toggle ","")
    else:
        raise SyntaxError
    nums = instr.split(" ")
    nums1, nums2 = nums[0].split(","), nums[2].split(",")
    num_starts = int(nums1[0]), int(nums1[1]) 
    num_ends = int(nums2[0]), int(nums2[1]) 
    if func == "turn on":
        light_array[num_starts[0]:num_ends[0]+1,num_starts[1]:num_ends[1]+1] = 1
    elif func =="turn of":
        light_array[num_starts[0]:num_ends[0]+1,num_starts[1]:num_ends[1]+1] = -1
    else:
        light_array[num_starts[0]:num_ends[0]+1,num_starts[1]:num_ends[1]+1] *= -1

light_array[light_array==-1] = 0    
print("Number of lights on ", np.sum(light_array))

light_array = np.zeros(shape=(1000,1000), dtype=np.int8)
light_array[:,:] = 0

for instruction in data:
    func = instruction[:7]
    if func == "turn on":
        instr = instruction.replace("turn on ","")
    elif func == "turn of":
        instr = instruction.replace("turn off ","")
    elif func == "toggle ":
        instr = instruction.replace("toggle ","")
    else:
        raise SyntaxError
    nums = instr.split(" ")
    nums1, nums2 = nums[0].split(","), nums[2].split(",")
    num_starts = int(nums1[0]), int(nums1[1]) 
    num_ends = int(nums2[0]), int(nums2[1]) 
    if func == "turn on":
        light_array[num_starts[0]:num_ends[0]+1,num_starts[1]:num_ends[1]+1] += 1
    elif func =="turn of":
        light_array[num_starts[0]:num_ends[0]+1,num_starts[1]:num_ends[1]+1] += -1
        light_array[light_array==-1] = 0    
    else:
        light_array[num_starts[0]:num_ends[0]+1,num_starts[1]:num_ends[1]+1] += 2

light_array[light_array==-1] = 0    
print("Total brightness is ", np.sum(light_array))


