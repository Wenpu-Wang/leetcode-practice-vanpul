# 题目描述
# 假设有k只小鸟和n个树洞，每只小鸟均匀随机选择一个树洞，给定n，计算当k不小于多少时，至少存在一对小鸟选择了同一个树洞这件事的概率不小于p（0<p<=1）
# 输入n（1<=n<=10000），p（0<p<=1），分别为树洞的数量和概率值
# 输出整数m，当k>=m时，至少存在一对小鸟选择了同一个树洞的概率>=p

while True:
    try:
        n, p = map(float, input().strip().split())
        print(n, p)
        q = 1 - p
        k = 0
        # 所有鸟不同洞概率prod，即至少一对鸟同树洞事件 的 对立事件
        # 当prod<q的时候，对立事件的概率>=p，得到k的解
        prod = 1
        while prod >= q:
            prod = prod * (1 - k/n)
            k += 1
        print(k)
    except:
        break

