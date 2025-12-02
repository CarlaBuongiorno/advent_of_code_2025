def get_password(rotation): # ['R50']
    dial = 50
    for r in rotation: # 'R50'
        direction = r[0] # 'R'
        rotate = int(r[1:]) # 50
        if direction == 'L': # False
            dial = dial - rotate # dial = 50 - 50
        else:
            dial = dial + rotate # dial = 50 + 50
        if dial == 0: # False
            return 1
        elif dial == 100: # True (100)
            return 1
        else:
            return 0