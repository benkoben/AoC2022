import requests

# This assignment is about learning recursion

def get_input(url) -> str:
    cookie = {'session': '53616c7465645f5fea2ff079c5cce5f9d6beab4cfe8276f39679cfb53bed2a1c93984ae48d06da1cea71e088be16d924f8d69f1e5a17c6a4284ac4fbd1ab9858'}
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0'}
    response =  requests.get(url, cookies=cookie, headers=headers)

    if  response.status_code == 400:
        print("Bad requests, have you checked session cookie and use agent header?")
    elif response.status_code == 200:
        return response.text

def dir_tree(fs) -> dict:
    level = list([])
    directory = {}
    abs_path = lambda x: '/'.join(x) 

    for cmd in fs:
        if cmd.startswith("$ cd"):
            if not cmd.endswith('..'):
                dir_name = cmd[5:]
                level.append(dir_name)
                if not abs_path(level) in directory:
                    directory[abs_path(level)] = []
            else:
                level.pop()

        elif cmd.split(' ')[0].isdigit():
            file_size, file_name = cmd.split(' ')
            directory[abs_path(level)].append(int(file_size))

        elif cmd.split(' ')[0].startswith('dir'):
            dir_name = cmd.split(' ')[1]
            child = level + [dir_name]
            directory[abs_path(level)].append(abs_path(child))

    return directory

def dir_size(dir_path: str, directory: dict) -> int:
    total = 0
    for x in directory[dir_path]:
        if isinstance(x, str):
            total += dir_size(x, directory)
        if isinstance(x, int):
            total += x

    return total

def main(url):
    commands  = get_input(url).splitlines()
    tree = dir_tree(commands)

    part1 = 0
    part2 = 70000000

    used_space = [dir_size(y, tree) for y in [x for x in tree.keys()]][0]
    unused_space = 70000000 - used_space

    for f in tree.keys():
        current_dir_size = dir_size(f, tree)
        if current_dir_size <= 100000:
            part1 += current_dir_size

        if unused_space + current_dir_size >= 30000000:
            # take the smallest possible value
            if current_dir_size < part2:
                part2 = current_dir_size


    print(part1)
    print(part2)


if __name__ == "__main__":
    url = "https://adventofcode.com/2022/day/7/input"
    main(url)
