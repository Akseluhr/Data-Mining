class CompareSignatures:
    # vec1 and vec2 = minhash signatures

    def __init__(self):
        pass

    # Estimate of jaccard similarity 
    # We will compare this with the actual jaccard similarity
    def compare(self, signature_matrix):
        length_rows = len(signature_matrix[0])
        length_cols = len(signature_matrix)
        count = 0
        
        # For each col (documents)
        for i in range(1, length_cols):
            # For each row (shingles)
            for j in range(length_rows):
                if(signature_matrix[i][j] == signature_matrix[i-1][j]):
                    count += 1
             
            # Non-necessary var declaration but good for readability
            jacc_estimate = count/length_rows
        print(jacc_estimate)
        
def main(): 
    example_matrix = [[1, 0, 1, 1, 0, 1, 0, 1], [0, 0, 1, 0, 1, 0, 0, 1]]
    compare_signatures = CompareSignatures()
    compare_signatures.compare(example_matrix)
    
    
main()
