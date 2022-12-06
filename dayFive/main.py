from pprint import pprint
from collections import defaultdict
import requests

def get_input(url) -> str:
    cookie = {'session': '53616c7465645f5fea2ff079c5cce5f9d6beab4cfe8276f39679cfb53bed2a1c93984ae48d06da1cea71e088be16d924f8d69f1e5a17c6a4284ac4fbd1ab9858'}
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0'}
    response =  requests.get(url, cookies=cookie, headers=headers)

    if  response.status_code == 400:
        print("Bad requests, have you checked session cookie and use agent header?")
    elif response.status_code == 200:
        return response.text

def create_inventory(start_layout, no_stacks) -> defaultdict:
    """
        This function parses the initial layout of crate stacks
    """
    stack_indexes = lambda x : [i for i, id_ in dict(enumerate(x)).items() if id_.isdigit()]
    new_stack     = lambda : list([])
    stack_indexes = stack_indexes(no_stacks)
    warehouse     = defaultdict(new_stack)

    for row in start_layout:
        for stack_number, index in dict(enumerate(stack_indexes)).items():
            if row[index].isalpha():
                warehouse[stack_number + 1].append(row[index])

    for k in warehouse.keys():
        warehouse[k].reverse()

    return warehouse

def main(url):
    data  = get_input(url).splitlines()
    inventory_part1 = create_inventory(data[0:8], data[8])
    inventory_part2 = create_inventory(data[0:8], data[8])
    instructions = data[10:]

    for step in instructions:
        crates_amount = int(step.split(' ')[1])
        start =  int(step.split(' ')[3])
        stop =  int(step.split(' ')[5])
        for i in list(range(0, crates_amount)):
            inventory_part1[stop].append(inventory_part1[start].pop())

        chunk_size = len(inventory_part2[start]) - crates_amount
        big_pop = inventory_part2[start][chunk_size:]
        del inventory_part2[start][chunk_size:]
        inventory_part2[stop] +=  big_pop

    print("Using crate mover 9000")
    pprint(''.join([v[-1] for k, v in inventory_part1.items()]))
    print("Using crate mover 9001")
    pprint(''.join([v[-1] for k, v in inventory_part2.items()]))

if __name__ == "__main__":
    url = "https://adventofcode.com/2022/day/5/input"
    main(url)
