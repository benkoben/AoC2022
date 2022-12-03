import requests
import json
from pprint import pprint

def get_input(url) -> str:
    cookie = {'session': '53616c7465645f5fd45683b271fe5e2dd9aafe8fdc22a9279fa52f78cb36f73abc3b66163f9b4d3fba09430c32511f99efe2f5338ce9b6fb8beffdd271292ff6'}
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0'}
    response =  requests.get(url, cookies=cookie, headers=headers)

    if  response.status_code == 400:
        print("Bad requests, have you checked session cookie and use agent header?")
    elif response.status_code == 200:
        return response.text

url = "https://adventofcode.com/2022/day/1/input"

def main():
    caloriesLog  = get_input(url)
    elves = dict()
    elv_count = 0
    calory_summary = 0

    fattest_elv = 0
    for item in caloriesLog.split('\n'):
        if item.isdigit():
            calory_summary += int(item) 
        else:
            if calory_summary > fattest_elv:
                fattest_elv = calory_summary
            elves[elv_count] = calory_summary
            calory_summary = 0
            elv_count += 1
    # part 1
    print(fattest_elv)
    # part 2
    print(sum(sorted(elves.values(), reverse=True)[0:3]))

if __name__ == "__main__":
    main()
