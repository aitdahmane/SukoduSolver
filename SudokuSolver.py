#creation du tableau des numéros

table = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#identifier les cases vides

def trouver_case_vide (table):
    for i in range(len(table)):
        for j in range (len(table[0])):
            if table[i][j] == 0:
             return ( i, j)
    return None

def trouver_num_valide(table, numero, position):

 #verifier la ligne

                for i in range(len(table)):
                   if table[position[0]][i] == numero and position[1] != i:
                    return False

#verifier la column

                for i in range(len(table)):
                    if table[i][position[1]] == numero and position[0] != i:
                        return False


                cordonne_x = position[1] // 3
                cordonne_y = position[0] // 3

                for i in range(cordonne_y*3, cordonne_y*3+3):
                   for i in range(cordonne_x * 3, cordonne_x * 3 + 3):
                       if table[i][j] == numero and (i, j) != position:
                           return False


def resoudre(table):
    vide_case = trouver_case_vide(table)
    if not vide_case:
        return True
    else:
        row, col = vide_case

    for i in range(1,10):
        if trouver_num_valide(table, i, (row, col)):
            table[row][col] = i

            if resoudre(table):
                return True

            table[row][col] = 0

    return False
