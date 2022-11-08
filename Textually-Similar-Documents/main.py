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