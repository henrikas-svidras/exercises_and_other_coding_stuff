include("utils/inputs_jl.jl")

using JuliaFormatter
format(@__FILE__)

input = Utils.get_data(2025, 2)

function parse_data(input)
    joined = join(input, "")
    sequences = split(joined, ",")
    ranges = []
    for sq in sequences
        a_str, b_str = split(sq, "-")
        push!(ranges, (parse(Int, a_str), parse(Int, b_str)))
    end
    return ranges
end

function is_invalid_id(s::String)
    iseven(length(s)) || return false

    half = div(length(s), 2)
    first_half = s[1:half]
    return s == first_half * first_half
end

function is_invalid_id_part2(s::String)
    L = length(s)

    for len = 1:(div(L, 2))
        iszero(mod(L, len)) || continue
        sub = s[1:len]
        if sub ^ (div(L, len)) == s
            return true
        end
    end

    return false
end

is_invalid_id(n::Integer) = is_invalid_id(string(n))
is_invalid_id_part2(n::Integer) = is_invalid_id_part2(string(n))

function part12(data)
    invalid_ids = []
    invalid_ids_p2 = []

    for (a, b) in data
        for val = a:b
            if is_invalid_id(val)
                push!(invalid_ids, val)
            end
            if is_invalid_id_part2(val)
                push!(invalid_ids_p2, val)
            end
        end
    end
    return sum(invalid_ids), sum(invalid_ids_p2)
end



data = parse_data(input)
t0 = time()
println("Part12: ", part12(data))
println("Elapsed: ", round(time() - t0; digits = 2), " seconds")
