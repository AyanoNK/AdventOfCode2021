from data_import import get_question_data

response = get_question_data(year=2021, day=3)

parsed_data = response.splitlines()

splitted = []
for binary in parsed_data:
    splitted.append([n for n in binary])

transposed = []
trans = ''


x = [item[0] for item in splitted]
y = list(list(zip(splitted)))
print(parsed_data[:1])
print(y[:1])
