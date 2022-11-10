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
from shingling import Shingling
from minhashing import MinHashing

document1 = "This"
document2 = "They"

ss = Shingling()
mh = MinHashing()
ss.__int__(2)
mh.__int__(100)
char_matrix = ss.create_characteristics_matrix([document1, document2])  # return a set of hashed values for shingles
signature_matrix = mh.compute_min_hash_signature_matrix(char_matrix)

print(signature_matrix)

#
# cs = CompareSets()
#
# print(cs.compute_jaccard_similarity([1,2,3,4], [1,2,5])) # 2/5 = 0.4 similarity
