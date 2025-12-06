include("utils/inputs_jl.jl")

using JuliaFormatter
format(@__FILE__)

input = Utils.get_data(2025, 6)

function parse_data(input::Vector{String})
    vals = [parse.(Int, split(line)) for line in input[1:(end-1)]]
    vals = collect.(zip(vals...))
    ops = split(input[end])

    return vals, ops
end

function parse_data_part2(input)

    rl_read = collect(zip(input[1:(end-1)]...))
    vals = Vector{Int}[]
    sub_vals = Int[]

    for col in rl_read
        num = replace(join(col), r"\s+" => "")

        if num == ""
            push!(vals, sub_vals)
            sub_vals = Int[]
            continue
        end
        if !all(isspace, num)
            push!(sub_vals, parse(Int, num))
        end
    end

    push!(vals, sub_vals)

    return vals
end

function part1(data)
    vals, ops = data
    ans = 0
    for (terms, op_symb) in zip(vals, ops)
        op = getfield(Base, Symbol(op_symb))
        ans += op(terms...)
    end
    return ans

end

function part2(data)
    return part1(data)
end

data1 = parse_data(input)
t0 = time()
println("Part1: ", part1(data1))
println("Elapsed: ", round(time() - t0; digits = 2), " seconds")

data2 = parse_data_part2(input)
t0 = time()
println("Part2: ", part2((data2, data1[2])))
println("Elapsed: ", round(time() - t0; digits = 2), " seconds")
