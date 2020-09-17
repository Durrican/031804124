import jieba.analyse
import re
import math


class Testt():



    def cclear(f1,f2):
        with open(f1, 'r', encoding='utf-8') as f:
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
        len_in = len(res_res)
        if len_in < 40:
            topk = round(len_in / 4) + 1
        elif 400 > len_in >= 40:
            topk = round(len_in / 10) + 1
        elif 2000 > len_in >= 400:
            topk = round(len_in / 20) + 1
        else:
            topk = round(len_in / 40)
        key_word = jieba.analyse.extract_tags(res_res, topK=topk, withWeight=False)
        m1=key_word
        with open(f2, 'r', encoding='utf-8') as f:
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
        len_in = len(res_res)
        if len_in < 40:
            topk = round(len_in / 4) + 1
        elif 400 > len_in >= 40:
            topk = round(len_in / 10) + 1
        elif 2000 > len_in >= 400:
            topk = round(len_in / 20) + 1
        else:
            topk = round(len_in / 40)
        key_word = jieba.analyse.extract_tags(res_res, topK=topk, withWeight=False)
        m2=key_word
        s1_cut = m1
        s2_cut = m2

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





