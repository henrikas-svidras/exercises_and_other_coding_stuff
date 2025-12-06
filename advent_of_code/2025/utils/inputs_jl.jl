module Utils

export get_test_data, get_data

using HTTP
using Gumbo



function get_test_data(year::Int, day::Int; raw::Bool=false)

    println("Getting test data for $year and $day")

    path = get_input_paths(day, test=true)

    if isfile(path)
        println("File already exists at $path")
    else

        session_cookie = ENV["SESSION_COOKIE"]

        headers = [
            "Cookie" => "session=$(session_cookie)"
        ]


        url = "https://adventofcode.com/$year/day/$day"
        r = HTTP.request("GET", url, headers=headers)
        r_body = String(r.body)

        parts = split(r_body, "For example")
        if length(parts)==1
            parts = split(r_body, "larger example")
        end
        result_part = parts[2]

        m = match(r"<pre><code>(.*?)</code></pre>"s, result_part)

        if m !== nothing
            result = m.captures[1]
        else
            error("No match found")
        end

        decoded = Gumbo.parsehtml(result).root[2][1].text

        open(path, "w") do f
            write(f, decoded)
        end
    end

    return fetch_data(year, day; test=true, raw=raw)

end

function get_data(year::Int, day::Int; raw::Bool=false)

    println("Getting data for $year and $day")

    path = get_input_paths(day, test=false)

    if isfile(path)
        println("File already exists at $path")
    else
        session_cookie = ENV["SESSION_COOKIE"]
        url = "https://adventofcode.com/$year/day/$day/input"
        
        headers = [
            "Cookie" => "session=$(session_cookie)"
        ]
        r = HTTP.request("GET", url, headers=headers)
        decoded = String(r.body)
        
        open(path, "w") do f
            write(f, decoded)
        end
    end

    return fetch_data(year, day; test=false, raw=raw)
        
end

function fetch_data(year::Int, day::Int; test::Bool=true, raw::Bool=false)

    path = get_input_paths(day, test=test)

    if !raw
        lines = [String(chomp(line)) for line in eachline(path)]
        return lines
    else
        content = read(path, String)
        return content
    end

end

function get_input_paths(day::Int; test::Bool=false)
    inputs_dir = "inputs"
    filename = test ? "$(day)_task_test.txt" : "$(day)_task.txt"
    return joinpath(inputs_dir, filename)
end

end