include("utils/inputs_jl.jl")
using JuliaFormatter
using GLMakie
format(@__FILE__)

input = Utils.get_data(2025, 9)

function parse_data(input)
    coords = [parse.(Int, split(vals, ",")) for vals in input]
    return coords
end

function part1(coords)
    max_area = 0

    for i in eachindex(coords), j = (i+1):length(coords)
        x1, y1 = coords[i]
        x2, y2 = coords[j]

        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        if area > max_area
            max_area = area
        end
    end

    return max_area
end

function plot_coords(coords)
    xs = [c[1] for c in coords]
    ys = [c[2] for c in coords]

    fig = Figure(size = (1200, 1000), figure_padding = 5)
    ax = Axis(fig[1, 1], height = 600, width = 600)

    scatter!(ax, xs, ys, markersize = 8, color = :blue)

    hover_text = Observable("")
    label = Label(fig[2, 1], hover_text, fontsize = 14)

    reset_button = Button(fig[2, 2], label = "reset", width = 100)

    rowsize!(fig.layout, 1, Relative(0.9))
    rowsize!(fig.layout, 2, Relative(0.1))
    on(reset_button.clicks) do _
        reset_limits!(ax)
    end

    on(events(fig).mouseposition) do mp
        mouse_data = mouseposition(ax)

        if mouse_data === nothing
            hover_text[] = ""
            return
        end

        mx, my = mouse_data
        dists = sqrt.((xs .- mx) .^ 2 .+ (ys .- my) .^ 2)
        closest_idx = argmin(dists)
        hover_text[] = "nearest ($(xs[closest_idx]), $(ys[closest_idx]))"
    end

    display(fig)

    while isopen(fig.scene)
        sleep(0.1)
    end

    return fig
end

function part2(coords)
    plot_coords(coords)

    x1, y1 = (94645, 50248) # This is the upper edge in the circle "cut in"
    # Now I will try to find the possible diagonal candidates for input

    y2 = 0
    prev_y2 = 0
    for i in eachindex(sort(coords, by = x -> x[1]))
        (x2, y2) = coords[i]
        if x2 < x1
            for k = (i-1):-1:1
                if coords[k][2] < y2
                    prev_y2 = coords[k][2]
                    break
                end
            end
            break
        end
    end

    candidates = []

    for j = prev_y2:y2
        for k in eachindex(coords)
            if coords[k][2] == j && coords[k][1] < x1
                push!(candidates, coords[k])
            end
        end
    end

    # one of these candidates will be the other corner of the rectangle,
    # my results are Any[[5942, 67632], [5135, 67632], [94492, 68060]]
    # the third is clearly too close to the first point, so its one if the first two
    # do a visual review to find which one
    # in my case its (5942, 67632)
    println(candidates)

    return (94645 - 5942 + 1) * (67632 - 50248 + 1)
end


data = parse_data(input)
t0 = time()
println("Part1: ", part1(data))
println("Elapsed: ", round(time() - t0; digits = 2), " seconds")

data = parse_data(input)
t0 = time()
println("Part2: ", part2(data))
println("Elapsed: ", round(time() - t0; digits = 2), " seconds")
