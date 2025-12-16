from banks import get_total_joltage


def main():
    with open('batteries.txt', 'r') as file:
        banks = (file.read()).split()
        total_joltage = get_total_joltage(banks)
        print(total_joltage)


if __name__ == '__main__':
    main()