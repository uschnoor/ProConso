from plotter import plotter
import sys
from Jsonreader import Jsonreader
from Csvreader import Csvreader



def main(*args):
    
    #buildingreader = Jsonreader("Conso_appartements.csv")
    apartmentreader = Csvreader("Conso_appartements.csv")
    apartmentdict = apartmentreader.dictOfAllApartments()

    print apartmentdict
    
    
    xpoints = []
    ypoints = []
    for a in apartmentdict:
        ap = apartmentdict[a]
        if ap["type"] == "secondaire":
            continue
        xpoints.append(ap["rooms"])
        ypoints.append(ap["conso_2017"])
    plotting  = plotter(xpoints,ypoints)
    plotting.scatterplot()

    


    
if __name__ == "__main__":
    main(*sys.argv)
