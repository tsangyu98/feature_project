from sklearn.decomposition import PCA

pca = PCA(n_components=0.9)
data = pca.fit_transform([[2, 8, 4, 5],
                          [6, 3, 0, 8],
                          [5, 4, 9, 1]]
                         )
print(data)
