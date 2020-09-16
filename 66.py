from difflib import SequenceMatcher
import jieba
import math
import re


def readLines(filepath):
    lines = []
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        lines1 = ''.join(lines)
        s = lines1
        punc = '~`!#$%^&*()_+-=|\';":/.,?><~·！@#￥%……&*（）——+-=“：’；、。，？》《{}“”'
        s = re.sub(r"[%s]+" % punc, "", s)
        lines = s
        res = []
        for line in lines:
            a = line.split()
            a1 = ''.join(a)
            res.append(a1)
            res1 = ''.join(res)
    return res1

def coscompare(file1,file2):
    s1=readLines(file1)
    s2=readLines(file2)
    s1_cut=jieba.lcut(s1)
    s2_cut=jieba.lcut(s2)
    word_set=set(s1_cut).union((set(s2_cut)))
    word_dict=dict()
    i=0
    for word in word_set:
        word_dict[word]=i
        i+=1

    len1=max(len(s1_cut),len(s2_cut))
    s1_code=[1]*len1
    s2_code=[1]*len1


    for word in s1_cut:
        s1_code[word_dict[word]]+=1

    for word in s2_cut:
        s2_code[word_dict[word]]+=1

    sum=0
    sq1=0
    sq2=0
    for i in range(len(s2_code)):
        sum += s1_code[i] * s2_code[i]
        sq1 += pow(s1_code[i], 2)
        sq2 += pow(s2_code[i], 2)
    res=round((float(sum)/(math.sqrt(sq1)*math.sqrt(sq2))),2)
    return res

files1 = r'C:\Users\Administrator\Desktop\软工\1\sim_0.8\orig.txt'
files2 = r'C:\Users\Administrator\Desktop\软工\1\sim_0.8\orig_0.8_mix.txt'
bb = coscompare(files1,files2)
print(bb)