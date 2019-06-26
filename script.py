import xml.etree.ElementTree as ET
import os
from PIL import Image
def parseXML(file):
    try:
        
        tree = ET.parse(file)
        root = tree.getroot()
    

        multipleTables = list()
        for item in root.findall("./table"):
            for child in item:
                table = list()
                temp = child.attrib['points'].split(" ")
                for t in temp:
                    table.append(t.split(","))
                multipleTables.append(table)
            
        return multipleTables
    except Exception as e:
        print(e,"for",filename+fileExtension)

def cropImage(souce, filename, fileExtension, coords, destinationDir):
    count = 1
    for coord in coords:
        try:
            
            im = Image.open(source + filename + fileExtension)
            x1 = int(coord[0][0])
            y1 = int(coord[0][1])

            x2 = int(coord[2][0])
            y2 = int(coord[2][1])
            cropped  = im.crop((x1,y1,x2,y2))

            cropped.save(destinationDir + str(count)+ "_" + filename + fileExtension)
        
            count +=1
        except Exception as e:
            print(e,"for",filename + fileExtension)
    
                
imageExt = [".jpg",".png",".TIFF"] #Image formats in the dataset
source = "TRACKB1_test/" #Source Path for Directory of Images
destination = "TRACKB1_test_extracted/" #Destination of Images Cropped
files = os.listdir(source)

if os.path.exists(destination):
    print("Directory already exists. Delete and re-run")
else:
    os.mkdir(destination)
    for file in files:
        filename, fileExtension = os.path.splitext(file)
        if fileExtension in imageExt:
            index = imageExt.index(fileExtension)
            print(".",end="")
            temp = parseXML(source + filename + ".xml") # function return a list comprising
            # of tables in that one image
            cropImage(source, filename, fileExtension, temp, destination) #Crops and saves new Images
    
    print("DONE")


