include("utils/inputs_jl.jl")

using JuMP, HiGHS
using JuliaFormatter
format(@__FILE__)

input = Utils.get_data(2025, 10)

function parse_data(input)
    parsed = split.(input, " ")
    buttons = []
    joltages = []
    lights = []
    for line in parsed
        push!(lights, [val=='#' for val in collect(line[1])[2:(end-1)]])

        push!(
            buttons,
            [
                [parse(Int, string(c)) for c in token if isdigit(c)] for
                token in collect.(line[2:(end-1)])[1:(end)]
            ],
        )

        push!(joltages, parse.(Int, split(line[end][2:(end-1)], ',')))
    end
    return lights, buttons, joltages
end

function min_presses(light, buttons)

    model = Model(HiGHS.Optimizer)
    set_silent(model)

    @variable(model, presses[1:length(buttons)] >= 0, Int)
    @variable(model, k[1:length(light)] >= 0, Int)

    for i = 1:length(light)
        target = light[i] ? 1 : 0

        @constraint(
            model,
            sum(presses[j] for j = 1:length(buttons) if (i - 1) in buttons[j]) ==
            target + 2 * k[i]
        )
    end

    @objective(model, Min, sum(presses))

    optimize!(model)


    return Int(round(objective_value(model)))
end



function min_presses_jolts(joltages, buttons)

    model = Model(HiGHS.Optimizer)
    set_silent(model)

    @variable(model, presses[1:length(buttons)] >= 0, Int)

    for i = 1:length(joltages)
        @constraint(
            model,
            sum(presses[j] for j = 1:length(buttons) if (i - 1) in buttons[j]) ==
            joltages[i]
        )
    end

    @objective(model, Min, sum(presses))

    optimize!(model)

    return Int(round(objective_value(model)))
end




function part1(data)
    (lights, buttons, _) = data

    total = 0
    for (l, b) in zip(lights, buttons)
        res = min_presses(l, b)
        total += res
    end

    return total
end

function part2(data)
    (_, buttons, joltages) = data

    total = 0
    for (j, b) in zip(joltages, buttons)
        res = min_presses_jolts(j, b)
        total += res
    end

    return total
end


data = parse_data(input)
t0 = time()
println("Part1: ", part1(data))
println("Elapsed: ", round(time() - t0; digits = 2), " seconds")

data = parse_data(input)
t0 = time()
println("Part2: ", part2(data))
println("Elapsed: ", round(time() - t0; digits = 2), " seconds")
