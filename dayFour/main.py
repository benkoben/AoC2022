import requests

def get_input(url) -> str:
    cookie = {'session': '53616c7465645f5fea2ff079c5cce5f9d6beab4cfe8276f39679cfb53bed2a1c93984ae48d06da1cea71e088be16d924f8d69f1e5a17c6a4284ac4fbd1ab9858'}
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0'}
    response =  requests.get(url, cookies=cookie, headers=headers)

    if  response.status_code == 400:
        print("Bad requests, have you checked session cookie and use agent header?")
    elif response.status_code == 200:
        return response.text


def main(url):
    assignments  = get_input(url).splitlines()
    get_range = lambda x, y: list(range(int(x), int(y) + 1 ))

    part1_count = 0
    part2_count = 0

    for assignment in assignments:
        elf1, elf2 = assignment.split(',')
        elf1_range = get_range(*elf1.split('-'))
        elf2_range = get_range(*elf2.split('-'))
        l1, r1 = elf1_range[0], elf1_range[-1]
        l2, r2 = elf2_range[0], elf2_range[-1]

        if set(elf1_range).issubset(set(elf2_range)) or set(elf2_range).issubset(set(elf1_range)):
            part1_count  += 1

        if max(l1, l2) <= min(r1,r2):
            part2_count += 1

    print(part1_count)
    print(part2_count)

if __name__ == "__main__":
    url = "https://adventofcode.com/2022/day/4/input"
    main(url)
