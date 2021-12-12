from data_import import get_question_data

response = get_question_data(year=2021, day=1)

parsed_data = response.splitlines()

parsed_data = [int(x) for x in parsed_data]


bigger_previous = []
ankle = None
for data in parsed_data:
    if ankle and data > ankle:
        bigger_previous.append(ankle)
    ankle = data

print('pt1', len(bigger_previous))

bigger_previous = []
for ranges in range(0, len(parsed_data)):
    try:
        calc = parsed_data[ranges] + \
            parsed_data[ranges + 1] + parsed_data[ranges + 2]
        if ankle and calc > ankle:
            bigger_previous.append(ankle)
    except IndexError:
        break
    ankle = calc

print('pt2', len(bigger_previous))
