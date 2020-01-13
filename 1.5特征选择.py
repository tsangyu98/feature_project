from sklearn.feature_selection import VarianceThreshold

# 通过对方差的过滤进行特征选择
vt = VarianceThreshold(threshold=0)
data = vt.fit_transform([[0, 2, 0, 3],
                         [0, 1, 4, 3],
                         [0, 1, 1, 3]]
                        )
print(data)

