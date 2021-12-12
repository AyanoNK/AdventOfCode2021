from data_import import get_question_data


response = get_question_data(year=2021, day=2)


parsed_data = response.splitlines()


parsed_data = [x.split() for x in parsed_data]
parsed_data = [[x[0], int(x[1])] for x in parsed_data]

# forward X increases the horizontal position by X units.
# down X increases the depth by X units.
# up X decreases the depth by X units.

horizontal = 0
depth = 0

for instruction in parsed_data:
    if instruction[0] == 'up':
        depth -= instruction[1]
    if instruction[0] == 'down':
        depth += instruction[1]
    if instruction[0] == 'forward':
        horizontal += instruction[1]


print('pt1', horizontal * depth)


horizontal = 0
depth = 0
aim = 0
for instruction in parsed_data:
    if instruction[0] == 'up':
        aim -= instruction[1]
    if instruction[0] == 'down':
        aim += instruction[1]
    if instruction[0] == 'forward':
        horizontal += instruction[1]
        depth += aim * instruction[1]

print('pt2', horizontal * depth)
