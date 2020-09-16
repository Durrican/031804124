import jieba.analyse
import re
import math


def clear(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        lines1 = ''.join(lines)
        punc = '~`!#$%^&*()_+-=|\';":/.,?><~·！@#￥%……&*（）——+-=“：’；、。，？》《{}'
        s = re.sub(r"[%s]+" % punc, "", lines1)
        res = []
        for line in s:
            a = line.split()
            a_res = ''.join(a)
            res.append(a_res)
            res_res = ''.join(res)
    return res_res


def TF(txt):
    len_in = len(txt)
    if len_in < 40:
        topk = round(len_in / 4) + 1
    elif 400 > len_in >= 40:
        topk = round(len_in / 10) + 1
    elif 2000 > len_in >= 400:
        topk = round(len_in / 20) + 1
    else:
        topk = round(len_in / 40)
    key_word = jieba.analyse.extract_tags(txt, topK=topk, withWeight=False)
    return key_word


def coscompare(res1_tf, res2_tf):
    s1_cut = res1_tf
    s2_cut = res2_tf

    word_set = set(s1_cut).union(set(s2_cut))
    word_dict = dict()
    i = 0
    for word in word_set:
        word_dict[word] = i
        i += 1

    len1 = len(word_dict)
    s1_code = [0] * len1
    s2_code = [0] * len1

    for word in s1_cut:
        s1_code[word_dict[word]] += 1

    for word in s2_cut:
        s2_code[word_dict[word]] += 1

    sum = 0
    sq1 = 0
    sq2 = 0
    for i in range(len(s2_code)):
        sum += s1_code[i] * s2_code[i]
        sq1 += pow(s1_code[i], 2)
        sq2 += pow(s2_code[i], 2)
    res = round((float(sum) / (math.sqrt(sq1) * math.sqrt(sq2))), 2)
    return res


files = input()
title = files.split(' ')
files1 = title[0]
files2 = title[1]
outfile = title[2]
res1 = clear(files1)
res2 = clear(files2)
res1_TF = TF(res1)
res2_TF = TF(res2)
res_final = coscompare(res1_TF, res2_TF)
res_final = str(res_final)
file = open(outfile, 'w', encoding='utf-8')
file.write(res_final)
file.close()

