# ----------------------------------------------------------------------------------------------------------------------
# playground

# shingle1 = 'abc'
# shingle2 = 'abc'
# shingle3 = 'abc'
#
# hashed_shingle = sum([pow(100, char_idx) * ord(character) for char_idx, character in enumerate(shingle1)]) % (2 ** 32)
# print(hashed_shingle)
#
# for index, c in enumerate(shingle2):
#     hashed_value = sum([pow(100, index) * ord(c)]) % (2 ** 32)
#
# print(hashed_value)
#
# val = 0
# for c in shingle3:
#     val = (val * 100 + ord(c)) % (2 ** 32)
#
# print(val)
#
#
# cs = CompareSets()
#
# print(cs.compute_jaccard_similarity([1,2,3,4], [1,2,5])) # 2/5 = 0.4 similarity
# ----------------------------------------------------------------------------------------------------------------------

# For module imports
import sys, os

# file_dir = current path to the project
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)


import matplotlib.pylab as plt
from datareader import DataReader
from shingling import Shingling
from minhashing import MinHashing
from lsh import LSH
from comparesignatures import CompareSignatures
import numpy as np
import time

def main():
    data_reader = DataReader()
    shingling_docs = Shingling()
    min_hashing = MinHashing()
    lsh = LSH()
    c_sig = CompareSignatures()
    
    shingling_docs.__int__(2)
    min_hashing.__int__(100)
    lsh.__int__(100, 0.8)
    
    path_to_files = file_dir + '/data/'
    
    clean_documents = DataReader.read_and_pre_process_all_documents(data_reader, path_to_files)
    
    # Find and Time Jaccard similarity using Shingles
    char_matrix, jaccard_similarities, start_time, end_time = shingling_docs.create_characteristics_matrix(clean_documents, True)
    print("Jaccard Similarities, Shingling:")
    print("--------- %s seconds ---------" % (end_time - start_time))

    #print(jaccard_similarities)
    #print("-"*75)
   
    # Find and Time Jaccard similarity estimate using min hash signature matrix
    signature_matrix = min_hashing.compute_min_hash_signature_matrix(char_matrix)
    np.array(signature_matrix)
    signature_matrix_trans = signature_matrix.T
    
    start_time = time.time()
    jaccard_similarities_est = []
    for i in range(len(signature_matrix_trans -1)):
        for j in range(len(signature_matrix_trans -1)):
            if i != j:
                jaccard_similarities_est.append((j, c_sig.compare2(signature_matrix_trans[i], signature_matrix_trans[j])))
    print("Jaccard Similarities Estimate, MinHash:")
    end_time = time.time()
    print("--------- %s seconds ---------" % (end_time - start_time))
    #print(jaccard_similarities_est) 
    #print("-"*75)

    
    # Find and Time Jaccard similarity estimate using LSH (threshold = .8)
    candidate_pairs, start_time, end_time = lsh.find_similar_documents(signature_matrix)
    print('Threshold, .8: LSH: ')
    print("--------- %s seconds ---------" % (end_time - start_time))
    #print(candidate_pairs)

main()







