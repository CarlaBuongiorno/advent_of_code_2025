# def get_total_joltage(banks):
#     results = []
#     for bank in banks:
#         sorted_bank = sorted(bank)
#         highest = bank.index(sorted_bank[-1])
#         if highest+1 < len(bank):
#             sliced_bank = bank[highest+1:]
#             sorted_sliced_bank = sorted(sliced_bank)
#             second_highest = sliced_bank.index(sorted_sliced_bank[-1])
#             results.append(f'{bank[highest]}{sliced_bank[second_highest]}')
#         else:
#             second_highest = bank.index(sorted_bank[-2])
#             if highest < second_highest:
#                 results.append(f'{bank[highest]}{bank[second_highest]}')
#             else:
#                 results.append(f'{bank[second_highest]}{bank[highest]}')
#     return sum([int(number) for number in results])


# -------------- part 2 -------------- #


# def get_total_joltage(banks):
#     results = []
#     index_of_previous_digit = 0
#     for bank in banks:
#         for n in range(1,13):
#             nth_digit, index_of_previous_digit = find_nth_digit(bank, n, index_of_previous_digit)
#             results.append(nth_digit)

        
# def find_nth_digit(bank, n, index_of_previous_digit):
#     current_range = bank[index_of_previous_digit:-(12-n)]
#     highest_number = max(current_range)
#     index_in_current_range = current_range.index(highest_number)
#     index_in_bank = index_in_current_range+index_of_previous_digit
#     return highest_number, index_in_bank



def get_total_joltage(banks):
    jolts = 0
    for bank in banks:
        results = []
        index_of_previous_digit = 0
        for n in range(1, 13):
            nth_digit, index_of_previous_digit = find_nth_digit(bank, n, index_of_previous_digit)
            results.append(str(nth_digit))
        jolts += int(''.join(results))
    return jolts


def find_nth_digit(bank, n, index_of_previous_digit):
    current_range = bank[index_of_previous_digit:len(bank)-(12-n)]
    current_range_ints = [int(i) for i in current_range]
    max_in_current_range = max(current_range_ints)
    index_in_current_range = current_range.index(str(max_in_current_range))
    index_in_bank = index_in_current_range+index_of_previous_digit
    return max_in_current_range, index_in_bank+1

