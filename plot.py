import matplotlib.pyplot as plt
import numpy as np

# plot variour charts for visualization.
def main():

    # Bar chart representing restaurant count by geographical food variety
    restaurant_types = ['Latino', 'South-Asian', 'Mid-East', 'European', 'Mexican', 'East-Asian', 'American']
    restaurant_count = [178, 224, 492, 1419, 1798, 2159, 4811]

    ind = np.arange(len(restaurant_count))
    width = 0.5

    plt.bar(ind, restaurant_count, width=width)
    plt.xticks(ind + width/2, restaurant_types)
    plt.title('Restaurants by food type')
    plt.show() 

    #Pie chart for European food
    labels = 'Italian', 'German', 'British', 'Spanish', 'French', 'Scottish', 'Irish'
    sizes = [1008, 21, 128, 40, 125, 28, 47]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'green', 'magenta', 'red'] 
    plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    #plt.title('European restaurants share')
    plt.show()
    
    #Pie chart for Asian food
    labels = 'Vietnamese', 'Filipino', 'Thai', 'Korean', 'Japanese', 'Mongolian', 'Chinese'
    sizes = [157, 54, 329, 119, 508, 19, 1002]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'green', 'magenta', 'red'] 
    plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    #plt.title('East asian restaurants share')
    plt.show()

    # Bar chart to show number of restaurants based on meal times
    meal_times = ['Pubs & Nightlife', 'Breakfast, Brunch', 'Dinning']
    rest_count = [1826, 5570, 9852]

    ind = np.arange(len(rest_count))
    width = 0.3

    plt.bar(ind, rest_count, width=width)
    plt.xticks(ind + width/2, meal_times)
    plt.title('Temporal categorization')
    plt.show()

    # Draw a plot showing the word concentration in a topic. The font size of a word in a topic will be decided by the probablity of that word in the topic
    #load topics probabilities from file
    topics_list = []
    max_prob = 0
    with open('input_resources/topics_for_chart', 'r') as fp:
        # Each line in the format topic xxx: probability1*word1 + probability2*word2 + ...
        for line in fp:
            topic_words = []
            word_probs = line.split('+')

            for word_str in word_probs:
                (prob_str, word) = word_str.strip().split('*')
                
                # the first word would have a prefix 'topic num: '. So strip it off
                prob_str = prob_str.split(':')
                if len(prob_str) > 1:
                    prob_str = prob_str[1].strip()
                else:
                    prob_str = prob_str[0].strip()

                prob = float(prob_str)
                if prob > max_prob:
                    max_prob = prob
                word_prob = (prob, word)
                topic_words.append(word_prob)

            topics_list.append(topic_words)

    # plot the topic words to show the concentration based on their probability of association with the topics
    num_topics = len(topics_list)
    num_words = 10 #len(topics_list[0])
    # Word with max prob should have the largest font
    fontsize_base = 40/max_prob 
    for t in range(num_topics):
        plt.subplot(1, num_topics, t+1)
        plt.ylim(0, num_words + 0.5)
        plt.xlim(0, 40)
        plt.xticks([])
        plt.yticks([])
        if t == 0 :
            plt.title("good experience")
        elif t == 1:
            plt.title("fast food")
        elif t == 2:
            plt.title("mexican")
        elif t == 3:
            plt.title("bad experience")
        elif t == 4:
            plt.title("breakfast")
        else:
            plt.title("topic {}".format(t))
    
        for i, (prob, word) in zip(range(num_words), topics_list[t]):
            plt.text(0.3, num_words-i, word, fontsize=fontsize_base*prob)

    # adjust the margins
    plt.tight_layout()
    plt.show()

    # Plot stacked barchart to show topic distribution of parking related reviews
    review_nums = ['r1-3', 'r2-3', 'r3-4', 'r4-3', 'r5-4', 'r6-4']
    # rows are reviews, and columns are topic probabilities for each review.
    # order of the topics in each row is: topic 0, topic 2, topic 6, topic 11 and topic 13
    # the numbers are taken from lda_ml/parking_reviews_analysis file
    topic_distr = np.array([[0.43715518192728697, 0, 0.2199335275086666, 0.32691124956180023, 0],
                            [0.57345668331375432, 0.19735966887362794, 0, 0.18918360438606333, 0],
                            [0.92820498984212629, 0, 0, 0, 0],
                            [0.55494845267339388, 0.37102748090226206, 0, 0, 0.05297138767793616],
                            [0.54729518677793176, 0.39079997508025671, 0, 0, 0],
                            [0.69249152198741792, 0, 0.26623856610063784, 0, 0]])

    N, K = topic_distr.shape
    # x-axis locations for the reviews
    ind = np.arange(N)
    # width of the bars
    width = 0.5
    plots = []
    height_cumulative = np.zeros(N)
    for k in range(K):
        color = plt.cm.coolwarm(k/K, 1)
        if k == 0:
            p = plt.bar(ind, topic_distr[:, k], width, color=color)
        else:
            p = plt.bar(ind, topic_distr[:, k], width, bottom=height_cumulative, color=color)

        height_cumulative += topic_distr[:, k]
        plots.append(p)

    # set height of the stacked bar
    plt.ylim(0, 1)
    plt.title('Topic distribution of reviews expressing parking concern')
    plt.ylabel('Topics')
    plt.xticks(ind+width/2, review_nums)
    plt.yticks(np.arange(0, 1, 10))
    topic_labels = []
    topic_labels.append('0: Accessibility & Location')
    topic_labels.append('2: Good Service & Experience')
    topic_labels.append('6: Bad Service & Experience')
    topic_labels.append('11: Breakfast & Brunch')
    topic_labels.append('13: Buffet, Lunch & Dinner')
    plt.legend([p[0] for p in plots], topic_labels)
    plt.show()

    #plot a heatmap to show the association of restaurant types and how they fare w.r.t different topics
    # Consider topic 0(accessibility), topic 2(good service), topic 6(bad service and experience), topic 9(good bar services) and topic 11(breakfast) for analysis
    # the numbers are taken from lda_ml/heatmap_analysis file.
    topic_dist = np.array([[0.0446, 0.0580, 0.0625, 0.0401, 0.0319],
                        [0.0391, 0.0619, 0.0637, 0.0497, 0.0494],
                        [0.0504, 0.1037, 0.1000, 0.0587, 0.0319],
                        [0.0378, 0.0706, 0.0795, 0.0506, 0.0457],
                        [0.0630, 0.0975, 0.0975, 0.0406, 0.0304],
                        [0.0747, 0.1007, 0.0902, 0.0669, 0.0495],
                        [0.0843, 0.1150, 0.1243, 0.0859, 0.0416],
                        [0.0560, 0.0835, 0.0916, 0.0731, 0.0584]])
    xlabels = ['Location, Accessibility, Decor', 'Good Service, Experience', 'Bad Service, Experience', 'Good Bar Services', 'Breakfast']
    ylabels = ['South Asian', 'American Fast Food', 'East Asian', 'Mexican', 'Mediterranean', 'European', 'Pubs & Bars', 'Breakfast & Bakeries']

    plt.pcolor(topic_dist, norm=None, cmap='Blues')
    # display restaurants categories on y-axis
    plt.yticks(np.arange(topic_dist.shape[0])+0.5, ylabels)
    # display topic tags on x-axi
    plt.xticks(np.arange(topic_dist.shape[1])+0.5, xlabels);
    #plt.gca().invert_yaxis()
    plt.xticks(rotation=90)
    # Add a legend
    plt.colorbar(cmap='Blues')
    # fix margins
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

