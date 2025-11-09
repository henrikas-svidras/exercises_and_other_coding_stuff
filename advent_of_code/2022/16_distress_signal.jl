input = open("inputs/16_task.txt")

all_input = readlines(input)

function parse_input(all_input::Vector{String})
    pattern = r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.*)"

    connections = Dict{String, Vector{String}}()
    rates       = Dict{String, Int}()
    
    for line in all_input
        for m in eachmatch(pattern, line)
            from_valve = m.captures[1]              
            flow_rate  = parse(Int, m.captures[2])  

            to_valves  = split(strip(m.captures[3]), ", ")

            connections[from_valve] = to_valves      
            rates[from_valve]       = flow_rate     
        end
    end

    return connections, rates
end


function bfs_dists(connections::Dict{String, Vector{String}}, start::String)
    dist = Dict{String, Int}(start => 0) 
    q = [start]                           
    head = 1                            

    while head <= length(q)
        v = q[head]                     
        head += 1
        for w in connections[v]         
            if !haskey(dist, w)       
                dist[w] = dist[v] + 1
                push!(q, w)
            end
        end
    end

    return dist
end


function pick_nodes(rates::Dict{String, Int})
    useful = [v for (v, r) in rates if r > 0] 
    return vcat(["AA"], useful)               
end


index_nodes(nodes::Vector{String}) = Dict(v => i for (i, v) in enumerate(nodes))


function pairwise_dists(
    connections::Dict{String, Vector{String}},
    nodes::Vector{String},
    name_to_idx::Dict{String, Int},
)
    dists = Dict{Tuple{Int, Int}, Int}()
    for v in nodes
        dv = bfs_dists(connections, v)
        for w in nodes
            if haskey(dv, w)
                dists[(name_to_idx[v], name_to_idx[w])] = dv[w]
            end
        end
    end
    return dists
end

function build_open_index(nodes::Vector{String})
    openable = nodes[2:end]                                
    return Dict(v => (k - 1) for (k, v) in enumerate(openable))
end


allmask_from_N(N::Int) = N == 64 ? typemax(UInt64) : (UInt64(1) << UInt64(N)) - UInt64(1)


function best_single_agent(
    dists::Dict{Tuple{Int, Int}, Int},
    rates::Dict{String, Int},
    name_to_idx::Dict{String, Int},
    open_idx::Dict{String, Int};
    total_time::Int = 30,
    start::String = "AA",
)
    memo = Dict{Tuple{Int, Int, UInt64}, Int}()

    function dfs(cur::Int, time_left::Int, opened::UInt64)::Int
        key = (cur, time_left, opened)
        if (val = get(memo, key, nothing)) !== nothing
            return val
        end

        best = 0
        for (v, bit) in open_idx
            mask = UInt64(1) << bit
            (opened & mask) != 0 && continue   

            tgt = name_to_idx[v]              
            dist = get(dists, (cur, tgt), typemax(Int))  
            cost = dist + 1              
            if cost <= time_left

                gain = rates[v] * (time_left - cost)
                cand = gain + dfs(tgt, time_left - cost, opened | mask)
                if cand > best; best = cand; end
            end
        end

        memo[key] = best
        return best
    end

    return dfs(name_to_idx[start], total_time, UInt64(0))
end

# ----------------------------------------------------------------------------------
#  part 2
# ----------------------------------------------------------------------------------


function best_with_mask(
    dists::Dict{Tuple{Int, Int}, Int},
    rates::Dict{String, Int},
    name_to_idx::Dict{String, Int},
    open_idx::Dict{String, Int},
    allowed::UInt64;
    total_time::Int = 26,
    start::String = "AA",
)
    memo = Dict{Tuple{Int, Int, UInt64}, Int}()

    function dfs(cur::Int, time_left::Int, opened::UInt64)::Int
        key = (cur, time_left, opened)
        if (val = get(memo, key, nothing)) !== nothing
            return val
        end

        best = 0
        for (v, bit) in open_idx
            bitmask = UInt64(1) << bit
            if (allowed & bitmask) == 0 || (opened & bitmask) != 0
                continue
            end
            tgt  = name_to_idx[v]
            dist = get(dists, (cur, tgt), typemax(Int))
            cost = dist + 1
            if cost <= time_left
                gain = rates[v] * (time_left - cost)
                cand = gain + dfs(tgt, time_left - cost, opened | bitmask)
                if cand > best; best = cand; end
            end
        end

        memo[key] = best
        return best
    end

    return dfs(name_to_idx[start], total_time, UInt64(0))
end

function best_two_agents(
    dists::Dict{Tuple{Int, Int}, Int},
    rates::Dict{String, Int},
    name_to_idx::Dict{String, Int},
    open_idx::Dict{String, Int};
    total_time::Int = 26,
)
    N = length(open_idx)             
    allmask = allmask_from_N(N)       

    best_cache = Dict{UInt64, Int}()

    function cached_best(mask::UInt64)
        get!(best_cache, mask) do
            best_with_mask(dists, rates, name_to_idx, open_idx, mask; total_time=total_time)
        end
    end

    best_sum = 0
    for mask in UInt64(0):UInt64(allmask)
        comp = allmask ⊻ mask  
        mask <= comp || continue 

        me = cached_best(mask)
        el = cached_best(comp)

        s = me + el
        if s > best_sum
            best_sum = s
        end
    end

    return best_sum
end





function solve_all(all_input::Vector{String})
    connections, rates = parse_input(all_input)

    nodes        = pick_nodes(rates)
    name_to_idx  = index_nodes(nodes)

    dists        = pairwise_dists(connections, nodes, name_to_idx)

    open_idx     = build_open_index(nodes)

    part1 = best_single_agent(dists, rates, name_to_idx, open_idx; total_time=30, start="AA")

    part2 = best_two_agents(dists, rates, name_to_idx, open_idx; total_time=26)

    return part1, part2
end



part1, part2 = solve_all(all_input)
println("Part 1: ", part1)
println("Part 2: ", part2)  
