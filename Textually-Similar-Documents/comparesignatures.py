import numpy as np


# class CompareSignatures:
#    def __init__(self):
#        pass

#    def signature_similarity(self,  signature, column_c, column_d):
# the fraction of elements with equal minhash signatures
#       return np.mean(signature[:, column_c] == signature[:, column_d])
#
class CompareSignatures:
    # vec1 and vec2 = minhash signatures

    def __init__(self):
        pass

    def signature_similarity(signature, column_c, column_d):
        return np.mean(signature[:, column_c] == signature[:, column_d])

    # Estimate of jaccard similarity
    # We will compare this with the actual jaccard similarity
    @staticmethod
    def compare(self, signature_matrix):
        length_doc = len(signature_matrix[0])
        total_docs = len(signature_matrix)
        jaccard_similarity_estimate = []
        # For each col (documents)

        for curr_doc in range(total_docs - 1):  # 0
            count = 0
            for compare_doc in range(length_doc):
                # avoid same doc comparisons
                if signature_matrix[curr_doc][compare_doc] == signature_matrix[curr_doc + 1][compare_doc]:
                    count += 1
            jaccard_similarity_estimate.append([curr_doc + 2, count / length_doc])
        return jaccard_similarity_estimate

    @staticmethod
    def compare2(self, col_1, col_2):
        length_doc = len(col_1)
        count = 0

        for i in range(length_doc):
            if col_1[i] == col_2[i]:
                count += 1
        result = count / length_doc
        return result
