include("utils/inputs_jl.jl")

using JuliaFormatter
format(@__FILE__)

input = Utils.get_data(2022, 21)

function parse_data(input)
    monkeys = Dict()
    for monkey in input
        name, shout = split(monkey, ": ")
        if any(isdigit, shout)
            monkeys[name] = parse(Int, shout)
        else
            shout = (shout[1:4], shout[6], shout[8:11])
            monkeys[name] = shout
        end
    end
    return monkeys
end

function monkey_eval(data, name; part2 = false)
    if isa(data[name], Int)
        return data[name]
    else
        first = monkey_eval(data, data[name][1])
        second = monkey_eval(data, data[name][3])
        if !part2
            op = getfield(Base, Symbol(data[name][2]))
            output = op(first, second)
            return output
        else
            return first, second
        end
    end
end

function part1(data)
    res = monkey_eval(data, "root")
    return res
end


function part2(data)
    sr_lo = 0
    sr_hi = 10^15 # guessing upper limit

    while sr_lo <= sr_hi
        mid = Int(floor((sr_lo + sr_hi)/2))
        data["humn"] = mid

        f, s = monkey_eval(data, "root"; part2 = true)

        diff = s - f

        if diff == 0
            println(mid)
            return mid
        elseif diff > 0
            sr_hi = mid - 1
        else
            sr_lo = mid + 1
        end
    end

end


data = parse_data(input)
t0 = time()
println("Part1: ", part1(data))
println("Elapsed: ", round(time() - t0; digits = 2), " seconds")

data = parse_data(input)
t0 = time()
println("Part2: ", part2(data))
println("Elapsed: ", round(time() - t0; digits = 2), " seconds")
