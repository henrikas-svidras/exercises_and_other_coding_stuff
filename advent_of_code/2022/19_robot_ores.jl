include("utils/inputs_jl.jl")
using Pkg
using JuliaFormatter
using Memoize
format(@__FILE__)

input = Utils.get_data(2022, 19)

struct Blueprint
    ore::Int
    clay::Int
    obsidian::NTuple{2,Int}
    geode::NTuple{2,Int}
    max_ore::Int
    max_clay::Int
    max_obs::Int
end

mutable struct Inventory
    ore::Int
    clay::Int
    obsidian::Int
    geode::Int
end

mutable struct Robots
    ore::Int
    clay::Int
    obsidian::Int
    geode::Int
end

function parse_data(d::Vector{String})
    blueprints = Dict{Int,Blueprint}()
    for (i, bp) in enumerate(d)

        function extract_numbers(line::String)
            return [parse(Int, m.match) for m in eachmatch(r"\d+", line)]
        end

        result = extract_numbers(bp)

        # println(result)

        cost_robot = result[2]
        cost_clay = result[3]
        cost_obs = (result[4], result[5])
        cost_geode = (result[6], result[7])
        max_ore = max(cost_robot, cost_clay, cost_obs[1], cost_geode[1])
        max_clay = cost_obs[2]
        max_obs = cost_geode[2]

        blueprints[i] = Blueprint(
            cost_robot,
            cost_clay,
            cost_obs,
            cost_geode,
            max_ore,
            max_clay,
            max_obs,
        )
    end

    # println(blueprints)
    return blueprints
end

const WORK_CACHE = Dict{NTuple{15,Int},Int}()  # 6 (bp) + 4 (inv) + 4 (rb) + 1 time
const T = Ref(0)
const BEST = Ref(0)

