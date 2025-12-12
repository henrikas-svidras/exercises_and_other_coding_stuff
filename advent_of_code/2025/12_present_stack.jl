include("utils/inputs_jl.jl")

using JuliaFormatter
format(@__FILE__)

input = Utils.get_data(2025, 12)

function parse_data(input)
    presents_parse = []
    spaces = []
    areas = []
    present = []
    for part in input
        part == "" && continue
        if contains(part, "x")
            (area, space) = split(part, ": ")
            push!(areas, parse.(Int, split(area, "x")))
            push!(spaces, parse.(Int, split(space, " ")))
        elseif isdigit(part[1]) && length(present)>0
            push!(presents_parse, present)
            present = []
        elseif !isdigit(part[1])
            push!(present, part)
        end
    end

    presents = []
    for (_, present) in enumerate(presents_parse)
        coords = []
        for (y, line) in enumerate(present)
            for (x, part) in enumerate(line)
                if part == '#'
                    push!(coords, (x, y))
                end
            end
        end
        push!(presents, coords)
    end

    return presents, spaces, areas
end


function part1(data)
    presents, spaces, areas = data

    present_parts = [length(p) for p in presents]

    fits = []
    no_fit = []
    investigate = []
    remaining = []
    total_counts = []

    for (n, (counts, (x, y))) in enumerate(zip(spaces, areas))
        min_space = sum(c * ppc for (c, ppc) in zip(counts, present_parts))
        total_presents = sum(counts)
        area = x * y

        rem = 0

        if area >= 9 * total_presents
            push!(fits, n)
            rem = area - 9 * total_presents
        elseif min_space > area
            push!(no_fit, n)
            rem = area - min_space
        else
            push!(investigate, n)
            rem = area - min_space
        end

        push!(remaining, rem)
        push!(total_counts, total_presents)
    end

    println(length(fits))
    println(length(no_fit))
    println(length(investigate))

    for n in investigate
        # println(presents[n])

        # println(spaces[n])

        # println(areas[n])

        # println(remaining[n])

        # println(total_counts[n])

        if (remaining[n] - total_counts[n]*2) < 0
            push!(no_fit, n)
        end
    end

    println(length(no_fit))

    return nothing
end


function part2(data)

end

data = parse_data(input)
t0 = time()
println("Part1: ", part1(data))
println("Elapsed: ", round(time() - t0; digits = 2), " seconds")
