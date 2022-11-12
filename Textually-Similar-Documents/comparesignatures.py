import numpy as np


class CompareSignatures:
    @staticmethod
    def signature_similarity(signature, column_c, column_d):
        # the fraction of elements with equal minhash signatures
        return np.mean(signature[:, column_c] == signature[:, column_d])
