import random
# Creating lists
charachters = ["A", "A", "B", "B", "C", "C", "D", "D", "E",
               "E", "F", "F", "G", "G", "H", "H", "I", "I", "X", "X"]
check_list = ["", "", "", "", "", "", "", "", "",
              "", "", "", "", "", "", "", "", "", "", ""]
out_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
random.shuffle(charachters)  # To shuffle charachters randomly


def ply1(num1, num2):  # function to remove the choice of player 1 and put star instead to not be choosed one more time
    if charachters[out_list.index(num1)] == charachters[out_list.index(num2)]:
        out_list.insert(out_list.index(num1), "*")
        out_list.pop(out_list.index(num1))
        out_list.insert(out_list.index(num2), "*")
        out_list.pop(out_list.index(num2))
        return out_list


def ply2(num1, num2):  # function to remove the choice of player 2 and put star instead to not be choosed one more time
    if charachters[out_list.index(num1)] == charachters[out_list.index(num2)]:
        out_list.insert(out_list.index(num1), "*")
        out_list.pop(out_list.index(num1))
        out_list.insert(out_list.index(num2), "*")
        out_list.pop(out_list.index(num2))
        return out_list


def is_valid_location(num1, num2):  # checking if number in list or not
    if num1 and num2 in out_list:
        return True


print(out_list)
# to check the game is well coded and do the right thing and will be removed when we want to play game and run it
print(charachters)
n = True  # To helf end the loop
ply_1_pts = 0  # points of player one to be checked at the end with player 2 to know winner
ply_2_pts = 0  # points of player two to be checked at the end with player 1 to know winner
while n == True:
    while out_list != check_list:  # condition of ending the game
        num1 = int(input("enter first num player 1: "))
        num2 = int(input("enter second num player 1: "))
        # if player entered an number that is not in list he will be asked to re enter the input again
        while not is_valid_location(num1, num2):
            print("invalid input")
            num1 = int(input("enter first number player 1: "))
            num2 = int(input("enter second number player 1: "))
        else:
            if charachters[out_list.index(num1)] == charachters[out_list.index(num2)]:
                ply_1_pts += 1  # if the two characters are the same the points of player 1 will increase
                print(f"player 1 points = {ply_1_pts}")
            else:
                # points will not increase if they aren't the same
                print(f"player 1 points = {ply_1_pts}")
            ply1(num1, num2)  # calling function
            print(out_list)
            # same condition as for player 1
        num1 = int(input("enter first num player 2: "))
        num2 = int(input("enter second num player 2: "))
        # if player entered an number that is not in list he will be asked to re enter the input again
        while not is_valid_location(num1, num2):
            print("invalid input")
            num1 = int(input("enter first number player 2: "))
            num2 = int(input("enter second number player 2: "))
        else:
            if charachters[out_list.index(num1)] == charachters[out_list.index(num2)]:
                ply_2_pts += 1
                print(f"player 2 points = {ply_2_pts}")
            else:
                print(f"player 2 points = {ply_2_pts}")
            ply1(num1, num2)
            print(out_list)
    else:
        if ply_1_pts > ply_2_pts:  # checking the winner
            print(
                f"player 1 won congratulations with {ply_1_pts} - {ply_2_pts}")
        else:
            print(
                f"player 2 won congratulations with {ply_1_pts} - {ply_2_pts}")
    n = False  # to exit the while true loop
else:
    print("<< Game Ended >>")  # Now it's the end of the game ")
