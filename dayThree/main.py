import requests
import string

from collections import defaultdict
from pprint import pprint

def get_input(url) -> str:
    cookie = {'session': '53616c7465645f5fd45683b271fe5e2dd9aafe8fdc22a9279fa52f78cb36f73abc3b66163f9b4d3fba09430c32511f99efe2f5338ce9b6fb8beffdd271292ff6'}
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0'}
    response =  requests.get(url, cookies=cookie, headers=headers)

    if  response.status_code == 400:
        print("Bad requests, have you checked session cookie and use agent header?")
    elif response.status_code == 200:
        return response.text


def main(url):
    # Spara alla värden för varje bokstav
    lower_and_upper = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    value_letter = dict(enumerate(lower_and_upper, start=1))
    letter_value = { v: k for k,v in value_letter.items() }
    rucksacks  = get_input(url).splitlines()
    print(type(rucksacks))
    prio_part_1 = 0
    prio_part_2 = 0
    for rucksack in rucksacks:
        common_item_types = []
        compartment_one, compartment_two = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        for c1_item in compartment_one:
            for c2_item in compartment_two:
                if c1_item == c2_item:
                    common_item_types.append(c1_item)

        for item in set(common_item_types):
            prio_part_1 += letter_value[item]

    groups = list([])
    chunk_size = 3
    start = 0
    for stop in range(start, len(rucksacks), chunk_size):
        group = rucksacks[start:stop+chunk_size]
        start += chunk_size
        groups.append([set(x) for x in group])
   
    for group in groups:
        item_counter = defaultdict(lambda: 0)
        for r1_item in group[0]:
            item_counter[r1_item] += 1
        for r2_item in group[1]:
            item_counter[r2_item] += 1
        for r3_item in group[2]:
            item_counter[r3_item] += 1

        badge = {v: k for k, v in item_counter.items()}[3]
        prio_part_2 += letter_value[badge]

    # part 1
    print(prio_part_1)
    # part 2
    print(prio_part_2)

if __name__ == "__main__":
    url = "https://adventofcode.com/2022/day/3/input"
    main(url)
