from pyspark import SparkConf, SparkContext
import numpy as np

def pyspark_kmeans(data_file, c_file, max_iter=100):
    """
    :param data_file: (text file) contains all points
    :param c_file: (text file) contains the starting centroids
    :param max_iter:(int) maximum # of iterations
    :return: (text file) contains the final seeds
    """
    data = sc.textFile(data_file).map(lambda l: np.array([float(i) for i in l.split(' ')])).cache()
    c_ini= sc.textFile(c_file).map(lambda l: np.array([float(i) for i in l.split(' ')])).collect()

    c = np.array(c_ini[:])
    
    for num_iter in range(max_iter):
        # group the points by centroids
        group = data.map(lambda l: (np.argmin([np.linalg.norm(l-i) for i in c]), (l, 1)))
        group_sum = group.reduceByKey(lambda n1, n2: (n1[0] + n2[0], n1[1] + n2[1])).sortByKey(ascending=True)
        # new centroids
        c_new = np.array(group_sum.map(lambda l: l[1][0]/l[1][1]).collect())
        
        if np.linalg.norm(c - c_new) == 0:
            break
        else:
            c = c_new
    
    # write the final seeds to text file
    file = open("final.txt", "w")
    for items in c:
        temp = ""
        for n in items:
            temp += str(n)+ " "
        file.write(temp + "\n")
    file.close()
        
    return
      
    
if __name__ == "__main__":
    sc = SparkContext('local[4]', 'pyspark_kmeans')
    pyspark_kmeans('data.txt', 'c1.txt')
    sc.stop()
