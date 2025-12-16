def get_total_joltage(banks):
    results = []
    for bank in banks:
        sorted_bank = sorted(bank)
        highest = bank.index(sorted_bank[-1])
        if highest+1 < len(bank):
            sliced_bank = bank[highest+1:]
            sorted_sliced_bank = sorted(sliced_bank)
            second_highest = sliced_bank.index(sorted_sliced_bank[-1])
            results.append(f'{bank[highest]}{sliced_bank[second_highest]}')
        else:
            second_highest = bank.index(sorted_bank[-2])
            if highest < second_highest:
                results.append(f'{bank[highest]}{bank[second_highest]}')
            else:
                results.append(f'{bank[second_highest]}{bank[highest]}')
    return sum([int(number) for number in results])
