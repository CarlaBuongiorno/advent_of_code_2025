from invalid_ids import get_invalid_ids


def main():
    with open('id_ranges.txt', 'r') as file:
        product_id_ranges = (file.read()).strip()
        id_ranges = product_id_ranges.split(',')
        invalid_ids = get_invalid_ids(id_ranges)
        print(invalid_ids)
    

if __name__ == '__main__':
    main()