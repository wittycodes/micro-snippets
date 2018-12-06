import model.naive_bayes as model



class1_train_dataset='training texts/jfk-ask-not-speech.txt'
class2_train_dataset='training texts/mlk-dream-speech.txt'
test_dataset='training texts/jfk-moon-speech.txt'

#training data from file
class1_loaded = model.load_data(class1_train_dataset)
class2_loaded = model.load_data(class2_train_dataset)

#preprocess the loaded files
class1_preprocessed = model.preprocess_raw_text(class1_loaded)
class2_preprocessed = model.preprocess_raw_text(class2_loaded)


#train with preprocessed data
model.class1_train(class1_preprocessed)
model.class2_train(class2_preprocessed)

#test string from file
testing_data = model.load_data(test_dataset)
processed_test_string = model.preprocess_raw_text(testing_data)
model.evaluate_test_string(processed_test_string)

#multiply all of the probabilities for each class
class1_calculated_prob = model.prob_class(model.class1_prob_list)
class2_calculated_prob = model.prob_class(model.class2_prob_list)


#final result
model.calculate_posterior_and_decide(class1_calculated_prob, class2_calculated_prob)


