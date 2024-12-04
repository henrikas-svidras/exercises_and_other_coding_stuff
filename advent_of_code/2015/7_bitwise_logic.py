#  7th day of advent of code 2015

# My solution was inefficient, ultimnately used solution from
# https://g.c5h.io/archive/aoc-2015/src/commit/a0ac85adeb8987c7c84e45b1c75715b717977669/7.py
# Very nice one!

import re
from utils.inputs import get_data_set

data = get_data_set(2015,7)

wires = {}
functions = {
    'AND': lambda left, right: lambda: left() & right(),
    'OR': lambda left, right: lambda: left() | right(),
    'LSHIFT': lambda left, right: lambda: left() << right(),
    'RSHIFT': lambda left, right: lambda: left() >> right(),
    'NOT': lambda value: lambda: ~ value()
}

def get_wire(name):
    if (name.isdigit()):
        return int(name)

    if hasattr(wires[name], '__call__'):
        wires[name] = wires[name]()

    return wires[name]

def handle_input(text):
    binary_match = re.match('^(.*?) (AND|OR|LSHIFT|RSHIFT) (.*?)$', text)
    if binary_match:
        (left, operator, right) = binary_match.group(1, 2, 3)
        return functions[operator](lambda: get_wire(left), lambda: get_wire(right))

    unary_match = re.match('^(NOT) (.*?)$', text)
    if unary_match:
        (operator, value) = unary_match.group(1, 2)
        return functions[operator](lambda: get_wire(value))

    return lambda: get_wire(text)



for line in data:
    (input, output) = line.split(' -> ')
    wires[output] = handle_input(input)

part_1 = wires['a']()
print('Part 1: %s' % part_1)

for line in data:
    (input, output) = line.split(' -> ')
    wires[output] = handle_input(input)

wires['b'] = 16076

part_2 = wires['a']()
print('Part 2: %s' % part_2)


