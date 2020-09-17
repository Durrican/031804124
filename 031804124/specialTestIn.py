import unittest

from 软工.specialTest import Testt


class MyTest(unittest.TestCase):

    def test_add(self):
        orig = 'sim_0.8/orig.txt'
        filepath = "sim_0.8/orig_0.8_add.txt"
        res_1 = Testt.cclear(orig, filepath)
        res_final = str(res_1)
        print("orig_0.8_add.txt 相似度")
        print(res_final)

    def test_del(self):
        print("orig_0.8_del.txt 相似度")
        orig = 'sim_0.8/orig.txt'
        filepath = "sim_0.8/orig_0.8_del.txt"
        res_1 = Testt.cclear(orig, filepath)
        res_final = str(res_1)
        print(res_final)

    def test_dis_1(self):
        print("orig_0.8_dis_1.txt 相似度")
        orig = 'sim_0.8/orig.txt'
        filepath = "sim_0.8/orig_0.8_dis_1.txt"
        res_1 = Testt.cclear(orig, filepath)
        res_final = str(res_1)
        print(res_final)

    def test_dis_3(self):
        print("orig_0.8_dis_3.txt 相似度")
        orig = 'sim_0.8/orig.txt'
        filepath = "sim_0.8/orig_0.8_dis_3.txt"
        res_1 = Testt.cclear(orig, filepath)
        res_final = str(res_1)
        print(res_final)

    def test_dis_7(self):
        print("orig_0.8_dis_7.txt 相似度")
        orig = 'sim_0.8/orig.txt'
        filepath = "sim_0.8/orig_0.8_dis_7.txt"
        res_1 = Testt.cclear(orig, filepath)
        res_final = str(res_1)
        print(res_final)

    def test_dis_10(self):
        print("orig_0.8_dis_10.txt 相似度")
        orig = 'sim_0.8/orig.txt'
        filepath = "sim_0.8/orig_0.8_dis_10.txt"
        res_1 = Testt.cclear(orig, filepath)
        res_final = str(res_1)
        print(res_final)

    def test_dis_15(self):
        print("orig_0.8_dis_15.txt 相似度")
        orig = 'sim_0.8/orig.txt'
        filepath = "sim_0.8/orig_0.8_dis_15.txt"
        res_1 = Testt.cclear(orig, filepath)
        res_final = str(res_1)
        print(res_final)

    def test_mix(self):
        print("orig_0.8_mix.txt 相似度")
        orig = 'sim_0.8/orig.txt'
        filepath = "sim_0.8/orig_0.8_mix.txt"
        res_1 = Testt.cclear(orig, filepath)
        res_final = str(res_1)
        print(res_final)

    def test_rep(self):
        print("orig_0.8_rep.txt 相似度")
        orig = 'sim_0.8/orig.txt'
        filepath = "sim_0.8/orig_0.8_rep.txt"
        res_1 = Testt.cclear(orig, filepath)
        res_final = str(res_1)
        print(res_final)
    def test_repp(self):
        print("orig_0.8_repp.txt 相似度")
        orig = 'sim_0.8/orig.txt'
        filepath = "sim_0.8/orig_0.8_repp.txt"
        res_1 = Testt.cclear(orig, filepath)
        res_final = str(res_1)
        print(res_final)


unittest.main()
