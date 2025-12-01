include("utils/inputs_jl.jl")

using JuliaFormatter
format(@__FILE__)

input = Utils.get_data(2025, 1)

function parse_data(input)
    return input
end

move(loc, steps) = mod(loc + steps, 100)

function part1(data)
    loc = 50
    res = 0
    for turn in data
        dir = turn[1] == 'L' ? -1 : 1
        amt = parse(Int, turn[2:length(turn)])
        loc = move(loc, dir * amt)

        if loc == 0
            res+=1
        end

    end
    return res
end

function hits_zero(loc, dir, amt)
    if dir == 1
        dist_to_zero = (100 - loc) % 100
    else
        dist_to_zero = loc % 100
    end

    # if on 0
    if dist_to_zero == 0
        dist_to_zero = 100
    end

    # if small step
    if dist_to_zero > amt
        return 0
    end

    # otherwise we have at least 1 step
    return 1 + div((amt - dist_to_zero), 100)
end

function part2(data)
    loc = 50
    res = 0
    for turn in data
        dir = turn[1] == 'L' ? -1 : 1
        amt = parse(Int, turn[2:length(turn)])

        res += hits_zero(loc, dir, amt)

        loc = move(loc, dir * amt)


    end

    return res
end

data = parse_data(input)
t0 = time()
println("Part1: ", part1(data))
println("Elapsed: ", round(time() - t0; digits = 2), " seconds")

data = parse_data(input)
t0 = time()
println("Part2: ", part2(data))
println("Elapsed: ", round(time() - t0; digits = 2), " seconds")
