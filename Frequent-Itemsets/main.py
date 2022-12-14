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
            if singleton[0] not in item:
                candidate = tuple(sorted(item + singleton))
                if candidate not in candidates:
                    candidates[candidate] = 0
    return candidates


def count_candidates(baskets, candidates, candidate_length, total_length):
    for basket in baskets:
        basket_variations = itertools.combinations(basket, candidate_length)
        for combination in basket_variations:
            if combination in candidates:
                candidates[combination] += (1 / total_length) * 100
    return candidates


def find_confidence_for_each_permuted_pair(item_set_permuted, position, frequent_item_sets):
    # print('THE ITEM SET PERMUTED WITH LENGTH ::', item_set_permuted, len(item_set_permuted))
    left_side = item_set_permuted[:position]
    # print('Step1: ', item_set_permuted, before_arrow, arrow_position)
    union_support = find_support_value(item_set_permuted, frequent_item_sets)
    single_support = find_support_value(left_side, frequent_item_sets)
    # print('UNION SUPPORT AND SINGLE SUPPORT :', union_support, single_support)
    return union_support / single_support


def find_support_value(item_set_permuted, frequent_item_sets):
    # print("FREQUENT ITEMS ::", frequent_item_sets)
    # print('GET SUPPORT :: ', item_set_permuted, frequent_item_sets[len(item_set_permuted) - 1][tuple(sorted(
    # item_set_permuted))], )
    return frequent_item_sets[len(item_set_permuted) - 1][tuple(sorted(item_set_permuted))]


def find_frequent_items():
    support = 1
    frequent_item_sets = []
    baskets = dat_to_df('/T10I4D100K.dat')

    singletons_count, singletons_count_with_percentage = count_singletons_from_baskets(baskets, len(baskets))
    filtered_items = filter_frequent_items(singletons_count_with_percentage, support)

    frequent_singletons = {(i,): filtered_items[i] for i in filtered_items}
    frequent_item_sets.append(frequent_singletons)
    print("Total number of frequent singletons found:", len(frequent_item_sets[0]))
    print("Frequent singletons:", frequent_singletons)

    k = 1
    while len(frequent_item_sets[k - 1]) > 0:
        candidates = generate_candidates(frequent_item_sets[k - 1], frequent_item_sets[0])
        candidates_count = count_candidates(baskets, candidates, k + 1, len(baskets))
        frequent_item_set = filter_frequent_items(candidates_count, support)
        frequent_item_sets.append(frequent_item_set)
        print("Total number of frequent " + str(k + 1) + "- tuples found:", len(frequent_item_sets[k]))
        print("Frequent " + str(k + 1) + "- tuples:", frequent_item_sets[k])
        k += 1

    return frequent_item_sets


def find_association_rules_from_frequent_items(frequent_item_sets):
    confidence = 0.5
    associations = set()

    for frequent_item_set in frequent_item_sets[1:]:
        for item_set in frequent_item_set:
            for item_set_permutations in itertools.permutations(item_set, len(item_set)):
                # print('PERMUTED :: ', item_set_permutations)
                for position in reversed(range(1, len(item_set_permutations))):
                    c = find_confidence_for_each_permuted_pair(item_set_permutations, position, frequent_item_sets)
                    # print('Confidence :', c)
                    if c >= confidence:
                        # print('Association found : ', item_set_permutations[:position], ' -> ',
                        #       item_set_permutations[position:], ' : ', c)
                        associations.add((', '.join(
                            map(str, sorted(item_set_permutations[:position]))) + ' -> ' + ', '.join(
                            map(str, sorted(item_set_permutations[position:]))), c))
                    else:
                        # Known rule: If A,B,C -> D is below confidence so that A,B -> C,D.
                        # So no need to iterate over arrow positions further
                        break

    print("Associations:")
    for association in associations:
        print(association)


def main():
    frequent_item_sets = find_frequent_items()
    find_association_rules_from_frequent_items(frequent_item_sets)


main()
