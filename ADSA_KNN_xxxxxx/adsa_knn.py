import json
import sys

import matplotlib.pyplot as plt

from adsa_data_gen import data_gen
class KNN():
	def __init__(self,path):
		with open(path) as f:
			d = json.load(f)
		self.data_gen = data_gen(dimensions=3, kwargs=d)
		self.test_dict, self.train = self.data_gen.create_data()

	def _get_dist(self,)
def main(path):
	knn = KNN(path=path)

	
if __name__ == "__main__":
    sys.exit(main(path="./data_sets/data_set.json"))
