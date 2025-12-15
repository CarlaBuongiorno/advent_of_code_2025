def get_password(sequence_of_rotations):
    rotations = [int(r[1:]) if r[0] == 'R' else -(int(r[1:])) for r in sequence_of_rotations]
    dial = [i for i in range(100)]
    rotation_list = []
    result = []
    start = 50
    for number_to_add in rotations:
        while True:
            rotation_list.append(dial[start])
            if len(rotation_list) == (abs(number_to_add) + 1):
                start = rotation_list[-1]
                result.extend(rotation_list[1:])
                rotation_list.clear()
                break
            if number_to_add > 0:
                start = (start + 1) % len(dial)
            else:
                start = (start - 1) % len(dial)
    return len([zero for zero in result if zero == 0])
