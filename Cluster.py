from sklearn.cluster import KMeans

def cluster(vectors):

    num_clusters = 3
    km_cluster = KMeans(n_clusters = num_clusters, max_iter = 300, n_init = 40, \
                        init='k-means++', n_jobs = -1)

    result = km_cluster.fit_predict(vectors)

    #print(result)

def vectorize():

    pass

def title_similarity():

    pass

def ingredient_similarity():

    pass

def category_similarity():

    pass


