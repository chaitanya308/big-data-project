# This code is submitted by Palak Goel

import csv
reader = csv.reader(open("yelp_academic_dataset_business.csv", "r"))
colCount =0
f = open('Restaurant_BusinessIds.txt', 'w')

for row in reader:
    for col in row:
      colCount = colCount+1;
      if ((colCount == 10) and (col.find("Restaurant") == -1)):
        break;
      else:
        if (colCount == 17):
           print (col)
           f.write(col)
           f.write("\n")
           break;
    colCount = 0
