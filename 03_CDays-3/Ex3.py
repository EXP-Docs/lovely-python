#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    在一个 8×8 国际象棋盘上，有 8 个皇后，每个皇后占一格；要求皇后间不会出现相
    互“攻击”的现象，即不能有两个皇后处在同一行、同一列或同一对角线上，问共
    有多少种不同的方法。
'''


''' 检查皇后是否发生攻击 '''
def check_attrack(chess_pos, x, y):
    is_attrack = False
    for pos in chess_pos:
        r = pos[0]
        c = pos[1]
        if x == r or y == c or (x - r == y - c) or (x - r == c - y):
            is_attrack = True
            break
    return is_attrack
# def check_attrack


''' 深搜解 '''
def dfs(chess_pos, x, y, queen, all_results):
    if x > 8 or y > 8 or queen > 8:
        return

    if not check_attrack(chess_pos, x, y):
        chess_pos.append([x, y])
        queen += 1
        if queen == 8:
            all_results.append(chess_pos[:])    # 利用切片复制数组，不然会被后面的remove操作清空解
        else:
            for xx in range(x + 1, 9): # 逐行检索
                for yy in (range(1, y) + range(y + 1, 9)): # 选择非当前列的合适列
                    dfs(chess_pos, xx, yy, queen, all_results)
        chess_pos.remove([x, y])
    return
# def dfs


''' 迭代入口 '''
def eight_queen():
    all_results = []
    for y in range(1, 9):   # 避免旋转重复解，固定x，迭代y即可
        dfs([], 1, y, 0, all_results)
    return all_results
# def eight_queen


# 调用
all_results = eight_queen()
print "八皇后问题不重复解集："
for result in all_results:
    print "%s" % result
print "八皇后问题不重复解总数： {}".format(len(all_results))
