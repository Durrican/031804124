import jieba
import math
s1 = '这只皮靴号码大了。那只号码合适'
s1_cut = jieba.lcut(s1)
s2 = '这只皮靴号码不小，那只更合适'
s2_cut = jieba.lcut(s2)
print(s1_cut)
print(s2_cut)
word_set=set(s1_cut).union(set(s2_cut))
print(word_set)

word_dict=dict()
i=0
for word in word_set:
    word_dict[word]=i
    i+=1
print(word_dict)



s1_cut_code = [0]*len(word_dict)
print(s1_cut_code)
for word in s1_cut:
    s1_cut_code[word_dict[word]]+=1
print(s1_cut_code)

s2_cut_code=[0]*len(word_dict)
for word in s2_cut:
    s2_cut_code[word_dict[word]]+=1
print(s2_cut_code)

sum=0
sq1=0
sq2=0

for i in range(len(s1_cut_code)):
    sum+=s1_cut_code[i]*s2_cut_code[i]
    sq1+=pow(s1_cut_code[i],2)
    sq2+=pow(s2_cut_code[i],2)
print(sum)
print(sq1)
print(sq2)
result=round(float(sum)/(math.sqrt(sq1)*math.sqrt(sq2)),2)

print(result)