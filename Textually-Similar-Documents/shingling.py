from scipy import sparse
import numpy as np
from comparesets import CompareSets


class Shingling:
    def __int__(self, k=10):
        self.k = k

    @staticmethod
    def hash_shingles(self, shingle, max_shingle_id=2 ** 32 - 1):
        val = 0
        for c in shingle:
            val = (val * 100 + ord(c)) % max_shingle_id
        return val

    def create_hashed_shingles(self, document):
        shingles_set = []
        for i in range(len(document) - self.k + 1):
            shingles_set.append(self.hash_shingles(self, document[i: i + self.k]))

        return sorted(set(shingles_set))

    def create_shingles(self, document):
        shingles_set = []
        for i in range(len(document) - self.k + 1):
            shingles_set.append(document[i: i + self.k])

        return sorted(set(shingles_set))

    # for creating characteristics matrix
    def create_hashed_shingles_for_all_documents(self, documents):
        documents_shingles = []
        for doc in documents:
            documents_shingles.append(self.create_hashed_shingles(doc))

        unique_shingles_set = set()
        for shingles in documents_shingles:
            for shingle in shingles:
                unique_shingles_set.add(shingle)

        shingle_with_ids = {shingle: idx for idx, shingle in enumerate(sorted(unique_shingles_set))}

        return documents_shingles, shingle_with_ids

    def create_characteristics_matrix(self, documents, check_similarity=False):
        documents_shingles, shingle_with_ids = self.create_hashed_shingles_for_all_documents(documents)
        c_sets = CompareSets()

        if check_similarity == True:
            jaccard_similarities = []
            for curr_doc in range(len(documents_shingles)):
                for compare_col in range(len(documents_shingles)):
                    if documents_shingles[curr_doc] != documents_shingles[compare_col]: #avoid same doc comparisons
                        jaccard_similarities.append((compare_col, c_sets.compute_j_similarity(documents_shingles[curr_doc], documents_shingles[compare_col])))
                
        number_of_documents = len(documents_shingles)  # column of characteristic matrix
        number_of_shingles = len(shingle_with_ids)  # row of characteristic matrix
        values = []
        for doc_id, shingles in enumerate(documents_shingles):
            for shingle in shingles:
                values.append((shingle_with_ids[shingle], doc_id, 1))

        shingle_indices, doc_indices, data = zip(*values)

        # create csr
        characteristic_matrix = sparse.csr_matrix((data, (shingle_indices, doc_indices)),
                                                  shape=(number_of_shingles, number_of_documents), dtype=np.bool_)

        return characteristic_matrix, jaccard_similarities
