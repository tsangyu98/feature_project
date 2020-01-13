from sklearn.preprocessing import StandardScaler

# 标准化就是将数据转换为均值为0，标准差为1的数据
sd = StandardScaler()
res = sd.fit_transform([[1., -1., 3.],
                        [2., 4., 2.],
                        [4., 6., -1.]]
                       )
print(res)
