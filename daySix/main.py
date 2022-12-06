
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


def first_unique_sequence(window_size: int, data_stream: str) -> int:
    pos = 0
    for index in list(range(0, len(data_stream))):
        pos = index + window_size
        next_seq = data_stream[index:pos]
        if len(set(next_seq)) == window_size:
            break
    return pos


def main(url):
    data_stream  = get_input(url)
    print(first_unique_sequence(window_size=4, data_stream=data_stream))
    print(first_unique_sequence(window_size=14, data_stream=data_stream))


if __name__ == "__main__":
    url = "https://adventofcode.com/2022/day/6/input"
    main(url)
