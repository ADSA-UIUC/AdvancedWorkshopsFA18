# In built libraries
import json
import math
import time


# Downloaded libraries
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt


class NB:

    def __init__(self, train_path, test_path, k_factor=0.1):

        # Intitialize all required variables
        self.corr = 0
        self.wrong = 0
        self.probabilities = {
            str(k): [0 for j in range(28*28)] for k in range(10)}
        self.priors = []
        self.conf_matrix = [[0 for i in range(10)] for j in range(10)]

        # Load all data from JSON
        start = time.time()
        with open(train_path, 'r') as fin:
            self.train_data = json.load(fin)
        with open(test_path, 'r') as fin:
            self.test_data = json.load(fin)
        print("Time taken to load the data : {}".format(time.time()-start))

        # Train the model by calculating the probabilities P(xi|y)
        start = time.time()
        self._calculate_probabilities(self.train_data, k_factor)
        print("Time taken to train: {}".format(time.time()-start))

        # Classify them by doing
        # argmax_over_y (ln prior + sum_over_all_x(ln(p(x|y))))
        start = time.time()
        self.classify(self.test_data)
        print("Time taken to classify full test data set is {}".format(
            time.time()-start))

        # Print confusion matrix and the heatmaps
        print(DataFrame(self.conf_matrix))
        print("Accuracy is {}".format((self.corr)/(self.corr+self.wrong)))
        self._print_heatmaps()

    def _calculate_probabilities(self, train_data, k):
        """
        To do:
        Here you have to calculate the probability
        P(x|y)
        for all x (0,0)->(28,28)
        for all y 1->10
        train_data is a dictionary where the key is the digit (char)
        and the value is an array of feature vectors
        where each feature vector is of size 28*28
        """
        # Put your code here

    def _print_heatmaps(self):
        for digit in range(10):
            cur_p = np.asarray(self.probabilities[str(digit)])
            cur_p = np.reshape(cur_p, (28, 28))
            plt.subplot(5, 2, digit+1)
            plt.imshow(cur_p, cmap='hot', interpolation='nearest')
            plt.title("Heatmap for the digit {}".format(digit))
        plt.show()

    def classify(self, data):
        # Loop through the dictionary with all test samples
        for key, value in data.items():
            # Loop through all samples for current class
            for digit in value:
                # Call helper classify function
                res = self._classify(digit)
                self.conf_matrix[int(key)][res] += 1
                if(int(key) == res):
                    self.corr += 1
                else:
                    self.wrong += 1

    def _classify(self, arr):
        """
        To do:
        Given a digit sample in arr use the helper
        function _get_cur_arg_value() to get the
        value of the argument (ln prior + sum_over_all_x(ln(p(x|y))))
        and classify to whatever y makes this value max
        and return that y
        MAKE SURE TO UPDATE Conf Matrix and self.corr and self.wrong
        arr is a feature vector of size 28*28
        """
        # Put your code here
        pass

    def _get_cur_arg_value(self, cur_arr, prob_arr, digit):
        """
        To do:
        Given a sample a probability array
        calculate the value
        ln prior + sum_over_all_x(ln(p(x|y))
        and return this
        cur_arr is a feature vector of size 28*28
        prob_arr is array of probabilities you are checking over
        this is alaso of size 28*28
        digit is the digit you are classifying it as
        """
        # Put your code here
        pass


NB("./train_data.json", "./test_data.json")
