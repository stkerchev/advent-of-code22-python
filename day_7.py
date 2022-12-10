import input


#  https://adventofcode.com/2022/day/7
def resolve_no_space_left_on_device():
    input_data = input.parse_day(7)
    print(f'day 7 - part 1 ==> {total_size(input_data, False)}')  # 1306611
    print(f'day 7 - part 2 ==> {total_size(input_data, True)}')  # 13210366


def total_size(input_data, remove):
    # "/-abc": ["d", "p"]
    d = {"/": set()}
    # "/-abc": [121212, 2122]
    f = {"/": set()}

    current_dir = "/"
    for line in input_data:
        if line.startswith("$"):
            if line == "$ ls":
                pass
            elif line == "$ cd /":
                current_dir = "/"
            elif line == "$ cd ..":
                index = current_dir.rindex("-")
                current_dir = current_dir[:index]
            else:  # "$ cd xyz"
                new_dir_name = current_dir + "-" + line.split(" ")[-1]
                current_dir = new_dir_name
                if new_dir_name not in d:
                    d[current_dir] = set()
        else:
            if line.startswith("dir"):
                new_dir_name = line.split(" ")[-1]
                set_of_nested = d.get(current_dir)
                set_of_nested.add(current_dir + "-" + new_dir_name)
            else:
                if current_dir in f:
                    file_set = f.get(current_dir)
                    file_set.add(line)
                else:
                    current_file = [line]
                    f[current_dir] = set(current_file)

    for key in f.keys():
        size_sum = 0
        set_of_files = f.get(key)
        for file in set_of_files:
            size = int(file.split(" ")[0])
            size_sum += size
        f[key] = size_sum

    dynamic_sum = {}
    result = 0
    for key in d.keys():
        dir_sum = calculate_sum(key, d, f, dynamic_sum)
        if dir_sum < 100000:
            result += dir_sum

    if not remove:
        return result

    space_all = 70000000
    space_need = 30000000
    space_used = dynamic_sum.get("/")
    available = space_all - space_used
    target = space_need - available
    best = space_all
    for dir_name in dynamic_sum.keys():
        current_dir_size = dynamic_sum.get(dir_name)
        if current_dir_size >= target:
            if current_dir_size <= best:
                best = current_dir_size
    return best


def calculate_sum(dir_name, d, f, dynamic_sum):
    if len(d.get(dir_name)) == 0:
        dynamic_sum[dir_name] = f.get(dir_name)
        return dynamic_sum.get(dir_name)
    else:
        result = 0
        if dir_name in f:
            result = f.get(dir_name)
        nested = d.get(dir_name)
        for nested_dir in nested:
            if nested_dir in dynamic_sum:
                result += dynamic_sum.get(nested_dir)
            else:
                dynamic_sum[nested_dir] = calculate_sum(nested_dir, d, f, dynamic_sum)
                result += dynamic_sum.get(nested_dir)
        dynamic_sum[dir_name] = result
        return result
