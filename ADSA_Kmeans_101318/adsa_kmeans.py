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
        # RANDOMLY SELECT STARTING POINTS
        self.x_start1 =
        self.y_start1 =
        self.x_start2 =
        self.y_start2 =
        self.cur_class1 = [[], []]
        self.cur_class2 = [[], []]

    def classify(self):
        """
        Call the helper _classify function on all points and store them
        in the respective array according to what it is classified as
        """

    def change_centres(self):
        """
        After each iteration the cluster center changes
        Calculate the new cluster centers and store them in the
        class' member variables
        """
        pass

    def run(self, k):
        """
        Call classify to complete the class
        """
        pass

    def _classify(self, x, y):
        """
        In this function you should return which
        class will the point (x,y) be classified as
        """
        pass


def main(path, k=10):
    kmeans = k_means(path=path)
    kmeans.run(k)
    plt.plot(kmeans.cur_class1[0], kmeans.cur_class1[1], 'ro')
    plt.plot(kmeans.cur_class2[0], kmeans.cur_class2[1], 'go')
    plt.show()


if __name__ == "__main__":
    sys.exit(main(path="./data_sets/data_set.json", k=100))
