def checkio(data):
    # just use dynamic programming
    # 1 3 6 .
    # 2 5 . .
    # 4 / . .
    # 7 . . . <- result
    pass

if __name__ == "__main__":
    print checkio([[1,2],[3,4],[1,5],[2,6],[4,8],[5,6],[6,7],
                   [7,8],[6,10],[7,11],[8,12],[10,11],
                   [10,14],[12,16],[14,15],[15,16]])
