import requests

def get_input(url) -> str:
    cookie = {'session': '53616c7465645f5fd45683b271fe5e2dd9aafe8fdc22a9279fa52f78cb36f73abc3b66163f9b4d3fba09430c32511f99efe2f5338ce9b6fb8beffdd271292ff6'}
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0'}
    response =  requests.get(url, cookies=cookie, headers=headers)

    if  response.status_code == 400:
        return "Bad requests, have you checked session cookie and use agent header?"
    return response.text


def main():
    url = "https://adventofcode.com/2022/day/2/input"
    strat_guide = get_input(url)
    # part 1 data
    rules = dict({
        'A': 1,
        'B': 2,
        'C': 3,
        'X': 1,
        'Y': 2,
        'Z': 3,
    })

    outcomes = dict({
        'loss': 0,
        'draw': 3,
        'win': 6,
    })

    win_combos = [
        ['A', 'Y'],
        ['B', 'Z'],
        ['C', 'X'],
    ]

    loss_combos = [
        ['A', 'Z'],
        ['B', 'X'],
        ['C', 'Y'],
    ]

    # part 2 data
    predictions = dict({
        'X': {
            'A': 'C',
            'B': 'A',
            'C': 'B',
            'value': outcomes['loss']
        },
        'Y': {
            'A': 'A',
            'B': 'B',
            'C': 'C',
            'value': outcomes['draw']
        },
        'Z': {
            'A': 'B',
            'B': 'C',
            'C': 'A',
            'value': outcomes['win']
        },
    })

    score_part1 = 0
    score_part2 = 0
    for turn in strat_guide.split('\n')[0:-1]: # skip last line 
        opponent, me = turn.split(' ')

        if rules[opponent] == rules[me]:
            score_part1+= outcomes['draw'] + rules[me]
        elif [opponent, me] in win_combos:
            score_part1+= outcomes['win'] + rules[me]
        elif [opponent, me] in loss_combos:
            score_part1 += outcomes['loss'] + rules[me]

        score_part2 += int(rules[predictions[me][opponent]]) + int(predictions[me]['value'])

    # Part 1
    print(score_part1)
    # Part 2
    print(score_part2)


if __name__ == "__main__":
    main()
