# encoding: utf-8


def isRight(mat, rows, cols, row, col, path, visited):
    if path == "":
        print "here"
        return True

    flag1 , flag2, flag3, flag4 = False, False, False, False
    if path[0] == mat[row][col]:
        visited[row][col] = 1

        if row-1 >= 0  and visited[row-1][col] == 0:
            print "row-1"
            visited[row - 1][col] = 1
            flag1 = isRight(mat, rows, cols, row-1, col, path[1:], visited)
            visited[row - 1][col] = 0

        if row+1 < rows and visited[row + 1][col] == 0:
            print "row+1"
            visited[row + 1][col] = 1
            flag2 =isRight(mat, rows, cols, row+1, col, path[1:], visited)
            visited[row + 1][col] = 0

        if col + 1 < cols and visited[row][col+1] == 0:
            print "col+1"
            visited[row ][col+1] = 1
            flag3 =isRight(mat, rows, cols, row, col+1, path[1:], visited)
            visited[row][col+1] = 0

        if col - 1 >= 0 and visited[row][col-1] == 0:
            print "col-1"
            visited[row][col-1] = 1
            flag4 = isRight(mat, rows, cols, row, col-1, path[1:], visited)
            visited[row][col-1] = 0

        if path[1:] == "":
            return True

        visited[row][col] = 0

    else :
        return  False

    return flag1 or flag2 or flag3 or flag4

def hasPath( tstr, rows, cols, path):
    visited = [[0 for i in range(cols)] for j in range(rows)]
    mat = [[tstr[j * cols  + i] for i in range(cols)] for j in range(rows)]

    print mat
    for i in range(rows):
        for j in range(cols):
            if isRight(mat, rows, cols, i, j, path, visited):
                return True

    return False

if __name__ == '__main__':
    #mat = [['a','b','c','e'],['s','f','c','s'],['a','d','e','e']]
    tstr = "AAAAAAAAAAAA"
    #tstr = "ABCESFCSADEE"

    rows, cols = 3, 4
    path = "AAAAAAAAAAAA"

    #path = 'BCCED'
    print hasPath(tstr, rows, cols, path)

