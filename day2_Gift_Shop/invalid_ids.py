def get_invalid_ids(product_id_ranges):
    id_ranges = [get_id_ranges(id_range) for id_range in product_id_ranges]
    all_ids = [get_all_ids(id_range) for id_range in id_ranges]
    all_ids = [id for row in all_ids for id in row]
    invalid_ids = [int(id) for id in all_ids if check_for_invalid(id)]
    return sum(invalid_ids)


def get_id_ranges(id_ranges):
    return [int(id) for id in id_ranges.split('-')]


def get_all_ids(id_range):
    return [str(id) for id in range(id_range[0], id_range[1]+1)]


def check_for_invalid(id): # '565656'
    if len(id) % 2 == 0:
        part1 = id[:int(len(id)/2)]
        part2 = id[int(len(id)/2):]
        return part1 == part2
