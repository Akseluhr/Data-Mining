import numpy as np
from nextprime import next_prime


class MinHashing:
    def __int__(self, number_of_hash_signature=100):
        self.number_of_hash_signature = number_of_hash_signature

    def compute_min_hash_signature_matrix(self, characteristic_matrix):
        number_of_min_hashes = self.number_of_hash_signature
        (number_of_shingles, number_of_documents) = characteristic_matrix.shape

        # print(number_of_min_hashes, number_of_shingles, number_of_documents)

        # signature matrix with infinity from book
        signature_matrix = np.full((number_of_min_hashes, number_of_documents), np.inf)

        #print(signature_matrix)

        p = next_prime(number_of_shingles)
        a = 2 * np.random.randint(0, p // 2, number_of_min_hashes) + 1  # a is always an odd number
        b = np.random.randint(0, p, number_of_min_hashes)

        # print(p, a, b)

        # print(characteristic_matrix.tolil().rows)

        for row_idx, document_ids in enumerate(characteristic_matrix.tolil().rows):
            # print('ROWS IDX ::', a, row_idx, a * row_idx)
            """ compute number_of_hash_signature independent hash functions """
            hashes = ((a * row_idx + b) % p) % number_of_shingles

            #print('HASHES "', hashes)

            for document_id in document_ids:
                #print(document_id)
                #print('DEBUG :: ', document_id, hashes, signature_matrix[:, document_id], hashes < signature_matrix[:, document_id] )
                signature_matrix[:, document_id] = np.where(hashes < signature_matrix[:, document_id],
                                                            hashes, signature_matrix[:, document_id])
                #print('SIG MAT ::', signature_matrix)


        return signature_matrix
