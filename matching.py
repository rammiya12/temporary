# The 'matching' module allows you to:
#  - Given a group of people, match Santas and Santees (= recipients of a
#    present!) so that:
#      - Everyone is giving one present, and receiving one present
#      - No-one is giving a present to themselves!

import random


#####################
# Week 2, or after learning about if statements
#####################

# Given the size of the round, and the current position, return the next
# position. Note that:
#   - Positions start from zero, and end at size-1. For example, if the size is
#     4, then the available positions are: 0, 1, 2, 3.
#   - After the last position, we go back to 0 (it's a circle!)
#
# >>> next_in_round(4, 0)
# 1
# >>> next_in_round(4, 1)
# 2
# >>> next_in_round(4, 2)
# 3
# >>> next_in_round(4, 3)
# 0
#
# You can assume that the position will always be between 0 and size-1.
def next_in_round(size, position):
    if position >= size:
        return "Input invalid"
    if position == size - 1:
        return 0
    return position + 1


#####################
# Week 3, or after learning about lists
#####################

# Given a list of some items, and a position, exchange the element at the given
# position with the element after it in the round. (As in, if the given position
# is the last element of the list, exchange that element with the first
# element!)
#
# This function should not return anything, it will just modify the list.
#
# So if we have a list:
# >>> names = ["Anita", "Ben", "Cecilia", "Daan"]
#
# And call this function to swap some elements, the list will be modified
# accordingly:
# >>> swap_with_next(names, 3)
# >>> names
# ['Daan', 'Ben', 'Cecilia', 'Anita']
def swap_with_next(items, pos):
    next_pos = next_in_round(len(items), pos)
    pos_2 = items[pos]
    items[pos] = items[next_pos]
    items[next_pos] = pos_2


#    return items

#####################
# Week 4, or after learning about for loops
#####################

# Given two lists (with the same items, but we won't actually check that!),
# changes them so that no element is in the same position in both lists.
#
# A good way to do this is to go through all the positions one by one. If at a
# certain position, the elements in both lists match, we can modify the second
# list by swapping the item at that position with the next one.
#
# So if we have the following lists:
# >>> names1 = ['Anita', 'Ben', 'Cecilia', 'Daan']
# >>> names2 = ['Anita', 'Cecilia', 'Ben', 'Daan']
#
# Where initially, positions 0 and 3 match (both lists have "Anita" and "Daan"
# in those positions, respectively).
#
# Then calling this function should fix the matching positions:
# >>> fix_matching_values_with_swaps(names1, names2)
#
# And we might get something like
# >>> names1
# ['Anita', 'Ben', 'Cecilia', 'Daan']
# >>> names2
# ['Daan', 'Anita', 'Ben', 'Cecilia']
#
# You can assume that both lists have the same length, or optionally print an
# error message if they don't.
def fix_matching_values_with_swaps(items1, items2):
    for i in range(0, len(items1)):
        # if both items equal in position i
        if items1[i] == items2[i]:
            swap_with_next(items2, i)



# Given two lists, one containing Santas, the other containing their matching
# Santees (= the people receiving the gifts), fix the lists so that no one gets
# matched with themselves.
#
# To implement this function, you should call a previously implemented function!
def fix_so_nobody_gets_their_own_name(santas, santees):
    # this will not work if two people have same name...
    fix_matching_values_with_swaps(santas, santees)


#####################
# Week 4, or after learning about dictionaries
#####################

# Given two lists of the same size, build a dictionary where the keys are taken
# from the first list, and the values are the corresponding elements in the
# second list.
#
# >>> names1 = ['Anita', 'Ben', 'Cecilia', 'Daan']
# >>> names2 = ['Ben', 'Daan', 'Anita', 'Cecilia']
# >>> merge_lists_to_dictionary(names1, names2)
# {'Anita': 'Ben', 'Ben': 'Daan', 'Cecilia': 'Anita', 'Daan': 'Cecilia'}
#
# You can assume that items1 and items2 have the same length, or optionally
# print an error message if they don't.
def merge_lists_to_dictionary(list1, list2):
    dct = {}
    for i in range(0, len(list1)):
        dct[list1[i]] = list2[i]
    return dct


#####################
# Week 5, or after learning about random
#####################

# Given a list, returns a copy of the list with the elements in random order.
# Note that this should not modify the original list!
#
# >>> original_list = [1, 2, 3, 4, 5]
# >>> randomized_list = shuffled_copy(original_list)
#
# Then the randomized list very likely has the elements in some different order:
# >>> randomized_list
# [4, 2, 5, 1, 3]
# And the original list definitely still has the original order:
# >>> original_list
# [1, 2, 3, 4, 5]
def shuffled_copy(items):
    copy_list = items.copy()
    return random.shuffle(copy_list)


# This function represents the way Santees are assigned to the Santas.
# Imagine we have each name written on a piece of paper, we put all these pieces
# of paper in a bag, and pull them out one by one (so they come out in a random
# order).
#
# To implement this function, you should call a previously implemented function!
def name_bag(names):
    return shuffled_copy(names)

# Given a list of the names of all participants, create a random Santa
# assignment. Make sure no-one gets assigned to give a present to themselves!
#
# Hints:
#   - Pull names out of a bag first
#   - Then fix the order to make sure no one gets their own name :)
#
# The order is random, so you probably won't see exactly the same results, but
# here's an example:
#
# >>> names = ['Anita', 'Ben', 'Cecilia', 'Daan']
# >>> build_santa_assignment(names)
# {'Anita': 'Ben', 'Ben': 'Daan', 'Cecilia': 'Anita', 'Daan': 'Cecilia'}
def build_santa_assignment(names):
    names_out_of_a_bag = name_bag(names) # names out of a bag in random order
    fix_so_nobody_gets_their_own_name(names, names_out_of_a_bag)
    return merge_lists_to_dictionary(names, names_out_of_a_bag)