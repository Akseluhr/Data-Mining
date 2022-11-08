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
