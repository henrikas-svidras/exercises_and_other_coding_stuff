include("utils/inputs_jl.jl")
using .Utils
using Plots
using Statistics
using Pkg
using JuliaFormatter
format(@__FILE__)

input = Utils.get_data(2022, 17; raw = true)

# I precoded the rocks into coords for easier handling later
rocks = [
    [(3, 1), (4, 1), (5, 1), (6, 1)],
    [(4, 1), (3, 2), (4, 2), (5, 2), (4, 3)],
    [(3, 1), (4, 1), (5, 1), (5, 2), (5, 3)],
    [(3, 1), (3, 2), (3, 3), (3, 4)],
    [(3, 1), (4, 1), (3, 2), (4, 2)],
]

# The "#" is optional kinda but useful if I want to draw for debuggind
world = Dict{Tuple{Int,Int},String}(
    (1, 0)=>"#",
    (2, 0)=>"#",
    (3, 0)=>"#",
    (4, 0)=>"#",
    (5, 0)=>"#",
    (6, 0)=>"#",
    (7, 0)=>"#",
)

# GLOBALS
seen = Dict{Tuple{Tuple{Vararg{Int}},Int,Int},Tuple{Int,Int}}()
const TARGET = 1_000_000_000_000
const STABILITY_THRESHOLD = 5000

heights = Int[]

# HELPERS
function parse_data(data::String)::String
    data = replace(data, "\n"=>"")
    data = replace(data, " "=>"")
    return data
end

function get_top_of_tower()::Tuple{Int,Int}
    return argmax(k -> k[2], keys(world))
end

function get_top_of_tower_all(
    wind_idx::Int,
    rock_idx::Int,
)::Tuple{Tuple{Vararg{Int}},Int,Int}
    top_y = maximum(k[2] for k in keys(world))
    xs = [x for (x, y) in keys(world) if y == top_y]
    return (Tuple(sort(xs)), wind_idx, rock_idx)
end

function add_rock(rock::Vector{Tuple{Int,Int}})::Vector{Tuple{Int,Int}}
    current_rock = Dict()

    k = get_top_of_tower()
    current_rock = [(r[1], k[2]+3+r[2]) for r in rock]

    return current_rock
end

function push_rock(current_rock::Vector{Tuple{Int,Int}}, wind::Char)::Vector{Tuple{Int,Int}}
    if wind == '>'
        moved_rock = [(cr[1]+1, cr[2]) for cr in current_rock]
    elseif wind == '<'
        moved_rock = [(cr[1]-1, cr[2]) for cr in current_rock]
    else
        error("something wrong, wind is $wind")
    end

    if all(r -> (r[1] in 1:7) && !haskey(world, r), moved_rock)
        return moved_rock
    else
        return current_rock
    end

end

function drop_rock(current_rock::Vector{Tuple{Int,Int}})::Tuple{Vector{Tuple{Int,Int}},Bool}
    dropped_rock = [(cr[1], cr[2]-1) for cr in current_rock]

    if any(r -> haskey(world, (r[1], r[2])), dropped_rock)
        return current_rock, false
    else
        return dropped_rock, true
    end
end

function draw_world()::Nothing
    xs = [k[1] for k in keys(world)]
    ys = [k[2] for k in keys(world)]

    xmin, xmax = extrema(xs)
    ymin, ymax = extrema(ys)
    for y in reverse(ymin:ymax)
        for x = xmin:xmax
            print(get(world, (x, y), "."))
        end
        println()
    end
end

# MAIN LOOP
function part12(data, world)::Nothing
    wind_it = Iterators.cycle(data)
    rock_it = Iterators.cycle(rocks)
    state = -1
    falling = false

    for (i, rock) in enumerate(rock_it)

        if !falling
            current_rock = add_rock(rock)
            falling = true
        end

        while falling
            wind, state = iterate(wind_it, state)
            current_rock = push_rock(current_rock, wind)
            current_rock, falling = drop_rock(current_rock)
        end

        for piece in current_rock
            world[piece] = "#"
        end

        #draw_world()

        k = get_top_of_tower()
        kk = get_top_of_tower_all((state-1)%length(data), (i-1)%length(rocks))

        h = k[2]
        push!(heights, h)

        if i == 2022
            k = get_top_of_tower()
            println("Part 1 answer: $(k[2])")
        end

        ## No cycle finding before initial period of stability
        ## Allowing it to look for cycles before it finds random stuff
        if i < STABILITY_THRESHOLD
            seen[kk] = (i, h)
            continue
        end

        # Find cycles
        if haskey(seen, kk)
            i_prev, h_prev = seen[kk]
            cycle_len = i - i_prev
            cycle_gain = h - h_prev

            remaining = TARGET - i
            ncycles = remaining ÷ cycle_len
            rem = remaining % cycle_len

            final_height = h + ncycles * cycle_gain + (heights[i_prev+rem] - h_prev)
            println("Part 2 answer: $final_height")
            return
        else
            seen[kk] = (i, h)
        end



    end
end

# CALLING
data = parse_data(input)
t0 = time()
part12(data, world)
println("Elapsed: ", round(time() - t0; digits = 2), " seconds")
