include("utils/inputs_jl.jl")

using JuliaFormatter
format(@__FILE__)

input = Utils.get_data(2025, 4)

function parse_data(input)
    papers = []

    for paper_line in input
        push!(papers, [c == '@' ? 1 : 0 for c in paper_line])
    end
    return papers
end


function part1(data; remove = false)
    H = length(data)
    W = length(data[1])

    ans = 0

    for y = 1:H
        for x = 1:W
            count = 0
            if data[y][x] == 1
                dirs =
                    ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1))
                for (dy, dx) in dirs
                    ny = y + dy
                    nx = x + dx

                    if ny in 1:H && nx in 1:W
                        count += data[ny][nx]
                    end
                end
                if count < 4
                    ans += 1
                    if remove
                        data[y][x] = 0
                    end
                end

            end
        end
    end

    return ans
end

function part2(data)
    ans = 0
    ans_last = nothing
    for i = 1:100
        ans == ans_last && break
        ans_last = ans
        ans+=part1(data; remove = true)

    end
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
