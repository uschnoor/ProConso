from plotter import plotter
import sys

def main(*args):
    plotting  = plotter([1,2],[1,2])
    plotting.scatterplot()

    


    
if __name__ == "__main__":
    main(*sys.argv)
