path_taken = []
colour_taken = []

def is_valid(i, j, m, n):
    if i < 0 or i >= m:
        return False

    if j < 0 or j >= n:
        return False

    return True

def get_next_step(direction,i,j):
        if(direction=='N'):
            return i-1,j
        elif(direction=='E'):
            return i,j+1
        elif(direction=='S'):
            return i+1,j
        elif(direction=='W'):
            return i,j-1
        elif(direction=='NE'):
            return i-1,j+1
        elif(direction=='SE'):
            return i+1,j+1
        elif(direction=='SW'):
            return i+1,j-1
        else:
            return i-1,j-1

def traverse(input_mat, visited, i, j, current_colour, current_direction,
             m, n):

    global path_taken
    global colour_taken

    if input_mat[i][j] == 'O':
        return True

    found_path = False

    while True:

        i, j = get_next_step(current_direction, i, j)
        # print(current_colour, current_direction, is_valid(i, j, m, n))
        # print(current_colour, current_direction, i, j, is_valid(i, j, m, n))
        # path_taken.append(current_direction)


        if is_valid(i, j, m, n):
            # print(i, j)
            cell = (input_mat[i][j]).split('-')

            if cell == ['O']:
                return True

            new_colour, new_direction = cell[0], cell[1]
            # print(i, j)
            # print(cell)
            # print(new_colour, input_mat[i][j]visited[i][j])
            if new_colour != current_colour and not visited[i][j]:
                visited[i][j] = True
                path_taken.append(new_direction)
                colour_taken.append(new_colour)

                # print(i, j, new_colour, new_direction, '\n', path_taken)
                found_path = traverse(input_mat, visited, i, j, new_colour, new_direction,
                 m, n)

                if found_path:
                    return found_path
                else:
                    while (path_taken[-1] != current_direction or colour_taken[-1] != current_colour):
                        path_taken = path_taken[:-1]
                        colour_taken = colour_taken[:-1]

                    path_taken.append(current_direction)
                    colour_taken.append(current_colour)

            else:
                path_taken.append(current_direction)
                colour_taken.append(current_colour)
        else:
            # path_taken = path_taken[:-1]

            return False

    return found_path



def main():
    import sys

    INPUT_FILE_NAME = sys.argv[1]
    OUTPUT_FILE_NAME = sys.argv[2]

    input_mat = (([w.rstrip()  for w in open(INPUT_FILE_NAME)]))


    # matrix of size mxn
    m = int(input_mat[0].rsplit()[0])
    n = int(input_mat[0].rsplit()[1])

    # remove first element from maze structure
    input_mat.remove(input_mat[0])

    # actual maze structure
    input_mat = ([w.rsplit() for w in input_mat])


    visited = []

    for i in range(m):
        row = []
        for j in range(n):
            row.append(False)
        visited.append(row)


    i, j = 0, 0
    cell = (input_mat[i][j]).split('-')
    current_colour, current_direction = cell[0], cell[1]
    path_taken.append(current_direction)
    colour_taken.append(current_colour)

    found_path = traverse(input_mat, visited, i, j, current_colour, current_direction,
                m, n)

    path_taken_formatted = ""

    cur_direction = ''
    cur_colour = ''
    counter = 0


    for direction, colour in zip(path_taken, colour_taken):
        if cur_direction == '':
            cur_direction = direction
            cur_colour = colour
        elif (cur_direction != direction or cur_colour != colour):
            path_taken_formatted += ' ' + str(counter) + cur_direction

            counter = 0
            cur_direction = direction
            cur_colour = colour

        counter += 1

    if counter >= 1:

        path_taken_formatted += ' ' + str(counter) + cur_direction
    else:
        path_taken_formatted += ' ' + cur_direction

    output_file = open(OUTPUT_FILE_NAME,"w")
    output_file.write(path_taken_formatted.strip())

if __name__ == "__main__":
    main()
