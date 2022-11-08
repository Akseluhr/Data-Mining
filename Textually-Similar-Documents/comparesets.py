class CompareSets:
    @staticmethod
    def compute_jaccard_similarity(set_one, set_two):
        set_1 = set(set_one)
        set_2 = set(set_two)

        jaccard_similarity_value = len(set_1.intersection(set_2)) / len(set_1.union(set_2))

        return jaccard_similarity_value
