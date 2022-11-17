import pandas as pd
import os,sys
from IPython.display import display
import itertools
def dat_to_df(filename):
  curr_file_dirr = os.path.dirname(__file__)
  sys.path.append(curr_file_dirr)
  print(curr_file_dirr)
  doc = open(curr_file_dirr + '/data' + filename, 'r')
  transactions = [i.strip('\n, ').split(' ') for i in doc] # Remove all new lines and split() splits a string into substrings whenever it finds a blank space.
  return transactions

def find_frequent_itemsets(tansactions, s, k=2):
    #unique_items = list(set(tansactions))
    #unique_items = {x for l in tansactions for x in l}
   # print(unique_items)
    unique_items = []
    for basket in tansactions:
        for item in basket: 
            if item not in unique_items: 
                unique_items.append(item)
    print('all unique items:', unique_items)

    support_singleton_item = []
    support_singleton_total = []
    support_doubleton_count = []
    support_tripleton_count = []
    
    
    count = 0
    # find support
    for i in range(k+1):
        if i == 0:
            for item in unique_items:
                for basket in tansactions:
                    if item in basket:
                        count += 1                
        
                
                if count >= s:
                    support_singleton_item.append(item)
                    support_singleton_total.append((item, count))
                count = 0
                    
            print('frequent singletons:', support_singleton_item)
            print('all counts', support_singleton_total)
        if i == 1: # step 2
            all_possible_pairs = list(itertools.combinations(support_singleton_item, 2))
           # print(all_possible_pairs) # all possible pairs of the frequent singletons
            count = 0
            for pair in all_possible_pairs:
                for basket in tansactions:
                    if (pair[0] in basket) and (pair[1] in basket):

                        count += 1
                      #  print(pair, basket, count)
                        
                if count >= s:
                    support_doubleton_count.append((pair, count))
                count = 0
                
                #for i in range(len(pair)):
                 #   if
            
            print("frequent doubletons:", support_doubleton_count)
        
        if i == 2: # step 3
            all_possible_pairs = list(itertools.combinations(support_singleton_item, 3))
            count = 0
            for pair in all_possible_pairs:
                for basket in tansactions:
                    if (pair[0] in basket) and (pair[1] in basket) and (pair[2] in basket):

                        count += 1
                      #  print(pair, basket, count)
                        
                if count >= s:
                    support_tripleton_count.append((pair, count))
                count = 0
                
                #for i in range(len(pair)):
                 #   if
            
            print("frequent tripletons:", support_tripleton_count)
                
    return list([support_singleton_total, support_doubleton_count, support_tripleton_count])

def calculate_confidence(doubletons, singletons):
    s_I = set(doubletons)
    s_j = set(singletons)
    print(s_j)
    confidence = []
    for dt in doubletons:
       print(dt)
       #comb = list(itertools.combinations(dt[0], 2))
       
       dt_support = dt[1] # <-- divide this with support of current I
       
       for j in singletons:
           if j[0] == dt[0][0]:
               print(j[1])
               confidence.append(dt[1] / j[1])
               
               
               
    print(confidence)
    #   j_support = s_j[]
      # if s_I in # If singleton is in 
    
    
def generate_association_rules(items, s, c):
    
    for entry in items:
        entry_length = len(entry)
        print(entry_length)
        for i in range(entry_length):
            print(entry[i][0][0])

def main():
    #transactions = dat_to_df('/T10I4D100K.dat') # <-- this guy is huge
    #transactions = transactions[:20] # So we try with the first 20 transactions
    
    test_trans =[['l1', 'l2', 'l5'], ['l2', 'l4'], ['l2', 'l3'], ['l1', 'l2', 'l4'], ['l1', 'l3'], ['l2', 'l3'], ['l1', 'l3'], ['l1', 'l2', 'l3', 'l5'], ['l1', 'l2', 'l3']]
    
    frequent_items = find_frequent_itemsets(test_trans, 2, 2)
    
    calculate_confidence(frequent_items[1], frequent_items[0])
    #generate_association_rules(frequent_items, 2, c=0.5)
main()


# Support to see how frequent a set of items is in a dataset. E.g. How often does {2, 5} occur in  [[2,5,3],[1,2,3][2,5,8]]

# Apriori algorithm was done for scalability



# Task 1:
# Support is the frequency (occurences) of the itemsets (A) or (A, B). Divide it by total num of items


# Out of set of items (A-E) and set of transactions (T1 - T5) (containing subsets of set of items)

# To find the support: 
# 1. Traverse the entire list of transactions
# 2. Find if your subitemset (e.g. (milk, bread) which is a doubleton itemset) occurs more than s time where s is the threshold 
    # 2b. start with singletons (milk)
    # 2c. then doubletons 
    # 2d up til the larges found basket (maybe we will find five baskets with e.g. 100 items, 99 of which are identical. if our threshold is 5, we will consider those itemsets as frequent itemsets 
    # Count the exact amount of occurences of those ITEMSETS that is greater than the threshold. This is the support. 
# For an itemset to be frequent, ALL its subsets must be frequent. 
    
    # Slide 17 important because apriori algorithm is based on this
    
    
# Task 2: 
# Generate association rules X - > Y Given a confidence threshold
# How likely is item(set) Y purchased when item(set) X is purchased?
# COnfidence is given by: 
    # support of I union J, where I and J are the number of occurances of an item(set) in transactions,in which Y also appears
    # E.g. in 5/10 transactions, beer occurs. In four of them, apples occur. Confidence is given by support(apple, beer) / support (apple) --> 0.8 
    
    
# We want to find INTERESTING associations. E.g. x --> milk is a very common rule, everyone buys milk 
# We can find this by computing the Interest of an association. Conf(I-->j) - conditional probability of j
    # keep the ones with high positive or negative interest values, usually above .5
    # getting the conditional probability of j --> number of occurences / number of transactions
    