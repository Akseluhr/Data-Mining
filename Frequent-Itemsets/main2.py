#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 16:40:13 2022

@author: akseluhr
"""

import itertools
import os
import sys


def dat_to_df(filename):
    curr_file_dirr = os.path.dirname(__file__)
    sys.path.append(curr_file_dirr)
    print(curr_file_dirr)
    doc = open(curr_file_dirr + '/data' + filename, 'r')
    transactions = [i.strip('\n, ').split(' ') for i in doc]
    return transactions


def count_singletons_from_baskets(baskets, length):
    count = {}
    count_with_percentage = {}
    for basket in baskets:
        for item in basket:
            if item in count:
                count[item] += 1
            else:
                count[item] = 1
            if item in count_with_percentage:
                count_with_percentage[item] += (1 / length) * 100
            else:
                count_with_percentage[item] = (1 / length) * 100
    return count, count_with_percentage


def filter_frequent_items(items_count, support_threshold):
    filtered_items = {}
    for item in items_count:
        if items_count[item] >= support_threshold:
            filtered_items[item] = items_count[item]

    return filtered_items


def generate_candidates(items, singletons):
    candidates = {}
    for item in items:
        for singleton in singletons:
            if singleton[0] not in item: #Not in candidate pair
                print("current item, is not in the dictionary", item)
                print("gets appended to candidate dict, is not in the dictionary", singleton)
                candidate = tuple(sorted(item + singleton))
                print("candidate", candidate)
                if candidate not in candidates:
                   # print("curr candidate", candidates[candidate])
                   print("curr candidate", candidate) 
                   candidates[candidate] = 0
                    
    print(candidates)
    return candidates


def count_candidates(baskets, candidates, candidate_length, total_length):
    for basket in baskets:
        basket_variations = itertools.combinations(basket, candidate_length)
        for combination in basket_variations:
            if combination in candidates:
                candidates[combination] += (1 / total_length) * 100
    return candidates


def main():
    support = 1  # 1 percent
    confidence = 0.5
    frequent_item_sets = []
    associations = set()

    baskets2 = dat_to_df('/T10I4D100K.dat')
    #transactions =[['l1', 'l2', 'l5'], ['l2', 'l4'], ['l2', 'l3'], ['l1', 'l2', 'l4'], ['l1', 'l3'], ['l2', 'l3'], ['l1', 'l3'], ['l1', 'l2', 'l3', 'l5'], ['l1', 'l2', 'l3']]
    baskets = [[11, 12, 15], [12, 14], [12, 13], [11, 12, 14], [11, 13], [12, 13], [11, 13], [11, 12, 13, 15], [11, 12, 13]]
    # baskets = baskets[:100]  # So we try with the first 20 transactions
    singletons_count, singletons_count_with_percentage = count_singletons_from_baskets(baskets, len(baskets))
    filtered_items = filter_frequent_items(singletons_count_with_percentage, support)
    # print(filtered_items)

    frequent_singletons = {(i,): filtered_items[i] for i in filtered_items}
    frequent_item_sets.append(frequent_singletons)
    print("Frequent singletons:", frequent_singletons)

    k = 1
    while len(frequent_item_sets[k - 1]) > 0:
        candidates = generate_candidates(frequent_item_sets[k - 1], frequent_item_sets[0])
        candidates_count = count_candidates(baskets, candidates, k + 1, len(baskets))
        frequent_item_set = filter_frequent_items(candidates_count, support)
        frequent_item_sets.append(frequent_item_set)
        print("Frequent " + str(k + 1) + "- tuples:", frequent_item_sets[k])
        k += 1

    for frequent_item_set in frequent_item_sets[1:]:
        for k_tuple in frequent_item_set:
            for tuple_permutation in itertools.permutations(k_tuple, len(k_tuple)):
                print(tuple_permutation)


main()