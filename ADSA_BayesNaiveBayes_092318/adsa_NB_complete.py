# In built libraries
import json
import heapq
import math
import time


# Downloaded libraries
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt


class NB:

    def __init__(self, train_path, test_path, k_factor=0.1):

        self.corr = 0
        self.wrong = 0
        self.probabilities = {
            str(k): [0 for j in range(28*28)] for k in range(10)}
        self.priors = []
        self.conf_matrix = [[0 for i in range(10)] for j in range(10)]

        start = time.time()
        with open(train_path, 'r') as fin:
            self.train_data = json.load(fin)
        with open(test_path, 'r') as fin:
            self.test_data = json.load(fin)
        print("Time taken to load the data : {}".format(time.time()-start))

        start = time.time()
        self._calculate_probabilities(self.train_data, k_factor)
        print("Time taken to train: {}".format(time.time()-start))

        start = time.time()
        self.classify(self.test_data)
        print("Time taken to classify full test data set is {}".format(
            time.time()-start))

        print(DataFrame(self.conf_matrix))
        print("Accuracy is {}".format((self.corr)/(self.corr+self.wrong)))
        self._print_heatmaps()

    def _calculate_probabilities(self, train_data, k):

        total = 0
        for i in train_data.keys():
            total += len(train_data[i])
        self.priors = [len(train_data[i])/total for i in train_data.keys()]
        for digit in range(10):
            digit_list = train_data[str(digit)]
            for cur_digit in digit_list:
                for cur_element in range(len(cur_digit)):
                    self.probabilities[str(
                        digit)][cur_element] += cur_digit[cur_element]
            for i in range(len(self.probabilities[str(digit)])):
                p = (self.probabilities[str(digit)]
                     [i]+k)/(len(digit_list)+(k*2))
                if p == 0 or p == 1:
                    raise Exception("WTF")
                self.probabilities[str(digit)][i] = p

    def _print_heatmaps(self):
        for digit in range(10):
            cur_p = np.asarray(self.probabilities[str(digit)])
            cur_p = np.reshape(cur_p, (28, 28))
            plt.subplot(5, 2, digit+1)
            plt.imshow(cur_p, cmap='hot', interpolation='nearest')
            plt.title("Heatmap for the digit {}".format(digit))
        plt.show()

    def classify(self, data):
        for key, value in data.items():
            for digit in value:
                res = self._classify(digit)
                self.conf_matrix[int(key)][res] += 1
                if(int(key) == res):
                    self.corr += 1
                else:
                    self.wrong += 1

    def _classify(self, arr):
        max_val = -9999999999
        for digit in range(10):
            digit_probability = self.probabilities[str(digit)]
            prob = self._get_cur_probability(
                cur_arr=arr, prob_arr=digit_probability, digit=digit)
            if prob > max_val:
                max_val = prob
                res = digit
        return res

    def _get_cur_probability(self, cur_arr, prob_arr, digit):
        prob = math.log(self.priors[digit])
        for i in range(28):
            for j in range(28):
                if(cur_arr[i*28+j] == 0):
                    prob += math.log(1-prob_arr[i*28+j])
                else:
                    prob += math.log(prob_arr[i*28+j])
        return prob


NB("./train_data.json", "./test_data.json")
