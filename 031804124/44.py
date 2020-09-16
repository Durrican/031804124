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

def cut(s1):
    s1 = readLines(s1)
    text_list = re.findall(".{20}", s1)
    new_text = " ".join(text_list)
    l = new_text.split()
    lenm = round(len(s1) / 20)
    return l,lenm


def coscompare(q1,q2):
    s1_cut=jieba.lcut(q1)
    s2_cut=jieba.lcut(q2)
    word_set=set(s1_cut).union(set(s2_cut))
    word_dict=dict()
    i=0
    for word in word_set:
        word_dict[word]=i
        i+=1


    s1_code = [word_dict[word] for word in s1_cut]
    s2_code = [word_dict[word] for word in s2_cut]

    s1_code=[0]*len(word_dict)
    s2_code=[0]*len(word_dict)

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
files2 = r'C:\Users\Administrator\Desktop\软工\1\sim_0.8\orig_0.8_rep.txt'
l1,len1=cut(files1)
l2,len2=cut(files2)
i=0
ans=[]
for i in range(0,min(len1,len2)-1):
    q1 = l1[i]
    q2 = l2[i]
    ans.append(coscompare(q1,q2))
    i+=1

j=0
final=0
for j in range(len(ans)):
    final+=ans[j]

finalres=round(final/len(ans),2)
print(l1)