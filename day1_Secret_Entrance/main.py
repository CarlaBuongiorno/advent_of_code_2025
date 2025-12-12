from password import get_password


def main():
    with open('rotations.txt', 'r') as file:
        rotations = file.read()
        rotations = rotations.split()
    
    password = get_password(rotations)
    print(password)


if __name__ == '__main__':
    main()