

#--------------------------------------------------initialize-----------------------------------------------------------#
#import modules
from collections import Counter
from math import log

#counters to track word frequency
class1_vocabulary = Counter()
class2_vocabulary = Counter()
#counts for the input to be classified
counts_for_test_string = Counter()

#define initial probabilities
class1_initial_probs = 0.5
class2_initial_probs = 0.5

#create empty lists that will hold the probabilities
class1_prob_list = []
class2_prob_list = []

#list to track ignored words
ignored_words = []

#------------------------------------------------------------------------------------------------------------------------#









#-------------------------------------------- data loading and preprocessing----------------------------------------------#
#loads training data
def load_data(file):
    with open(file, 'r') as myfile:
        data = myfile.read().replace('\n', '')
    return data

#remove special characters
def preprocess_raw_text(text):
    for substring in ['/', '\\', '\r', '-', '\n']:
           text = text.replace(substring, ' ')
    for substring in ['.', ',', ';', '!', '(', ')', '?', '&', '*', ':', '"', '\'', '\xd5', '$', '[', ']']:
            text = text.replace(substring, '')
    text = text.lower()
    return [text]


#store words in Counter with usage counts
def class1_train(statements):
    for statement in statements:
        class1_vocabulary.update(word.lower() for word in statement.split())

def class2_train(statements):
    for statement in statements:
        class2_vocabulary.update(word.lower() for word in statement.split())

#-------------------------------------------------------------------------------------------------------------------------#







#---------------------------------------------- Classify -----------------------------------------------------------------#

#parse and count words in test string 
def evaluate_test_string(statements):
  
    for statement in statements:
        counts_for_test_string.update(word.lower() for word in statement.split())

    for word in counts_for_test_string:        
        #ignore words that have 3 or less characters
        if (len(word) < 4):
            ignored_words.append(word)
            continue
        else:
            #print( so we can track the progress)
            print( 'testing feature:' + word)
            print( 'class 1 probability for feature:' + str(convert_class_percent_for_word(word, class1_vocabulary)))
            print( 'class 2 probability for feature:' + str(convert_class_percent_for_word(word, class2_vocabulary)))
            
            #append the probablity for each word to the respective class probabilites list
            class1_prob_list.append(convert_class_percent_for_word(word, class1_vocabulary))
            class2_prob_list.append(convert_class_percent_for_word(word, class2_vocabulary))
    print( '------------------------------------')
    print( 'Ignored words:')
    print( ignored_words)




#helper function
def convert_class_percent_for_word(word, counter):
    #Laplace smoothing to remove zero frequency issues
    laplace_value = 1.00
    vocabulary = float(len(counter))
    return float(float(counter[word] + laplace_value)/(sum(counter.values()) + vocabulary))#in English = return a float value of frequency of the given word plus the laplace value / total number of words in the training set for the class plus the total vocabulary in the class training set (unique words)




#calculate probability for the class - multiply all probabilities for the words in the test string for the class
def prob_class(list):
    running_prob = 1.00
    for item in list:
        scalar = 1.00 
        #to prevent underflow of small floats
        scaled_value = float(item) + scalar
        running_prob *= scaled_value
    return running_prob
             




#calulculate posterior probability and make a decision
def calculate_posterior_and_decide(class1Prob, class2Prob):
    
    #multiply by priors
    class1Prob = float(class1Prob * class1_initial_probs)
    class2Prob = float(class2Prob * class2_initial_probs)
    
    #calculate posterior probability
    posterior_class1 = class1Prob / (class1Prob + class2Prob)
    posterior_class2 = class2Prob / (class1Prob + class2Prob)


    print( '------------------------------------')
    print( 'Class 1 Posterior Probability:' + str(posterior_class1 * 100) + '%')
    print( 'Class 2 Posterior Probability:' + str(posterior_class2 * 100) + '%')
    print( '------------------------------------')
   
   
   
    if (posterior_class1 > posterior_class2):
        print( 'Class 1 selected - It is more likely that the test phrase came from Class 1')
    elif (posterior_class1 == posterior_class2):
        print( 'Probabilities identical for classes. Cannot make a decision')
    else:
        print( 'Class 2 selected - It is more likely that the test phrase came from Class 2')
        return 'class 2'





#-------------------------------------------------------------------------------------------------------------------------#