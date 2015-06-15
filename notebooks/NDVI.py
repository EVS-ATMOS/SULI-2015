# Michelle attempting to write a Python script
# NDVI measurements

## Defining Variables
##Rvis = PARout/PARin
##
##Visin = 0.45 * Rg
##
##NIRin = 0.55 * Rg
##
##Visout = Rvis * Visin
##
##NIRout = SOLRout - Visout
##
##RNIR = NIRout / NIRin

# NDVI Measurements

a = int(38.15) # 760 nm
b = int(39.14) # 810 nm
c = int(4.71) # 660 nm
d = int(10.40) # 710nm

## Gathering values for each nm 

a = input("Enter the 760 nm measurement: ")
print (("This is the 760 nm measurement:"),(a))
print ("----------------------------------\n")

b = input("Enter the 810 nm measurement: ")
print (("This is the 810 nm measurement:"),(b))
print ("----------------------------------\n")

c = input("Enter the 660 nm measurement: ")
print (("This is the 660 nm measurement:"),(c))
print ("----------------------------------\n")

d = input("Enter the 710 nm measurement: ")
print (("This is the 710 nm measurement:"),(d))
print ("----------------------------------\n")

## Computing NIR, Red, and NDVI

NIR = float(a) + float(b)
Red = float(c) + float(d)
NDVI = (NIR - Red) / (NIR + Red)

NIR = round(NIR, 2)
Red = round(Red, 2)
NDVI = round(NDVI, 2)

# Writing to a text file

dataset = [a, b, c, d, NIR, Red]
NDVIFile = open('NDVIFile.txt', 'a')
NDVIFile.write("In order: 760 nm, 810 nm, 660 nm, 710 nm, NIR, Red, NDVI\n")
NDVIFile.write("VISin, NIRin, Rvis, VISout, NIRout, rNIR, Second NDVI\n")
for i in dataset:
    NDVIFile.write("%s\n" % i)
NDVIFile.write(str(NDVI))
NDVIFile.write("\n")

## SECOND NDVI CALCULATION ##

# VISin
# NIRin

solr = input("Enter SOLR:\n")
VISin = float(0.45) * float(solr)
NIRin = float(0.55) * float(solr)
VISin = round(VISin, 2)
NIRin = round(NIRin, 2)

NDVIFile.write(str(VISin))
NDVIFile.write("\n")
NDVIFile.write(str(NIRin))
NDVIFile.write("\n")

# Rvis

PARout = input("Enter PARout:\n")
PARin = input("Enter PARin:\n")
Rvis = float(PARout) / float(PARin)
Rvis = round(Rvis, 2)

NDVIFile.write(str(Rvis))
NDVIFile.write("\n")

# VISout

VISout = float(Rvis) * float(VISin)
VISout = round(VISout, 2)

NDVIFile.write(str(VISout))
NDVIFile.write("\n")

# NIRout

solrOut = input("Enter SOLRout:\n")
NIRout = float(solrOut) - float(VISout)
NIRout = round(NIRout, 2)

NDVIFile.write(str(NIRout))
NDVIFile.write("\n")

# rNIR

rNIR = float(NIRout) / float(NIRin)
rNIR = round(rNIR, 2)

NDVIFile.write(str(rNIR))
NDVIFile.write("\n")

# Finally gets the damn NDVI

NDVI2 = (float(rNIR) - float(Rvis)) / (float(rNIR) + float(Rvis))
NDVI2 = round(NDVI2, 2)

NDVIFile.write(str(NDVI2))
NDVIFile.write("\n-------------------\n")
NDVIFile.close()

print (("NIR:"),(NIR))
print (("Red:"),(Red))
print (("NDVI:"),(NDVI))
print ("VISin:",(VISin))
print ("NIRin:",(NIRin))
print ("Rvis:",(Rvis))
print ("VISout:",(VISout))
print ("NIRout:",(NIRout))
print ("rNIR:",(rNIR))
print ("Second NDVI:",(NDVI2))










 
