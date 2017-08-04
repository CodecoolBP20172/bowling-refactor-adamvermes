def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for line in range(len(game)):
        if game[line] == '/':
            result += 10 - last
        else:
            result += get_value(game[line])
        # if not in_first_half:
            # frame += 1
        if frame < 10  and get_value(game[line]) == 10:
            if game[line] == '/':
                result += get_value(game[line+1])
            elif game[line] == 'X' or game[line] == 'x':
                result += get_value(game[line+1])
                if game[line+2] == '/':
                    result += 10 - get_value(game[line+1])
                else:
                    result += get_value(game[line+2])
        last = get_value(game[line])
        if not in_first_half:
            frame += 1
        if in_first_half == True:
            in_first_half = False
        else:
            in_first_half = True
        if game[line] == 'X' or game[line] == 'x':
            in_first_half = True
            frame += 1
    return result

def get_value(char):
    if char == '1' or char == '2' or char == '3' or \
       char == '4' or char == '5' or char == '6' or \
       char == '7' or char == '8' or char == '9':
        return int(char)
    elif char == 'X' or char == 'x':
        return 10
    elif char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
