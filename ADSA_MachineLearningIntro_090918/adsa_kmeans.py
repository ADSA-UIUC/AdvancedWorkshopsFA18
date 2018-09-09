# Inbuilt packagges
import json
import random
import sys

import matplotlib.pyplot as plt

# Own packages
from adsa_data_gen import data_gen


class k_means():

    def __init__(self, path):
        with open(path) as f:
            d = json.load(f)
        self.data_gen = data_gen(dimensions=2, kwargs=d)
        self.test, self.train = self.data_gen.create_data()
        self.x = self.train[0]
        self.y = self.train[1]
        plt.plot(self.x, self.y, 'ro')
        plt.show()
        self.x_start1 = random.choice(self.x)
        self.y_start1 = random.choice(self.y)
        self.x_start2 = random.choice(self.x)
        self.y_start2 = random.choice(self.y)
        self.cur_class1 = [[], []]
        self.cur_class2 = [[], []]

    def classify(self):
        del self.cur_class1[0][:]
        del self.cur_class1[1][:]
        del self.cur_class2[0][:]
        del self.cur_class2[1][:]
        for i in range(len(self.x)):
            cl = self._calculate_distance(self.x[i], self.y[i])
            if cl == 1:
                self.cur_class1[0].append(self.x[i])
                self.cur_class1[1].append(self.y[i])
            else:
                self.cur_class2[0].append(self.x[i])
                self.cur_class2[1].append(self.y[i])
        self.change_centres()

    def change_centres(self):
        self.x_start1 = sum(self.cur_class1[0])/len(self.cur_class1[0])
        self.x_start2 = sum(self.cur_class2[0])/len(self.cur_class2[0])
        self.y_start1 = sum(self.cur_class1[1])/len(self.cur_class1[1])
        self.y_start2 = sum(self.cur_class2[1])/len(self.cur_class2[1])

    def run(self, k):
        for i in range(k):
            self.classify()
            print(len(self.cur_class1[0]))
            print(len(self.cur_class2[0]))

    def _calculate_distance(self, x, y):
        dist1 = (self.x_start1 - x)**2 + (self.y_start1 - y)**2
        dist2 = (self.x_start2 - x)**2 + (self.y_start2 - y)**2
        if dist1 > dist2:
            return 1
        else:
            return 2


def main(path):
    kmeans = k_means(path=path)
    kmeans.run(100)
    plt.plot(kmeans.cur_class1[0], kmeans.cur_class1[1], 'ro')
    plt.plot(kmeans.cur_class2[0], kmeans.cur_class2[1], 'go')
    plt.show()


if __name__ == "__main__":
    sys.exit(main(path="./data_sets/data_set.json"))
