## 24th task of advent of code
row = 3010
column = 3019

start_num = 20151125
res = start_num

the_1_n_value = sum(range(2,column+1))

counts = [column]

for i in range(1, row-1):
    counts.append(counts[-1]+1)

the_diff = sum(counts)

the_m_n_value = the_1_n_value + the_diff

for i in range(the_m_n_value):
    start_num = (start_num*252533)%33554393

print(start_num)