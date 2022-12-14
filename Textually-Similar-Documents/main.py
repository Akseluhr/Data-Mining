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
import os
import sys
import time
import numpy as np
from comparesignatures import CompareSignatures
from datareader import DataReader
from lsh import LSH
from minhashing import MinHashing
from shingling import Shingling

from comparesets import CompareSets

data_reader = DataReader()
shingling_docs = Shingling()
min_hashing = MinHashing()
lsh = LSH()

shingling_docs.__int__(10)
min_hashing.__int__(5)
lsh.__int__(5, 0.2)

path_to_files = './data/'

clean_documents = DataReader.read_and_pre_process_all_documents(data_reader, path_to_files)

document_1_shingles = shingling_docs.create_shingles(clean_documents[0])
document_2_shingles = shingling_docs.create_shingles(clean_documents[1])
document_3_shingles = shingling_docs.create_shingles(clean_documents[2])
document_4_shingles = shingling_docs.create_shingles(clean_documents[3])
document_5_shingles = shingling_docs.create_shingles(clean_documents[4])
document_6_shingles = shingling_docs.create_shingles(clean_documents[5])

print(CompareSets.compute_j_similarity(document_3_shingles, document_6_shingles))
print(CompareSets.compute_j_similarity(document_1_shingles, document_3_shingles))
print(CompareSets.compute_j_similarity(document_1_shingles, document_4_shingles))
print(CompareSets.compute_j_similarity(document_1_shingles, document_5_shingles))
print(CompareSets.compute_j_similarity(document_1_shingles, document_6_shingles))

# char_matrix = shingling_docs.create_characteristics_matrix(['They', 'This'])
# signature_matrix = min_hashing.compute_min_hash_signature_matrix(char_matrix)
# candidate_pairs = lsh.find_similar_documents(signature_matrix)
#
# print('Following pair represents the similar text files: ', candidate_pairs)

# file_dir = current path to the project
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)


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
    char_matrix, jaccard_similarities, start_time, end_time = shingling_docs.create_characteristics_matrix(
        clean_documents, True)
    print("Jaccard Similarities, Shingling:")
    print("--------- %s seconds ---------" % (end_time - start_time))

    # print(jaccard_similarities)
    # print("-"*75)

    # Find and Time Jaccard similarity estimate using min hash signature matrix
    signature_matrix = min_hashing.compute_min_hash_signature_matrix(char_matrix)
    np.array(signature_matrix)
    signature_matrix_trans = signature_matrix.T

    start_time = time.time()
    jaccard_similarities_est = []
    for i in range(len(signature_matrix_trans - 1)):
        for j in range(len(signature_matrix_trans - 1)):
            if i != j:
                jaccard_similarities_est.append(
                    (j, c_sig.compare2(c_sig, signature_matrix_trans[i], signature_matrix_trans[j])))
    print("Jaccard Similarities Estimate, MinHash:")
    end_time = time.time()
    print("--------- %s seconds ---------" % (end_time - start_time))
    # print(jaccard_similarities_est)
    # print("-"*75)

    # Find and Time Jaccard similarity estimate using LSH (threshold = .8)
    candidate_pairs, start_time, end_time = lsh.find_similar_documents(signature_matrix)
    print('Threshold, .8: LSH: ')
    print("--------- %s seconds ---------" % (end_time - start_time))
    print("Similar documents: ", candidate_pairs)


main()