function work(blueprint::Blueprint, inventory::Inventory, robots::Robots, n::Int)::Int

    remaining_time = T[] - n

    ## OPTIMISATION 1: if there is too much material just clamp to max
    cap_ore = remaining_time * blueprint.max_ore
    cap_clay = remaining_time * blueprint.max_clay
    cap_obs = remaining_time * blueprint.max_obs

    inv_ore_k = min(inventory.ore, cap_ore)
    inv_clay_k = min(inventory.clay, cap_clay)
    inv_obs_k = min(inventory.obsidian, cap_obs)
    inv_geo_k = inventory.geode
    ####

    key = (
        blueprint.ore,
        blueprint.clay,
        blueprint.obsidian[1],
        blueprint.obsidian[2],
        blueprint.geode[1],
        blueprint.geode[2],
        inv_ore_k,
        inv_clay_k,
        inv_obs_k,
        inv_geo_k,
        robots.ore,
        robots.clay,
        robots.obsidian,
        robots.geode,
        n,
    )

    if haskey(WORK_CACHE, key)
        return WORK_CACHE[key]
    end


    can_ore =
        inventory.ore >= blueprint.ore &&
        remaining_time > 0 &&
        robots.ore < blueprint.max_ore
    can_clay =
        inventory.ore >= blueprint.clay &&
        remaining_time > 0 &&
        robots.clay < blueprint.max_clay
    can_obs =
        inventory.ore >= blueprint.obsidian[1] &&
        inventory.clay >= blueprint.obsidian[2] &&
        remaining_time > 0 &&
        robots.obsidian < blueprint.max_obs
    can_geo =
        inventory.ore >= blueprint.geode[1] &&
        inventory.obsidian >= blueprint.geode[2] &&
        remaining_time > 0

    inv_after = Inventory(
        inventory.ore + robots.ore,
        inventory.clay + robots.clay,
        inventory.obsidian + robots.obsidian,
        inventory.geode + robots.geode,
    )

    ## SECOND OPTIMISATION: if theoretically cant afford more geodes then best, just stop here
    optimistic_upper_bound =
        inv_after.geode + robots.geode*(remaining_time) + sum(1:((remaining_time)+1))
    if optimistic_upper_bound <= BEST[]
        WORK_CACHE[key] = 0
        return 0
    end
    ####

    results = Int[inv_after.geode]

    # THIRD OPTIMISATION: ALWAYS GO FOR GEO (Greedy but for works because obsidian is used only for Geo. That means not building just loses Geo). At least in my head seems logical, but idk
    if can_geo
        r2 = Robots(robots.ore, robots.clay, robots.obsidian, robots.geode + 1)
        i2 = Inventory(
            inv_after.ore - blueprint.geode[1],
            inv_after.clay,
            inv_after.obsidian - blueprint.geode[2],
            inv_after.geode,
        )
        push!(results, work(blueprint, i2, r2, n+1))
    else
        # FOURTH OPTIMISATION: pruning branches where it is no longer possible to build anything
        if inventory.ore + robots.ore * remaining_time >= remaining_time * blueprint.max_ore
            can_ore = false
        end
        if inventory.clay + robots.clay * remaining_time >=
           remaining_time * blueprint.max_clay
            can_clay = false
        end
        if inventory.obsidian + robots.obsidian * remaining_time >=
           remaining_time * blueprint.max_obs
            can_obs = false
        end
        if can_obs
            r2 = Robots(robots.ore, robots.clay, robots.obsidian + 1, robots.geode)
            i2 = Inventory(
                inv_after.ore - blueprint.obsidian[1],
                inv_after.clay - blueprint.obsidian[2],
                inv_after.obsidian,
                inv_after.geode,
            )
            push!(results, work(blueprint, i2, r2, n+1))
        end
        if can_clay
            r2 = Robots(robots.ore, robots.clay + 1, robots.obsidian, robots.geode)
            i2 = Inventory(
                inv_after.ore - blueprint.clay,
                inv_after.clay,
                inv_after.obsidian,
                inv_after.geode,
            )
            push!(results, work(blueprint, i2, r2, n+1))
        end
        if can_ore
            r2 = Robots(robots.ore + 1, robots.clay, robots.obsidian, robots.geode)
            i2 = Inventory(
                inv_after.ore - blueprint.ore,
                inv_after.clay,
                inv_after.obsidian,
                inv_after.geode,
            )
            push!(results, work(blueprint, i2, r2, n+1))
        end
        if remaining_time > 0
            push!(results, work(blueprint, inv_after, robots, n+1))
        end
    end

    best = maximum(results)
    WORK_CACHE[key] = best
    if best > BEST[]
        BEST[] = best
    end
    return best
end



function part1(blueprints)
    results = Dict{Int,Int}()
    start_inventory = Inventory(0, 0, 0, 0)
    start_robots = Robots(1, 0, 0, 0)
    T[] = 24
    for (n, blueprint) in blueprints
        BEST[] = 0
        empty!(WORK_CACHE)
        value = work(blueprint, start_inventory, start_robots, 1)
        results[n] = n * value
    end

    ans = sum([r for (_, r) in results])
    empty!(WORK_CACHE)
    return ans
end


function part2(blueprints)
    results = Dict{Int,Int}()
    start_inventory = Inventory(0, 0, 0, 0)
    start_robots = Robots(1, 0, 0, 0)
    T[] = 32

    for n = 1:min(3, length(blueprints))
        blueprint = blueprints[n]
        BEST[] = 0
        empty!(WORK_CACHE)
        value = work(blueprint, start_inventory, start_robots, 1)
        results[n] = value
    end

    ans = prod([r for (_, r) in results])
    empty!(WORK_CACHE)
    return ans
end


##
##
## With 2 optimisations it started working
## I came up with 2 more, and it was cut down to 2.5s and 6.5s on my system

data = parse_data(input)
t0 = time()
println("Part1: ", part1(data))
println("Elapsed: ", round(time() - t0; digits = 2), " seconds")

t0 = time()
println("Part2: ", part2(data))
println("Elapsed: ", round(time() - t0; digits = 2), " seconds")
