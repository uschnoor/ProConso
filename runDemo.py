from plotter import plotter
import sys
from Jsonreader import Jsonreader
from Csvreader import Csvreader


def plotWithGroups(plotting,apartmentdict, xaxis, yaxis, group, IsGroupBuildingdict, selectbypair  ):

    listx=[]
    listy=[]
    listz=[]

    for a in apartmentdict:
        
        ap = apartmentdict[a]
        buildingnumber = ap["building"]
        buildingdict = Jsonreader(buildingnumber).GetBuildingDict()
        if ap[xaxis] == 0:
            continue
        if a=="1021896":
            continue
        if not ap[selectbypair[0]] == selectbypair[1]:
            continue

        listx.append(ap[xaxis])
        listy.append(ap[yaxis])
        if IsGroupBuildingdict:
            listz.append(buildingdict[group])
        else:
            listz.append(group+" "+ap[group])
    title=selectbypair[1]
    xtitle=xaxis
    plotting.pandaplot_3groups(listx, listy, listz,title, xtitle)
    return


def main(*args):
    
    #buildingreader = Jsonreader("Conso_appartements.csv")
    apartmentreader = Csvreader("Conso_appartements.csv")
    apartmentdict = apartmentreader.dictOfAllApartments()

    print apartmentdict


    
    
    xpoints = []
    ypoints = []
    for a in apartmentdict:
        ap = apartmentdict[a]
        buildingnumber = ap["building"]
        buildingdict = Jsonreader(buildingnumber).GetBuildingDict()
        print buildingdict
        aptype = "secondaire"
        if ap["type"] == aptype:
            continue
        #xpoints.append(ap["rooms"])
        xpoints.append(buildingdict["Annee"])
        ypoints.append(ap["conso_2017"])
    plotting  = plotter()
    plotting.scatterplot_onevariable(xpoints,ypoints, aptype)
#

    plotWithGroups(plotting,apartmentdict, "rooms", "conso_2017", "EfficaciteGlobale", True, ["type", "principale"] )
    plotWithGroups(plotting,apartmentdict, "rooms", "conso_2017", "building", False , ["type", "principale"] )
    plotWithGroups(plotting,apartmentdict, "rooms", "conso_2017", "Annee", True, ["type", "principale"] )


if __name__ == "__main__":
    main(*sys.argv)
