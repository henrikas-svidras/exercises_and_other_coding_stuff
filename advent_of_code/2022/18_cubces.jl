include("utils/inputs_jl.jl")
using Pkg
using JuliaFormatter
format(@__FILE__)

input = Utils.get_data(2022, 18)

function parse_data(d::Vector{String})::Vector{Tuple{Int,Int,Int}}
    cleaned = Tuple{Int,Int,Int}[]
    for c in d
        x, y, z = split(c, ",")
        x, y, z = parse(Int, x), parse(Int, y), parse(Int, z)
        push!(cleaned, (x, y, z))
    end
    return cleaned
end


neighbors = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

function in_bounds(p)

end

function part1(cubes::Vector{Tuple{Int,Int,Int}})::Int
    S = Vector{Tuple{Int,Int,Int}}(cubes)
    area = 0
    for (x, y, z) in S
        for (dx, dy, dz) in neighbors
            if ! ((x+dx, y+dy, z+dz) in S)
                area += 1
            end
        end
    end
    return area
end


function part2(cubes::Vector{Tuple{Int,Int,Int}})::Int
    S = Vector{Tuple{Int,Int,Int}}(cubes)

    xs = [c[1] for c in S]
    ys = [c[2] for c in S]
    zs = [c[3] for c in S]


    xmin, xmax = minimum(xs)-1, maximum(xs)+1
    ymin, ymax = minimum(ys)-1, maximum(ys)+1
    zmin, zmax = minimum(zs)-1, maximum(zs)+1



    start = (xmin, ymin, zmin)
    queue = [start]
    visited = Set{Tuple{Int,Int,Int}}((start,))

    area = 0
    while !isempty(queue)
        x, y, z = popfirst!(queue)
        for (dx, dy, dz) in neighbors
            nb = (x+dx, y+dy, z+dz)

            if nb in S
                area += 1
            elseif (
                xmin <= nb[1] <= xmax && ymin <= nb[2] <= ymax && zmin <= nb[3] <= zmax
            ) && !(nb in visited)
                push!(visited, nb)
                push!(queue, nb)
            end
        end
    end

    return area
end

data = parse_data(input)
t0 = time()
println("Part1: ", part1(data))
println("Part2: ", part2(data))
println("Elapsed: ", round(time() - t0; digits = 2), " seconds")
