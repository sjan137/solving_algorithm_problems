def self_num():
    num_list = set(range(1, 10001))
    not_self_num = set()
    for a_1000 in range(10):
        for a_100 in range(10):
            for a_10 in range(10):
                for a_1 in range(10):
                    not_self_num.add(1001 * a_1000 + 101 * a_100 + 11 * a_10 + 2 * a_1)
    self_num = list((num_list - not_self_num))
    self_num.sort()
    for self_number in self_num:
        print(self_number)

self_num()