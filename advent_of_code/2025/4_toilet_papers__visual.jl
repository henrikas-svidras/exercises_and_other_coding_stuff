include("utils/inputs_jl.jl")

using Plots
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

function evolve_frames_for_part2(input)
    data = parse_data(input)

    frames = Vector{Vector{Vector{Int}}}()
    removed_step = Int[]
    total_removed = Int[]

    total = 0

    push!(frames, deepcopy(data))
    push!(removed_step, 0)
    push!(total_removed, 0)

    for n = 1:10000
        removed = part1(data; remove = true)
        removed == 0 && break

        total += removed
        push!(frames, deepcopy(data))
        push!(removed_step, removed)
        push!(total_removed, total)
    end

    return frames, removed_step, total_removed
end


function grid_to_matrix(grid::Vector{Vector{Int}})
    H = length(grid)
    W = length(grid[1])
    mat = Matrix{Int}(undef, H, W)
    for y = 1:H
        for x = 1:W
            mat[y, x] = grid[y][x]
        end
    end
    return mat
end



function animate_papers(input; filename = "visuals/4.gif", fps = 20)
    frames, removed_step, total_removed = evolve_frames_for_part2(input)

    anim = @animate for (i, grid) in enumerate(frames)
        mat = grid_to_matrix(grid)

        title_str = if i == 1
            "Step 0 (initial)"
        else
            "Step $(i-1): removed $(removed_step[i]) (total $(total_removed[i]))"
        end

        heatmap(
            mat;
            axis = nothing,
            border = :none,
            colorbar = false,
            title = title_str,
            size = (600, 600),
        )
    end

    gif(anim, filename; fps = fps)
end

animate_papers(input)
