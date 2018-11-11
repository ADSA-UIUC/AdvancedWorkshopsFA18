import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd

def linear_regression_scatter_plot():
    # Load pre-computed df from csv file
    reg_data = pd.read_csv('lin_reg_data.csv', sep=',')
    with open('lin_reg_coeff.json', 'r') as fp:
        reg_coeff = json.load(fp)

    _linear_regression_scatter_plot(reg_data, reg_coeff)

def _linear_regression_scatter_plot(data, coeff):
    pass

def naive_bayes_heatmap():
    # Load pre-computed probabilities dictionary from JSON file
    with open('nb_probabilities.json', 'r') as fp:
        nb_probabilities = json.load(fp)

    _naive_bayes_heatmap(nb_probabilities)

def _naive_bayes_heatmap(probabilities):
    pass

def k_means_clusters():
    # Load pre-computed probabilities dictionary from JSON file
    with open('kmeans_clusters.json', 'r') as fp:
        km_clusters = json.load(fp)
    _k_means_clusters(km_clusters)

def _k_means_clusters(clusters):
    pass

linear_regression_scatter_plot()
naive_bayes_heatmap()
k_means_clusters()
