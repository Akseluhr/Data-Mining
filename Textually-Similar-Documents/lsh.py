import math
from collections import defaultdict
import itertools

from comparesignatures import CompareSignatures


class LSH:

    def __int__(self, number_of_bands=100, similarity_threshold=0.8):
        self.number_of_bands = number_of_bands
        self.similarity_threshold = similarity_threshold

    def find_candidates_pairs_from_signature_matrix(self, signature_matrix):
        number_of_bands = self.number_of_bands
        (number_of_signature, number_of_documents) = signature_matrix.shape

        print('num of sig: ', number_of_signature, 'num of docs', number_of_documents)

        rows_per_band = math.ceil(number_of_signature / number_of_bands)

        print('num of rows per band: ', rows_per_band)

        candidate_pairs = set()
        column_buckets = defaultdict(list)

        print('Initial Column buckets and Candidate Pairs: ', column_buckets, candidate_pairs)

        for band_idx in range(number_of_bands):

            print(band_idx)

            band = signature_matrix[band_idx * rows_per_band: (band_idx + 1) * rows_per_band]

            print('Band::', band)

            for document_id, column in enumerate(band.T):
                print('doc id: ', document_id, ' column: ', column)
                column_buckets[tuple(column)].append(document_id)

            print('column buckets: ', column_buckets)

            for document_ids in column_buckets.values():
                print('doc ids in column bucket :', document_ids)
                pairwise_combinations = itertools.combinations(document_ids, 2)
                candidate_pairs.update(pairwise_combinations)
                print('candidate pairs :', candidate_pairs)

            column_buckets.clear()

        return candidate_pairs

    def find_similar_documents(self, signature_matrix):
        candidate_pairs = self.find_candidates_pairs_from_signature_matrix(signature_matrix)
        similar_documents = []

        for candidate in candidate_pairs:
            document_similarity = CompareSignatures.signature_similarity(signature_matrix, *candidate)
            if document_similarity > self.similarity_threshold:
                similar_documents.append(candidate)

        return similar_documents
