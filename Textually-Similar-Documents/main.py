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
from datareader import DataReader
from shingling import Shingling
from minhashing import MinHashing
from lsh import LSH
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







