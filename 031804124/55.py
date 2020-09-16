import os
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


def compare(file1, file2):
    lines1 = readLines(file1)
    lines2 = readLines(file2)

    count = 0.
    for line in lines1:
        if lines2.count(line) > 0:
            count += 1
    return count / max(len(lines1), len(lines2))


path = r"C:\Users\Administrator\Desktop\软工\1\sim_0.8"  # 输入路径，根据实际情况决定。
dirs = os.listdir(path)
files = []
error_files = []
for file in dirs:
    files.append(os.path.join(path, file))

for i in range(len(files)):
    for j in range(i + 1, len(files)):
        try:
            degree = compare(files[i], files[j])
            if degree > 0.7:
                print("{}和{}的作业相似度为：{:.2%}".format(files[i].split(" ")[0], files[j].split(" ")[0], degree).replace(
                    "第二次作业\\", ""))
        except Exception as e:
            if error_files.count(j) == 0:
                error_files.append(j)
            continue