from data_import import get_question_data

response = get_question_data(year=2021, day=3)

parsed_data = response.splitlines()

print(parsed_data)
