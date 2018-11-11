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
    z_int = coeff['z_int']
    slope_x = coeff['slope_x']
    slope_y = coeff['slope_y']

    # Ploting Values and Regression Line
    max_x = np.max(data['Math'].values)
    min_x = np.min(data['Math'].values) - 5

    max_y = np.max(data['Reading'].values)
    min_y = np.min(data['Reading'].values) - 5

    # Calculating line values x and y
    x = np.linspace(min_x, max_x, 1000)
    y = np.linspace(min_y, max_y, 1000)
    z = z_int + slope_x * x + slope_y * y

    # Initialize a 3d plot
    fig = plt.figure()
    ax = Axes3D(fig)

    # Plot points
    ax.scatter(data['Math'].values, data['Reading'].values, data['Writing'].values, color='#ef1234', label='Scatter Plot')
    # Plot Line
    ax.plot(x, y, z, color='#000000', label='Regression Line')

    # Label axes
    ax.set_xlabel('Math score (%)')
    ax.set_ylabel('Reading score (%)')
    ax.set_zlabel('Writing score (%)')
    plt.title("Reading and Math vs. Writing Scores Data")

    # Construct a legend
    plt.legend()

    # Render the plot
    plt.show()

def naive_bayes_heatmap():
    # Load pre-computed probabilities dictionary from JSON file
    with open('nb_probabilities.json', 'r') as fp:
        nb_probabilities = json.load(fp)

    _naive_bayes_heatmap(nb_probabilities)

def _naive_bayes_heatmap(probabilities):
        # Loop through digits
        for digit in range(10):
            # Convert dict to numpy array
            digit_prob = np.asarray(probabilities[str(digit)])
            digit_prob = np.reshape(digit_prob, (28, 28))

            # Create subplot
            plt.subplot(5, 2, digit+1)

            # Map point probabilities to a color value
            plt.imshow(digit_prob, cmap='hot', interpolation='nearest')

            # Set spacing to make the plot pretty
            plt.subplots_adjust(left=0.2, bottom=0.1, right=0.8, top=0.95, wspace=0.5, hspace=1)

            # Set a title for each subplot
            plt.title("Heatmap for the digit {}".format(digit))

        # Renders plot
        plt.show()

def k_means_clusters():
    # Load pre-computed probabilities dictionary from JSON file
    with open('kmeans_clusters.json', 'r') as fp:
        km_clusters = json.load(fp)
    _k_means_clusters(km_clusters)

def _k_means_clusters(clusters):
    class_1 = clusters['class_1']
    class_2 = clusters['class_2']

    # Plot the first class
    plt.plot(class_1[0], class_1[1], 'ro', label="Class 1")

    # Plot the second class
    plt.plot(class_2[0], class_2[1], 'go', label="Class 2")

    # Set plot title
    plt.title("K-Means Clusters")

    # Render plot
    plt.legend()
    plt.show()

linear_regression_scatter_plot()
naive_bayes_heatmap()
k_means_clusters()
