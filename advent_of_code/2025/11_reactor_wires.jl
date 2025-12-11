include("utils/inputs_jl.jl")

using DataStructures: OrderedSet
using Graphs
using JuliaFormatter
format(@__FILE__)

input = Utils.get_data(2025, 11)

function parse_data(input)
    connections = Dict()
    for line in input
        node, attached = split(line, ": ")
        connections[node] = split(attached, " ")
    end
    return connections
end

function count_paths(data, start, dest)
    total = 0
    path_counts = Dict(start => 1)

    while !isempty(path_counts)
        next_path_counts = Dict()

        for (node, count) in path_counts
            if node == dest
                total += count
                continue
            elseif node == "out"
                continue
            else
                for next_node in data[node]
                    next_path_counts[next_node] =
                        get(next_path_counts, next_node, 0) + count
                end
            end
        end

        path_counts = next_path_counts
    end

    return total
end


function part1(data)

    cnt = count_paths(data, "you", "out")
    return cnt
end


function part2(data)
    cnt =
        count_paths(data, "svr", "fft") *
        count_paths(data, "fft", "dac") *
        count_paths(data, "dac", "out")

    # this one is = 0 in my solution
    # cnt2 =
    #     count_paths(data, "svr", "dac") *
    #     count_paths(data, "dac", "fft") *
    #     count_paths(data, "fft", "out")


    return cnt
end



data = parse_data(input)
t0 = time()
println("Part1: ", part1(data))
println("Elapsed: ", round(time() - t0; digits = 2), " seconds")

data = parse_data(input)
t0 = time()
println("Part2: ", part2(data))
println("Elapsed: ", round(time() - t0; digits = 2), " seconds")
