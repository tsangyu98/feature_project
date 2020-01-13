from sklearn.preprocessing import MinMaxScaler
import numpy as np
np.set_printoptions(suppress=True)

# 读取数据
with open('data.txt', 'r') as f:
    contents = f.readlines()

a = []
for content in contents:
    content = content.strip()
    content = content.split(' ')
    a.append(content)

a[5].remove('')
a[-3].remove('')
a[-1].remove('')
n = np.array(a)
data = n.astype('float')
data = data.tolist()

# 对数据进行归一化
mm = MinMaxScaler()
res = mm.fit_transform(data)
print(res)



