
row = 9
column = 9
user_input = []
print("*****_ENTER 0 IF THE BLOCK IS BLANK_*****")
print()
print("Enter the numbers in row order: ")

for r in range(row):
    problem = []
    #loop 1 row at a time for a total of 9 times
    for c in range(column):
        #add a total of 9 user inputs in the chosen row above
        problem.append(int(input()))
    #continue back to the row loop
    user_input.append(problem)
    #add input values in a new array


def final_sudoku(user_input):
    if not isEmpty(user_input):
        return True
    else:
        row, column = isEmpty(user_input)

    for i in range(1, 10):
        if isValid(user_input, i, (row, column)):
            user_input[row][column] = i

            if final_sudoku(user_input):
                return True

            user_input[row][column] = 0

    return False


def input_sudoku(user_input):

    print()
    for i in range(row):
    #check if for each row's position, divisible by 3
        if i % 3 == 0 and i != 0:
            print("--------------------")

        for j in range(column): 
        #check if for each column's position, divisible by 3
            if j % 3 == 0 and j != 0:
                print("|", end="")
            if j == 8:
                print(user_input[i][j])
            else:
                print(str(user_input[i][j]) + " ", end = "")

#we are checking by rows
#by columns and
#by each 3 x 3 block (a total of 9 3x3 blocks)
def isValid(user_input, num, position):

    #by each row
    for i in range(9):
        #row 0 of column i, i will increase
        #horizontally
        if user_input[position[0]][i] == num and position[1] != i:
            return False

    #by each column
    for j in range(9):
        #column 0 of row j, j will increase
        #vertically
        if user_input[j][position[1]] == num and position[0] != j:
            return False

    #by each 3x3 block
    block_x  = position[1] // 3
    block_y  = position[0] // 3

    for i in range(block_y * 3, block_y * 3 + 3):
        for j in range(block_x * 3, block_x * 3 + 3):
            if user_input[i][j] == num and (i, j) != position:
                return False
    return True

def isEmpty(user_input):
    for i in range (9):
        for j in range (9):
            if user_input[i][j] == 0:
                return (i, j)
    return None

print()
print("***Unsolved 9 x 9 Sudoku***")
input_sudoku(user_input)
final_sudoku(user_input)
print()
print("***Solved 9 x 9 Sudoku***")
input_sudoku(user_input)

