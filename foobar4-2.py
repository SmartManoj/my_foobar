def detect_inf_loop(a, b):
    number_sum = a + b
    if number_sum % 2:
        return True
    number_sum /= 2
    lower_number = a if a < b else b

    if not number_sum % lower_number:
        number_sum /= lower_number
        count = 1
        while count < number_sum:
            count <<= 1
        if count == number_sum:
            return False
    return True


def get_shortest_list(l):
    return min(l, key=lambda list_item: len(list_item) or 101)


def extract_values(l, first_value, second_value):
    if first_value in l:
        l.pop(l.index(first_value))

    if second_value in l:
        l.pop(l.index(second_value))

    return l


def item_matched_lists(l, searched_value):
    return [i for i, x in enumerate(l) if x == searched_value]


def non_empty_list_count(l):
    return len(filter(lambda x: len(x), l))


def answer(banana_list):
    count = 0

    banana_list = sorted(banana_list)

    match_list = [[second_item for second_item in banana_list if detect_inf_loop(item, second_item)] for item in
                  banana_list]

    current_min_list = get_shortest_list(match_list)

    while len(current_min_list) and non_empty_list_count(match_list) > 1:
        current_item = banana_list[match_list.index(current_min_list)]
        matched_item = current_min_list[0]
        for matched_item_index in item_matched_lists(banana_list, matched_item):
            if len(match_list[matched_item_index]):
                del match_list[matched_item_index][:]
                break
        del current_min_list[:]
        match_list = map(lambda x: extract_values(x, current_item, matched_item), match_list)
        count += 2
        current_min_list = get_shortest_list(match_list)

    return len(banana_list) - count

