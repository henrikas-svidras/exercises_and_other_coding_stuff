include("utils/inputs_jl.jl")

using JuliaFormatter
format(@__FILE__)

input = Utils.get_data(2025, 3)

function parse_data(input)
    bank_nums = [parse.(Int, string.(collect(bank))) for bank in input]
    return bank_nums
end

function drop_lowest(num_list)
    n = length(num_list)
    idx = n

    for i = 1:(n-1)
        if num_list[i] < num_list[i+1]
            idx = i
            break
        end
    end

    return vcat(num_list[1:(idx-1)], num_list[(idx+1):end])
end

function part12(data, keep)
    ans = 0

    for bank in data
        curr = Int[]

        for num in reverse(bank)
            pushfirst!(curr, num)
            if length(curr) > keep
                curr = drop_lowest(curr)
            end
        end

        ans += parse(Int, join(curr))
    end

    return ans
end

data = parse_data(input)
t0 = time()
println("Part1: ", part12(data, 2))
println("Elapsed: ", round(time() - t0; digits = 2), " seconds")

data = parse_data(input)
t0 = time()
println("Part2: ", part12(data, 12))
println("Elapsed: ", round(time() - t0; digits = 2), " seconds")
