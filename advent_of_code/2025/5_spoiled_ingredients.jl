include("utils/inputs_jl.jl")

using JuliaFormatter
format(@__FILE__)

input = Utils.get_data(2025, 5)

function parse_data(input)
    ranges = Tuple{Int,Int}[]
    ings = Int[]

    for ln in input
        if occursin('-', ln)
            nums = parse.(Int, split(ln, "-"))
            push!(ranges, (nums[1], nums[2]))
        elseif ln != ""
            push!(ings, parse(Int, ln))
        end
    end

    # println(ranges)
    # println(ings)

    return ranges, ings
end

function part1(data)
    ranges, ings = data
    ans = 0
    for ing in ings
        for r in ranges
            if ing in r[1]:r[2]
                ans+=1
                break
            end
        end
    end

    return ans

end

function part2(data)
    ranges, _ = data

    ranges = sort(ranges; by = r -> (r[1], r[2]))

    ans = 0

    cur_s, cur_e = ranges[1]

    for (new_s, new_e) in Iterators.drop(ranges, 1)

        if new_s <= cur_e
            if new_e > cur_e
                cur_e = new_e
            end
        else
            ans += cur_e - cur_s + 1
            cur_s, cur_e = new_s, new_e
        end
    end

    ans += cur_e - cur_s + 1

    return ans
end

data = parse_data(input)
t0 = time()
println("Part1: ", part1(data))
println("Elapsed: ", round(time() - t0; digits = 2), " seconds")

data = parse_data(input)
t0 = time()
println("Part2: ", part2(data))
println("Elapsed: ", round(time() - t0; digits = 2), " seconds")
