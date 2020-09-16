import jieba
import math
import re

def coscompare(q1,q2):
    s1_cut=jieba.lcut(q1)
    s2_cut=jieba.lcut(q2)
    word_set=set(s1_cut).union(set(s2_cut))
    word_dict=dict()
    i=0
    for word in word_set:
        word_dict[word]=i
        i+=1

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
    res=round((float(sum+1)/(math.sqrt(sq1+1)*math.sqrt(sq2+1))),2)
    return res


def clear(files1):
    lines=[]
    with open(files1, 'r', encoding='utf_8') as f:
        lines = f.readlines()
        res = []
        for line in lines:
            a = line.split()
            a1 = ''.join(a)
            res.append(a1)
            res1 = ''.join(res)
    return res1



files1 = r'C:\Users\Administrator\Desktop\软工\1\sim_0.8\orig.txt'
files2 = r'C:\Users\Administrator\Desktop\软工\1\sim_0.8\orig_0.8_mix.txt'

pattern = r'。|，|？|！|：'
res1=clear(files1)
res2=clear(files2)
result_list1 = re.split(pattern,res1)
result_list2 = re.split(pattern,res2)
len1=len(result_list1)
len2=len(result_list2)
i=0
j=0
ans=[]
for i,j in zip(range(0,min(len1,len2)-3),range(0,min(len1,len2)-3)):
    q1 = result_list1[i]
    q2 = result_list2[j]
    q3=result_list2[j-1]
    q5=result_list2[j-2]
    q7=result_list2[j-3]
    z2=coscompare(q1,q2)
    z3=coscompare(q1,q3)
    z5=coscompare(q1,q5)
    z7=coscompare(q1,q7)
    if z2>z3  and z2>z5  and z2 > z7:
        i+=1
        j+=1
        ans.append(z2)
        print(q1,q2)
    elif z3>z2  and z3 > z5 and z3>z7 :
        j=j-1
    elif z5 > z2 and z5 > z3   and z5>z7:
        j=j-2
    elif z7 > z2 and z7 > z3  and z7 > z5:
        j=j-3
    i=i-1
    j=j-1

j=0
final=0
for j in range(len(ans)):
    final+=ans[j]


finalres=round(final/len(ans),2)
print(finalres)