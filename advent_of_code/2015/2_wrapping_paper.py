## 2nd task of 2015 aocd
from utils.inputs import get_data_set

data = get_data_set(2015,2)

paper_needs = 0
ribbon_needs = 0
for line in data:
    l, w, h = line.split("x")
    l = int(l)
    w = int(w)
    h = int(h)

    area_parts = [l*w, w*h, h*l]
    min_part = min(area_parts)
    paper_needs+= sum(area_parts)*2 + min_part

    dims = [l, w, h]
    volume = l*w*h
    dims.pop(dims.index(max(dims)))
    ribbon_needs += (sum(dims)*2)
    ribbon_needs += volume
print(f"Elves need {paper_needs} ft of paper")
print(f"Elves need {ribbon_needs} ft of ribbon")