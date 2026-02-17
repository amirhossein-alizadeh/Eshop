def group_list(list, size=4):
    res_list = []
    for i in range(0, len(list), size):
        res_list.append(list[i:i + size])
    return res_list
