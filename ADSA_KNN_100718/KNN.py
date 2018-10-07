import json
import numpy as np


class KNN:
    """

    """

    def __init__(self):
        with open("train_data.json") as fin:
            self.train_data = json.load(fin)
        with open("test_data.json") as fin:
            self.test_data = json.load(fin)
        self.traindata = []
        self.testdata = []
        self.trainlabels = []
        self.testlaels = []

    def setup_data(self):

        for i in self.train_data:
            cur_data = self.train_data[i]
            for j in cur_data:
                self.traindata.append(np.asarray(j))
                self.trainlabels.append(i)

        for i in self.test_data:
            cur_data = self.test_data[i]
            for j in cur_data:
                self.testdata.append(np.asarray(j))
                self.testlabels.append(i)

    def classify():
    """
    Iterate through all points and call classify_helper on it
    """

    def _classify_helper(self, k, vector):
    """
    Take in a single datapoint andn
    return it's class
    """
        vector = np.asarray(vector)
        for data_point in self.traindata:
            dist = np.sqrt
