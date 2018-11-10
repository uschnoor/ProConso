import numpy as np
import matplotlib.pyplot as plt



class plotter:
    def __init__(self,xpoints,ypoints):
        self.xpoints = np.array(xpoints)
        self.ypoints = np.array(ypoints)


    def scatterplot(self):
        plt.scatter(self.xpoints, self.ypoints)
        plt.title('Scatter plot pythonspot.com')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
