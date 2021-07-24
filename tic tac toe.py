# write your code her
counter = 0
user = '         '
all_coordinate = ['11', '12', '13', '21', '22', '23', '31', '32', '33']


def showcase():
    print("---------")
    print("| " + user[0] + " " + user[1] + " " + user[2] + " |")
    print("| " + user[3] + " " + user[4] + " " + user[5] + " |")
    print("| " + user[6] + " " + user[7] + " " + user[8] + " |")
    print("---------")


def coordinate():
    """Look if the input coordinate is valid. No words or number beyond 1 to 3. Enter 2 numbers within from 1 to 3"""
    global num
    global user
    if num.isalpha():
        print("You should enter numbers!")
        num = input("Enter the coordinates: ").replace(" ", "")
        return coordinate()
    elif num not in all_coordinate:
        print("Coordinates should be from 1 to 3!")
        num = input("Enter the coordinates: ").replace(" ", "")
        return coordinate()
    elif user[all_coordinate.index(num)] != " ":
        print("This cell is occupied! Choose another one!")
        num = input("Enter the coordinates: ").replace(" ", "")
        return coordinate()
    elif counter in range(0, 9, 2):
        location = all_coordinate.index(num)
        user = user[:location] + user[location].replace(" ", "X") + user[location + 1:]
    elif counter in range(1, 9, 2):
        location = all_coordinate.index(num)
        user = user[:location] + user[location].replace(" ", "O") + user[location + 1:]


def result_scan():
    global counter
    amount_x1 = 0
    amount_o1 = 0
    amount_x2 = 0
    amount_o2 = 0
    amount_x3 = 0
    amount_o3 = 0
    amount_ = 1
    for x in range(2, 7, 2):
        if user[x] == "X":
            amount_x1 += 1
        if user[x] == "O":
            amount_o1 += 1
    for x in range(0, 9, 4):
        if user[x] == "X":
            amount_x2 += 1
        if user[x] == "O":
            amount_o2 += 1
    if amount_x1 == 3 or amount_x2 == 3:
        print("X wins")
        counter += 9
    elif amount_o1 == 3 or amount_o2 == 3:
        print("O wins")
        counter += 9
    elif user[0:3] == "XXX" or user[3:6] == "XXX" or user[6:9] == "XXX":
        print("X wins")
        counter += 9
        counter += 9
    elif "_" in user:
        for x in user:
            if x == "X":
                amount_x3 += 1
            if x == "O":
                amount_o3 += 1
            if x == "_":
                amount_ += 1
        if amount_x3 != amount_o3:
            print("Impossible")
            counter += 9
        if amount_x3 == amount_o3 == amount_:
            print("Game not finished")
            counter += 9
    elif user[0:3] == "OOO" or user[3:6] == "OOO" or user[6:9] == "OOO":
        print("O wins")
        counter += 9
    elif user[0] == user[3] == user[6] == "X" or user[1] == user[4] == user[7] == "X" or user[2] == user[5] == user[8] == "X":
        print("X wins")
        counter += 9
    elif user[0] == user[3] == user[6] == "O" or user[1] == user[4] == user[7] == "O" or user[2] == user[5] == user[8] == "O":
        print("O wins")
        counter += 9
    elif ' ' not in user:
        counter += 9
        print("Draw")
    else:
        return


showcase()
while counter <= 9:
    num = input("Enter the coordinates: ").replace(" ", "")
    coordinate()
    showcase()
    result_scan()
    counter += 1
