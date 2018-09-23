import csv
from collections import defaultdict
import json
class reader:
    def __init__(self,lim=100):
        self.train,self.test = self._get_data(lim)
        self._print_list(self.train['0'])
        with open("train_data.json",'w') as fout:
            json.dump(self.train,fout)
        with open("test_data.json",'w') as fout:
            json.dump(self.test,fout)
    @staticmethod
    def _print_list(print_list):
        for digit in print_list:
            for row in range(28):
                for column in range(28):
                    print(digit[28*row+column],end="")
                print()
            print()

    @staticmethod
    def _get_data(lim=100):
        train = defaultdict(list)
        test = defaultdict(list)
        with open('mnist_train.csv','r') as fin:
            mnist_reader = csv.reader(fin)
            for digit in mnist_reader:
                cur_elem=[]
                for element in range(1,len(digit)):
                    if int(digit[element]) > lim:
                        cur_elem.append(1)
                    else:
                        cur_elem.append(0)
                train[digit[0]].append(cur_elem)

        with open('mnist_test.csv','r') as fin:
            mnist_reader = csv.reader(fin)
            for digit in mnist_reader:
                cur_elem=[]
                for element in range(1,len(digit)):
                    if int(digit[element]) > lim:
                        cur_elem.append(1)
                    else:
                        cur_elem.append(0)
                test[digit[0]].append(cur_elem)
        return train, test

reader(45)
