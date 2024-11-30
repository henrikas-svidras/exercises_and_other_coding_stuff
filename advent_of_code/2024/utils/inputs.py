import os 

file_path = os.path.abspath(__file__)
inputs_dir = os.path.dirname(os.path.dirname(file_path)) + "/inputs"

def is_data_present(path):
    return os.path.exists(path)

def get_data_set(year, day):
    path = inputs_dir+f"/{day}_task.txt"
    if is_data_present(path):
        print("Downloaded already. Loading...")
        with open(path) as f:
            lines = [line.replace("\n","") for line in f]
        return lines
    else:        
        import urllib.request

        session_cookie = os.getenv("SESSION_COOKIE")

        url = f'https://adventofcode.com/{year}/day/{day}/input'
        print(f"Downloading from {url}...")
        a_request = urllib.request.Request(url)
        a_request.add_header("Cookie", f"session={session_cookie}")
        page = urllib.request.urlopen(a_request).read()
        with open(path, "wb") as f:
            f.write(page)
        return get_data_set(year, day)

def get_test_data_set(year, day):
    path = inputs_dir+f"/{day}_task_test.txt"
    if is_data_present(path):
        print("Downloaded already. Loading test data...")
        with open(path) as f:
            lines = [line.replace("\n","") for line in f]
        return lines
    else:        
        import urllib.request
        import re
        url = f'https://adventofcode.com/{year}/day/{day}'
        print(f"Downloading testa data from {url}...")
        a_request = urllib.request.Request(url)
        page = urllib.request.urlopen(a_request).read()
        result = page.split(b"For example:")[1]
        result = re.search(rb"<pre><code>(.*?)</code></pre>", result, re.DOTALL).group(1)
        with open(path, "wb") as f:
            f.write(result)
        return get_test_data_set(year, day)