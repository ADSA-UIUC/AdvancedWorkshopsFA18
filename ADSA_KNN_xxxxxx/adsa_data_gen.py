import numpy as np
import json


class data_gen:
    def __init__(self, dimensions=2, kwargs=None):
        """
            KWargs is details about classes needed
            format:
            {
                "ClassName":{
                                "Centres": Array of floats
                                "BoundDistance": float,
                                "Number": int
                            }
                ...
            }
        """
        self.dimensions = dimensions
        self.kwargs = kwargs

    def create_data(self):
        """
        Function to create the data, returns tuple
	At index 0 there is a dictionary of format:
        {
            "[point1,point2...]": ClassName
            ...
        }
	At index 1 there is a python array of np arrays
	
        """
        ret = {}
        test_data = [[] for i in range(self.dimensions)]
        for key, data in self.kwargs.items():
            if len(data["Centres"]) == self.dimensions:
                ret[key] = self.create_class(data)
	final_ret = {}
        for key in ret.keys():
		val = ret[key]
		for i in range(len(val[0])):
			cur_arr=[]
			for j in range(self.dimensions):
				cur_arr.append(val[j][i])
			final_ret[tuple(cur_arr)]=key
	for key, value in ret.items():
            for i in range(self.dimensions):
                test_data[i].extend(value[i])
        return final_ret,test_data

    def create_class(self, properties):
        """Helper to create classes using np"""
        data = []
        bounddistance = properties["BoundDistance"]
        size = properties["Number"]
        for i in range(self.dimensions):
            cur_centre = properties["Centres"][i]
            data.append(np.random.uniform(
                low=(cur_centre - bounddistance),
                high=(cur_centre + bounddistance),
                size=size
            ))
        return data


def main():
    with open("./data_sets/data_set.json") as f:
        data = json.load(f)
    d = data_gen(dimensions=3, kwargs=data)
    a = d.create_data()
    print(a)
    with open("./data_sets/data_set.json") as f:
        data = json.load(f)

if __name__ == "__main__":
    main()
