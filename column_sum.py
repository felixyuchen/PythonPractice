#计算二维数组（矩阵）中每一列的元素之和，并以列表形式返回
def column_sum(matrix):
    if not matrix:
        return []

    rows = len(matrix)
    colums = len(matrix[0])
    col_sums = [0] * colums

    for col in range(colums):
        for row in range(rows):
            col_sums[col] += matrix[row][col]

    return col_sums


def main():
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    result = column_sum(matrix)
    print(result)


if __name__ == "__main__":
    main()
