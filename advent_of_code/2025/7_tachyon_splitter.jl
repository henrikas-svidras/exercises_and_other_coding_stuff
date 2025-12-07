include("utils/inputs_jl.jl")

using JuliaFormatter
format(@__FILE__)

input = Utils.get_data(2025, 7)

function parse_data(input)
    start_coord = findfirst('S', input[1])
    start = (start_coord, 1)

    splitters = Dict{Tuple{Int,Int},Int}()
    for (y, line) in enumerate(input), (x, symbol) in enumerate(line)
        if symbol == '^'
            splitters[(x, y)] = 0
        end
    end

    # println(splitters)

    return start, splitters, length(input), length(input[1])


end

function beam_go_down(
    coord::Tuple{Int,Int},
    seen::Set{Tuple{Int,Int}},
    splitters::Dict{Tuple{Int,Int},Int},
    length::Int,
)
    new_coord = (coord[1], coord[2]+1)

    if new_coord[2] > length
        return
    end

    if new_coord in seen
        return
    else
        push!(seen, new_coord)
    end

    if haskey(splitters, new_coord)
        splitters[new_coord] = 1
        new_coord1 = (new_coord[1]-1, new_coord[2])
        new_coord2 = (new_coord[1]+1, new_coord[2])
        beam_go_down(new_coord1, seen, splitters, length)
        beam_go_down(new_coord2, seen, splitters, length)

    else
        beam_go_down(new_coord, seen, splitters, length)
    end
end

function part1(data)
    start, splitters, L, _ = data
    seen = Set{Tuple{Int,Int}}()

    beam_go_down(start, seen, splitters, L)

    return sum(values(splitters))
end

function part2(data)
    start, splitters, L, W = data

    beams = zeros(Int, W)
    beams[start[1]] = 1

    for y = 1:L
        nbeams = zeros(Int, W)

        for x = 1:W
            count = beams[x]
            if count == 0
                continue
            end

            coord = (x, y)

            if haskey(splitters, coord)
                splitters[coord] = 1

                nbeams[x-1] += count
                nbeams[x+1] += count

            else
                nbeams[x] += count
            end
        end

        beams = nbeams
    end

    return sum(beams), sum(values(splitters))
end


data = parse_data(input)
t0 = time()
println("Part1: ", part1(data))
println("Elapsed: ", round(time() - t0; digits = 2), " seconds")

data = parse_data(input)
t0 = time()
println("Part1: ", part2(data))
println("Elapsed: ", round(time() - t0; digits = 2), " seconds")
