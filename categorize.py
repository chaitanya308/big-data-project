import optparse
import numpy as np

import csv

category_dict = {
'Pakistani':'South Asian',
'Bangladeshi':'South Asian',
'Indian':'South Asian',
'Afghan':'South Asian',
'Himalayan/Nepalese':'South Asian',
'Burmese':'South Asian',
'Nightlife':'Bars & Pubs',
'Bars':'Bars & Pubs',
'Gay Bars':'Bars & Pubs',
'Tapas Bars':'Bars & Pubs',
'Music Venues':'Bars & Pubs',
'Breweries':'Bars & Pubs',
'Beer':'Bars & Pubs',
'Gastropubs':'Bars & Pubs',
'Active Life':'Bars & Pubs',
'Sushi Bars':'Bars & Pubs',
'Pubs':'Bars & Pubs',
'Dive Bars':'Bars & Pubs',
'Sports Bars':'Bars & Pubs',
'Cocktail Bars':'Bars & Pubs',
'Dance Clubs':'Bars & Pubs',
'Hookah Bars':'Bars & Pubs',
'Wine Bars':'Bars & Pubs',
'Wine & Spirits':'Bars & Pubs',
'Mexican':'Mexican',
'Tex-Mex':'Mexican',
'Fast Food': 'Fast Food',
'Buffets':'Lunch & Dinner',
'Diners':'Lunch & Dinner',
'Breakfast & Brunch':'Breakfast & Brunch',
'Modern European':'European',
'Polish':'European',
'Belgian':'European',
'German':'European',
'Portuguese':'European',
'Laotian':'European',
'Slovakian':'European',
'Italian':'European',
'Scottish':'European',
'French':'European',
'Irish':'European',
'British':'European',
'Spanish':'European',
'Shanghainese':'Asian',
'Ramen':'Asian',
'Singaporean':'Asian',
'Asian Fusion':'Asian',
'Vietnamese':'Asian',
'Thai':'Asian',
'Cantonese':'Asian',
'Mongolian':'Asian',
'Malaysian':'Asian',
'Chinese':'Asian',
'Japanese':'Asian',
'Indonesian':'Asian',
'Korean':'Asian',
'Filipino':'Asian',
'Taiwanese':'Asian',
'Szechuan':'Asian',
'Russian':'Asian',
'American Traditional':'American Traditional',
'American New':'American New',
'Ice Cream & Frozen Yogurt':'Breakfast',
'Cafes':'Breakfast',
'Donuts':'Breakfast',
'Juice Bars & Smoothies':'Breakfast',
'Coffee & Tea':'Breakfast',
'Creperies':'Breakfast',
'Cheesesteaks':'Breakfast',
'Bakeries':'Breakfast',
'Desserts':'Breakfast',
'Patisserie/Cake Shop':'Breakfast',
'Delis':'Breakfast',
'Bagels':'Breakfast',
'Sandwiches':'Fast Food',
'Salad':'Fast Food',
'Chicken Wings':'Fast Food',
'Hot Dogs':'Fast Food',
'Steakhouses':'Fast Food',
'Burgers':'Burgers',
'Pizza':'Pizza',
'Barbeque':'Barbeque',
'Mediterranean':'Mediterranean',
'Persian/Iranian':'Mediterranean',
'Middle Eastern':'Mediterranean',
'Greek':'Mediterranean',
'Lebanese':'Mediterranean',
'Turkish':'Mediterranean',
'Arabian':'Mediterranean',
'Moroccan':'Mediterranean',
'Ethiopian':'Mediterranean',
'African':'Mediterranean',
'Brazilian':'Latin American',
'Colombian':'Latin American',
'Venezuelan':'Latin American',
'Latin American':'Latin American',
'Argentine':'Latin American',
'Peruvian':'Latin American',
'Caribbean':'Latin American',
'Cuban':'Latin American',
'Hawaiian':'Hawaiian'
}

ignored_tags_file = "lda_ml/ignored_tags.txt"

# Restaurants that appear in the top results that are strongly associated with a topic are passed to this script, and the script
# generates a categorization of those restaurants based on the tags associated with them. The categorization details and further
# analysed and a heatmap is generated showing restaurants and topics association.
def main():
    parser = optparse.OptionParser()
    parser.add_option("-f", dest="restaurants_file", help="filename that contains information of restaurants, each in one line.")
    
    (options, args) = parser.parse_args()

    # Check if the filename of the restaurants is provided.
    if not (options.restaurants_file):
        parser.error("Please provide name of the restaurants file through -f option")
  
    fp = open(ignored_tags_file, 'w') 
    dict = {}
    wider_dict = {}
    with open(options.restaurants_file, 'r') as rfp:
        reader = csv.reader(rfp, delimiter=';')

        # read each row from the file
        # each row/line is in the format business_id;name;categories_list;review_count;stars
        for row in reader:
            category_list = []
            categories = row[2].split(",")
            
            for category in categories:
                key = category.strip()
                if key in dict:
                    dict[key].append(row[0])
                else:
                    dict[key] = [row[0]]
            
                if key in category_dict:
                    k = category_dict[key]
                    if k not in category_list:                
                        if k in wider_dict:
                            wider_dict[k] += 1
                        else:
                            wider_dict[k] = 1
                        category_list.append(k)

                # some un-important category tags are ignored. Capture them in a file for reference.
                # Completely ignore the tag 'Restaurants' as all of the restuarants have that tag.
                elif key != "Restaurants":
                    fp.write(key + "\n")

        fp.close()
 
        # Details of these categorization are used for topic association analysis and heatmap generation.
       
        print("--------- Granular Categorization----------")
        # Traverse the category dictionary and print the counts
        for key in dict:
            print("{}:{}".format(key, len(dict[key])))           

        print("----------- Broad Categorization--------")
        for key in wider_dict:
            print("{}:{}".format(key, wider_dict[key]))               
     
if __name__ == '__main__':
    main()
