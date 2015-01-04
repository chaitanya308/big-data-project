#This code is submitted by Palak Goel

import csv
import unicodedata

reader = csv.reader(open("yelp_academic_dataset_review_few.csv", "r", encoding="utf-8"))
colCount =0
my_list = []
list_row = []



with open("Restaurant_BusinessIds.txt", 'r') as f:
    my_list = [line.rstrip('\n') for line in f]    



#f2 = open('ExtractedReviews.txt', 'w+')
#f.write("test")
#f.close


  
with open("ExtractedReviews2.txt", 'w') as f2: 
 for row in reader:
    for col in row:
      colCount = colCount+1;
      list_row.append(col)
      if ((colCount == 5) and (col in my_list)):
        
        my_uni = list_row[2]
        #f2.write(my_uni)
        unicodedata.normalize('NFKD', my_uni).encode('ascii','ignore')
        print (my_uni)
        break
        
    colCount = 0;
    list_row = []


f.close
