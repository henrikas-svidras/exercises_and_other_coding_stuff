include("utils/inputs_jl.jl")

using DataStructures
using JuliaFormatter
format(@__FILE__)

input = Utils.get_data(2025, 8)

function parse_data(lines)
    pts = NTuple{3,Int}[]
    for line in lines
        line = strip(line)
        xyz = parse.(Int, split(line, ","))
        push!(pts, (xyz[1], xyz[2], xyz[3]))
    end

    return pts
end

function dist(a, b)
    dx = a[1] - b[1]
    dy = a[2] - b[2]
    dz = a[3] - b[3]
    return dx*dx + dy*dy + dz*dz
end

function build_connections(points)

    n = length(points)

    edges = Vector{Tuple{Int,Int,Int}}()

    for i = 1:(n-1)
        pi = points[i]
        for j = (i+1):n
            pj = points[j]
            d2 = dist(pi, pj)
            push!(edges, (d2, i, j))
        end
    end

    sort!(edges, by = e -> e[1])


    return edges
end

function part1(data; num_pairs = 1000)
    n = length(data)
    edges = build_connections(data)

    dsu = IntDisjointSet(n)

    for k = 1:num_pairs
        _, i, j = edges[k]
        union!(dsu, i, j)
    end

    comp_sizes = Dict{Int,Int}()

    for i = 1:n
        root = find_root!(dsu, i)

        if haskey(comp_sizes, root)
            comp_sizes[root] += 1
        else
            comp_sizes[root] = 1
        end
    end

    sizes = sort(collect(values(comp_sizes)), rev = true)

    return prod(sizes[1:3])
end

function part2(data)
    n = length(data)
    edges = build_connections(data)

    dsu = IntDisjointSet(n)

    last_i = 0
    last_j = 0

    for (d2, i, j) in edges
        if !in_same_set(dsu, i, j)
            union!(dsu, i, j)
            last_i, last_j = i, j

            if num_groups(dsu) == 1
                return data[last_i][1] * data[last_j][1]
            end
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
