import requests


cookies = {
    'session': '53616c7465645f5f199dc392a3e7c6f5b3988259e6f458710d127077b7fe7f71d615259591b9c76bb1c43f28a3db37ef'
}


def get_question_data(year, day):
    url = 'http://adventofcode.com/{year}/day/{day}/input'.format(
        year=year, day=day)

    request = requests.get(url, cookies=cookies, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'})

    response = request.text
    return response
