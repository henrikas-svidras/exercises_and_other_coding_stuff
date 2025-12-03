include("utils/inputs_jl.jl")

using JuliaFormatter
format(@__FILE__)

input = [
    "2718578396614-2917433960864,2590597945418-2718161909381,6797874938136-6837903382281,1634606170089-1652610008257,7245231484720-7322365008663,693064002765-715981456831,5491430860445-5559688285867,5821438059403-5929371927214,7024696853238-7216774763178,6448914248445-6647857914491,4667054279620-4724701059936,2076122434864-2186371315777,5022698735105-5192998826691,166338025374-282274374423,4961673689218-5010218182744,6701312394331-6786448090779,4444332376942-4452910891957,806182354410-813443611733,1939955274151-2061030611124,6338879277920-6448155530241,283712673821-482115520322,5939454750467-5966152893896,3886019227317-4037891591496,6122186923834-6272744056239,17820519715-127447035232,1267491984933-1284573692463,1694245771202-1754339701199,2953244255384-3101488404389,1344933891335-1345980288418,6841078701410-7022688611683,5270899973679-5382441043211,1007093930359-1202243765380,3107479726235-3262365314835,3474420239839-3670025013821,3686188705103-3840182903911,4053380811858-4130719151228,3294697720522-3320859516491,5607422361446-5754261926073,2446121172056-2529524977541,4134365555445-4326553654484,1882126952441-1914436629511,4763811494877-4919110669996,2238608850909-2380649742730,499296606494-583727380590,881058839320-1005249953946,6031453139726-6119495446878,4486265706230-4608294258522,7370568555626-7479108933145,3333222819043-3471650119437,1399390987972-1530203653876",
]

function parse_data(input)
    joined = join(input, "")
    sequences = split(joined, ",")
    ranges = []
    for sq in sequences
        a_str, b_str = split(sq, "-")
        push!(ranges, (parse(Int, a_str), parse(Int, b_str)))
    end
    return ranges
end

function is_invalid_id(n::Integer)
    s = string(n)
    L = length(s)

    for len = 1:(L÷2)
        L % len == 0 || continue
        sub = s[1:len]
        if sub ^ (L ÷ len) == s
            return true
        end
    end

    return false
end

function part12(ranges)
    seen = Set{Int}()

    low = minimum(first.(ranges))
    right = maximum(last.(ranges))

    min_n = ndigits(low)
    max_n = ndigits(right)
    println(min_n, max_n)

    for n = min_n:max_n
        for m = 1:(div(n, 2))
            mod(n, m) == 0 || continue
            #part1
            div(n, m) == 2 || continue
            #part 2
            #div(n, m) >= 2 || continue

            rep_multiplier = div((10^n - 1), (10^m - 1))

            for (L, R) in ranges
                x_low = cld(L, rep_multiplier)
                x_high = fld(R, rep_multiplier)

                x_low > x_high && continue

                for x = x_low:x_high
                    N = x * rep_multiplier
                    is_invalid_id(N) && push!(seen, N)
                end
            end
        end
    end

    return sum(seen)
end


data = parse_data(input)
t0 = time()
println("Part12: ", part12(data))
println("Elapsed: ", round(time() - t0; digits = 2), " seconds")
