from sklearn.impute import SimpleImputer
import numpy as np

si = SimpleImputer(missing_values=np.nan, strategy='mean')

data = si.fit_transform([[1, 2],
                         [np.nan, 3],
                         [7, 6]]
                        )

print(data)
