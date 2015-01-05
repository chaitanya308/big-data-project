big-data-project
========================

Project: Analysis of yelp dataset through topic extraction from user reviews.

Programming Environment(Linux):
- Download Anaconda 3.4 with Python 3.4.1 from http://continuum.io/downloads
- Setup anaconda environment by following the instructions at http://docs.continuum.io/anaconda/install.html#linux-install
- Activate default environment of Anaconda by running the command 'source $HOME/anaconda3/bin/activate ~/anaconda3'
- Install gensim by following the instructions at http://radimrehurek.com/gensim/install.htmlInstall gensim
    - gensim pre-requisites numpy and scipy also needs to be installed. Use 'pip install pkg_name' to install the dependency packages
- NLTK resources need to be downloaded while running the lda_ml.py program
    - open interactive python window ($ipython)
    - type 'import nltk'
    - type 'nltk.download()'
    - Select the resuorce in the window, and install them

For our project, the environment is setup on CentOs 6.0 and VIM editor is used for source code editing.

Input Dataset:
Yelp challenge dataset available at https://www.yelp.com/dataset_challenge/dataset should be downloaded and unzipped.
The dataset is big, around 1.3GB.

Project Folder Organization:
sample_resources - contains samples of some the input and output files of various scripts, for reference
data_extraction - contains python and shell scripts used to extract the data from yelp dataset
lda - contains source code (and output fiels) to extract topics and to analyze and visualize the findings
dispersion_analysis - contains a python script for word dispersion analysis and plots.

Input data extraction and filtering:
Run the script extract_data to convert the files to CSV and extract relevant data.
$./extract_data

The script has a set of commands to do the following tasks:
- Creates input_resources directory, where all the files generated by this script would be kept
- Converts yelp_academic_dataset_business.json to yelp_academic_dataset_business.csv
- Converts yelp_academic_dataset_review.json to yelp_academic_dataset_review.csv
- Converts yelp_academic_dataset_user.json to yelp_academic_dataset_user.csv
- Filters out the restaurants from yelp_academic_dataset_review.csv into restaurant_ids file
- Extract the category information of restaurants into seprate file for later use
- Filters out users whose review count is greater than 10 into users file
- Filters out the reviews of the restaurants and users whose review count greater than 10 into reviews_of_users_with_atleast_11_reviews, and reviews_of_users_with_atleast_11_reviews_all_fields

Samples of this data are provided in sample_resources directory for reference.

ExtractReviews.py and ExtractRestaurantIDs.py scripts should be used to extract the data required for DispersionPlot.py script.

Run the LDA analysis program:
Once all the required input data is present in input_resources, proceed to execute the LDA by running lda_ml.py script
<pre>
$python lda_ml.py -h
Usage: lda_ml.py [options]

Options:
  -h, --help            show this help message and exit
  -f REVIEWS_FILE       reviews filename that contains only text of the
                        review, each in one line.
  -s STOPWORDS_FILE     stopwords filename
  -k NUM_TOPICS         Number of topics
  -d MIN_DF             Minimum document frequency for a token to be included
                        in the dictionary
  -n NUM_TERMS          Number of terms/tokens to be retained in the
                        dictionary
  -w NUM_WORDS          Number of words to be printed for each topic
  -l                    Load previously stored LDA model
  -c                    If topic probability distribution are available from
                        previous run, then dont capture topic distribution
                        for reviews again
  -r REVIEW_INFO_FILE   CSV file containing the users review information. The
                        order of the reviews in this file and the file
                        specified through -f option should be same.

$python lda_ml.py -f reviews_of_users_with_atleast_11_reviews -l -k 15 -w 50 -c -r reviews_of_users_with_atleast_11_reviews_all_fields
</pre>

This program would output the extracted topics. And lot of intermediate data will also be generated in lda_ml directory for reference and cross verification. Samples of the intermediate data is provided in sample_resources directory.

After the topics are extracted, certain manual analysis is required to tag the topics appropriately and to analyze the topics association with various restaurants.
analyze_topics_assoc script automates this analysis to certain extent. Run the script by issuing ./analyze_topics_assoc at shell prompt. This script uses categorize.py to produce the categorization of restaurants associated with a topic. In this case, topics association analysis is captured in lda_ml/heatmap_analysis file. Once the analysis is done, plot.py can be used to generate various charts.

The script DispersionPlot.py in dispersion_analysis directory produces the word correlation dispersion plots for various words in the user reviews.
