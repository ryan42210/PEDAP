import math as m

def mean(data_l: list)->float:
    res = 0
    for i in data_l:
        res += i
    
    return res/len(data_l)


def std_dev(data_l: list, sample=False)->float:
    tmp = 0
    avg = mean(data_l)
    for i in data_l:
        tmp += (i - avg)**2

    if (sample):
        res = m.sqrt(tmp/len(data_l))
    else:
        res = m.sqrt(tmp/(len(data_l)-1))
    
    return res


def std_dev_m(data_l: list)->float:
    tmp = std_dev(data_l, True)
    return tmp/m.sqrt(len(data_l))


def uncern_a(sigma_N: float, measure_num: int, confi_prob = '0.95')->float:
    c_prob_col = {'0.683':0, '0.90': 1, '0.95':2, '0.98': 3, '0.99': 4}
    if confi_prob not in c_prob_col.keys():
        # Todo
        raise KeyError

    if measure_num > 11 or measure_num < 3:
        # Todo
        raise Exception

    with open('file.csv') as f:
        t_table = f.readlines()

    tp = t_table[measure_num-1].split(',')
    return float(tp[c_prob_col[confi_prob]])*sigma_N

