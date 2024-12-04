## 4th task of 2015 aocd
from utils.inputs import get_data_set
from hashlib import md5    

my_input = "bgvyzdsv"

for i in range(10000000):
    hexval = md5((my_input+str(i)).encode("utf-8")).hexdigest()[:5]
    if hexval == "00000":
        print("Found ", i)
        break


for i in range(10000000):
    hexval = md5((my_input+str(i)).encode("utf-8")).hexdigest()[:6]
    if hexval == "000000":
        print("Found ", i)
        break