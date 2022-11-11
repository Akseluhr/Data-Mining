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
from lsh import LSH

document1 = "This is a similar document let see what happens"
document2 = "Yo what the flux man you sum goodie"
document3 = "This is a almost similar document let see what happens"
document4 = "Yo what the flux man you sum goodie"

ss = Shingling()
mh = MinHashing()
lsh = LSH()
ss.__int__(2)
mh.__int__(100)
lsh.__int__(50, 0.8)
char_matrix = ss.create_characteristics_matrix([document1, document2, document3, document4])
signature_matrix = mh.compute_min_hash_signature_matrix(char_matrix)
candidate_pairs = lsh.find_similar_documents(signature_matrix)

print(candidate_pairs)
#
# cs = CompareSets()
#
# print(cs.compute_jaccard_similarity([1,2,3,4], [1,2,5])) # 2/5 = 0.4 similarity
