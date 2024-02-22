import numpy as np
import matplotlib.pyplot as plt
import sys
import csv


class Plotter:

    def figureCreator(self, skeleton):
        # Convert the list of strings to a list of floats
        points = [list(map(float, landmark.split(','))) for landmark in skeleton]
        return np.array(points)

    def frontal(self, figure):
        x = figure[:, 0]
        y = figure[:, 1]

        fig = plt.figure(figsize=(10, 5))
        ax = fig.add_subplot(131)
        ax.scatter(x, y)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Frontal Projection (XY plane)')

        plt.tight_layout()
        plt.show()

    def lateral(self, figure):
        x = figure[:, 0]
        z = figure[:, 2]

        fig = plt.figure(figsize=(10, 5))
        ax = fig.add_subplot(132)
        ax.scatter(x, z)
        ax.set_xlabel('X')
        ax.set_ylabel('Z')
        ax.set_title('Lateral Projection (XZ plane)')

        plt.tight_layout()
        plt.show()

    def topdown(self, figure):
        y = figure[:, 1]
        z = figure[:, 2]

        fig = plt.figure(figsize=(10, 5))
        ax = fig.add_subplot(133)
        ax.scatter(y, z)
        ax.set_xlabel('Y')
        ax.set_ylabel('Z')
        ax.set_title('Top-down Projection (YZ plane)')

        plt.tight_layout()
        plt.show()


if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Usage: dataAnalizer <filename>")

    filename = sys.argv[1]
    if filename.split('.')[-1] != 'csv':
        print('Wrong file type. Must be csv.')

    show = Plotter()

    with open(sys.argv[1], newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            skely = show.figureCreator(row)
            show.lateral(skely)

            input("Press Enter to continue...")

