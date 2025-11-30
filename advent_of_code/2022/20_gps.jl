include("utils/inputs_jl.jl")

using JuliaFormatter
format(@__FILE__)

input = Utils.get_data(2022, 20)

function parse_data(input, multip = 1)
    original = [parse(Int, n)*multip for n in input]
    numbers = [(i, original[i]) for i in range(1, length(original))]

    return numbers, original
end


function part1(data)
    numbers, original = data
    seq_length = length(original)
    for i in range(1, seq_length)
        idx = findfirst(t -> t[1] == i, numbers)
        number = numbers[idx]
        numbers = deleteat!(numbers, idx)
        new_idx = mod(idx - 1 + number[2], seq_length-1) + 1
        insert!(numbers, new_idx, number)

    end

    # println.(map(t -> t[2], numbers))
    zero_idx = findfirst(t -> t[2] == 0, numbers)

    v1 = numbers[mod(zero_idx-1+1000, seq_length)+1][2]
    v2 = numbers[mod(zero_idx-1+2000, seq_length)+1][2]
    v3 = numbers[mod(zero_idx-1+3000, seq_length)+1][2]

    return v1 + v2 + v3

end


function part2(data)
    numbers, original = data
    seq_length = length(original)
    for ii in range(1, 10)
        println(ii)
        for i in range(1, seq_length)
            idx = findfirst(t -> t[1] == i, numbers)
            number = numbers[idx]
            numbers = deleteat!(numbers, idx)
            new_idx = mod(idx - 1 + number[2], seq_length-1) + 1
            insert!(numbers, new_idx, number)

        end
    end

    # println.(map(t -> t[2], numbers))
    zero_idx = findfirst(t -> t[2] == 0, numbers)

    v1 = numbers[mod(zero_idx-1+1000, seq_length)+1][2]
    v2 = numbers[mod(zero_idx-1+2000, seq_length)+1][2]
    v3 = numbers[mod(zero_idx-1+3000, seq_length)+1][2]

    return v1 + v2 + v3
end

data = parse_data(input)
t0 = time()
println("Part1: ", part1(data))
println("Elapsed: ", round(time() - t0; digits = 2), " seconds")

data = parse_data(input, 811589153)
t0 = time()
println("Part2: ", part2(data))
println("Elapsed: ", round(time() - t0; digits = 2), " seconds")
