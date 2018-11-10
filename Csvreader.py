import csv

class Csvreader:
    def __init__(self,csvfile):
        self.csvfile = csvfile

    def reader(self):
        csvfileopen = open(self.csvfile,'rb')
        reader = csv.reader(csvfileopen)
        return reader
    def dictOfAllApartments(self):
        dictOfFlats = {}
        read = self.reader()
        batiment = 0
        for line in read:
            if line[0].startswith("#"): continue
            if line[0].startswith("BATIMENT"):
                batiment = line[0].split(" ")[1]
                continue
            print line[0], line[1]
            if not len(line)  ==9:
                print("line too short")
                continue
            if line[1].startswith("Blanchisserie"): continue
            apartment_ise = line[2] #line[1].split(" ")[1]
            dictOfFlats[apartment_ise] = {}
            dictOfFlats[apartment_ise]["building"] = batiment
            dictOfFlats[apartment_ise]["ISE"] = line[2]
            dictOfFlats[apartment_ise]["number"] = line[1].split(" ")[1]
            dictOfFlats[apartment_ise]["conso_2014"] = float(line[3].replace(",",""))
            dictOfFlats[apartment_ise]["conso_2015"] = float(line[4].replace(",",""))
            dictOfFlats[apartment_ise]["conso_2016"] = float(line[5].replace(",",""))
            dictOfFlats[apartment_ise]["conso_2017"] = float(line[6].replace(",",""))

            rooms = line[7]
            if line[7].startswith("Studio"):
                rooms=1
            elif line[7].startswith("Aucun"):
                rooms = 0
            else:
                rooms=line[7].split(" ")[0]
            type = ""
            if len(line[8].split(" ") )== 2:
                if line[8].split(" ")[1] == "principale":
                    type = "principale"
                elif line[8].split(" ")[1] == "secondaire":
                    type = "secondaire"
                
            dictOfFlats[apartment_ise]["type"] = type

            dictOfFlats[apartment_ise]["rooms"] = rooms

        return dictOfFlats
