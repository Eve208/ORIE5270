from pyspark import SparkConf, SparkContext
import numpy as np

def mat_mult_vec(matrix_file,vector_file):
    """
    :param matrix_file:(text file) contains the matrix, with the first col as row index
    :param vector_file:(text file) contains the vector
    :return: (rdd object) contains the output vector
    """
    mat = sc.textFile(matrix_file).map(lambda l: np.array([float(i) for i in l.split(",")])).cache()
    vec = sc.textFile(vector_file).map(lambda l: np.array([float(i) for i in l.split(",")])).cache()
    
    mat = mat.map(lambda l: (l[0], ((l[1+i], i) for i in range(len(l[1:])))))
    mat_flat = mat.flatMap(matCol)
    vec = vec.flatMap(addVecInd)
    
    mat_join = mat_flat.join(vec).map(lambda l: (l[1][0][0], l[1][0][1]*l[1][1]))
    result = mat_join.reduceByKey(lambda n1, n2: n1 + n2).map(lambda l: l[1])
    return result

def matCol(l):
    # generate (j,(i,val)) tuple
    for i in l[1]:
        yield(i[1], (l[0], i[0]))

def addVecInd(l):
     # add vevtor index
    for i in range(len(l)):
        yield(i, l[i])


if __name__ == '__main__':
    sc = SparkContext('local[4]', 'matrix_mult')
    mat_mult_vec("A.txt", "B.txt")
    sc.stop()
