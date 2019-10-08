# -*- coding: utf-8 -*-
"""Assignment2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GqwOKHI8crRxrUJHZgjFKB1CSGlJkF5L

# Assignment 2 ― Classification

## 0. Introduction

In this second assigment, we will explore another cornerstone of machine learning: supervised classification. We will be specifically classifying movie reviews by their corresponding score. To do this, we will first pre-process the raw data by cleaning and turning each review into a vector. Then, we will explore the following learning algorithms for classification: support vector classifiers, random forests, and naive Bayes classifiers.

* [Question 1.1](#scrollTo=qQPEFaRiRbOS)
* [Question 2.1](#scrollTo=LawTBDrOcPJe)
* [Question 2.2](#scrollTo=Hqp7LyWtlLVx)
* [Question 3.1](#scrollTo=Qs_t1uVzh01s)
* [Question 3.2](#scrollTo=fl9Z0VVXoRsY)
* [Question 3.3](#scrollTo=Perywb8YapEU)
* [Question 4.1](#scrollTo=YKLBuWjmAKoJ)
* [Question 5.1](#scrollTo=Myn-42J9ACsH)
* [Question 6.1](#scrollTo=fN-dse1NBQnk)
* [Question 6.2](#scrollTo=wfCjr-JrEJya)
* [Quesiton 6.3](#scrollTo=l1iGVZtkE5fF)
$% latex commands for later use$
$\newcommand{\R}{\mathbb{R}}$
$\newcommand{\B}{\mathbb{B}}$
$\newcommand{\argmax}{\operatorname*{arg\ max}}$
$\newcommand{\given}{\; \vert \;}$

## 1. Importing Libraries and Data

For this assignment, we will be using a dataset of metatritic reviews. The data consists of a csv file where the first column is a string containing a user review and the second column contains the corresponding score that the user gave to the movie. First, we will import any libraries that we might use.

**Note.** You may use any library you'd like unless when otherwise specified to not use any or to use a particular one.

### Question 1.1 Importing Libraries

Add any modules you use as you complete the assignment here.
"""

import csv
import random
### Answer starts here ###
import pandas as pd
import re
import spacy
import numpy as np
from collections import Counter

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
### Answer ends here ###

!wget https://raw.githubusercontent.com/LiTigre/McGillAI-asg2-data/master/metacritic_dataset.csv

"""Let's create a variable to hold the name of the dataset for convenience."""

dataset_filename = 'metacritic_dataset.csv'

"""Also create a function to print a review."""

def print_review(review, score):
  print('--------------- Review with score of {} ---------------'.format(score))
  print(review)
  print('------------------------------------------------------')
  print()

"""Let's load the data and see what the first 10 reviews look like."""

with open(dataset_filename) as csv_file:
  csv_reader = csv.reader(csv_file)
  colnames = next(csv_reader)
  data = list(csv_reader)
  
for review, score in random.sample(data, 10):
  print_review(review, score)

"""## 2. Preprocessing

We will be converting our data into a binary bag-of-words representation (Google "binary bag-of-words"). To do this, we will perform two steps beforehand.

### Question 2.1 Cleaning the Data
Create a function called `clean`, which takes a string and then:

 1. lower-case all words 
 2. only keeps letters and spaces
  
  
  For example, this will cause
  
  >`This was the WORST movie I have EVER SEEN!!!!!!`
  
  to become
  
  >`this was the worst movie i have ever seen`
  
   Of course, you could do more pre-processing steps if you would like, such as lemmatization, stemming, etc... but TOTALLY OPTIONAL!
"""

nlp = spacy.load('en', disable=['parser', 'ner'])

def clean(review):
  ### Start of Answer ###
  
  # transform to lowercase, remove special characters, and lemmatization
  lowerString = review.lower()
  new_string = re.sub(r'[^a-zA-Z ]+', '', lowerString)
  global nlp
  doc = nlp(new_string)
  return " ".join([token.lemma_ for token in doc])
  
  #return new_string
  ### End of Answer ###

"""Test your function with this example string"""

print(clean("This was the WORST movie I have EVER SEEN!!!!!!"))

"""Now, we'll use the function to clean the whole dataset. We'll also turn the scores into integers while we're at it."""

clean_data = [[clean(review), int(score)] for review, score in data]

for review, score in random.sample(clean_data, 5):
  print_review(review, score)

"""### Question 2.2 Picking features

We now need to turn each review into vectors. We will pick the top 2,000 words as features

Using those 2,000 features, create a function called `vectorize` which will take a string as an input, and convert it to a vector using the binary bag of words representation.

For example, the string `"This movie made me cry"` will become a vector of size 2,000 with 5 elements being 1 (assuming each word is part of the 2,000 most common) and 1,995 being 0, that it, is i will look something like

 > `[0, 0, ..., 0, 1, 0, ..., 0, 1, 0..., 0, 1, 0, ..., 0, 1, 0 ..., 0, 1, 0, ..., 0, 0]`
 
 In order to accomplish this task, you will
 
 1. write a `get_vocab` function which takes as an argument a list of (cleaned) reviews and the vocabulary size and outputs the a list of size `vocab_size` containing the most common words.
 2. write a `vectorize` function which takes as an argument a review and the vocabulary and turns the review into its binary bag of words representation.
 3. use the `vectorize` function to create a new variable called `vectorized_data` which will contain the bag-of-words representation of each data point contained in the `clean_data` variable rather than its string representation. Don't forget that a data point consists of review-score pairs.

**Warning**: this may take up to five minutes depending on implementation. Make use of dictionaries if you want this to be faster. However, speed is not evaluated.
"""

def vectorize(some_string, vocab):
  ### Answer starts here ###
  # split the review in a list of words to match the most common words. Returns
  # a binary bag of words
  review = some_string.split()
  review_vector = np.zeros(len(vocab))
  for word in review:
    for index in range(len(vocab)):
      if word == vocab[index][0]:
        review_vector[index] = 1
  return review_vector
  ### Answer ends here ###

def get_vocab(reviews, vocab_size):
  ### Answer starts here ###
  # create one list containing all the words from all reviews in order to use it
  # in a Counter object
  all_text = []
  for review in reviews:
    review = review.split()
    for index in range(len(review)):
      all_text.append(review[index])
  
  count = Counter(all_text)   
  return count.most_common(vocab_size)

  ### Answer ends here ###
  
def vectorize_all(reviews, vocab):
  ### Answer starts here ###
  all_bags = []
  for review in reviews:
    # list contains the bag of words and the corresponding score
    bag_vector = [vectorize(review, vocab), review[1]]
    all_bags.append(bag_vector)
  return all_bags
      
  ### Answer ends here ###

"""Test your function with the following code.
The `vocabulary` variable should have a length of 2000 and the most common words should be "the", "and", "a", etc.
"""

num_features = 2000
vocabulary = get_vocab([review for review, score in clean_data], num_features)
print(len(vocabulary))
print(vocabulary)

"""Test your function with the following input.
The vector should have four "1"s.
"""

vector = vectorize("the and a of zyxw", vocabulary)
print(vector)
print(sum(vector))

"""Now, vectorize the whole dataset."""

### Answer starts here ###
vectorized_data = vectorize_all([[review, score] for review, score in clean_data], vocabulary)
### Answer ends here ###

print(vectorized_data)

for vector, score in random.sample(vectorized_data, 5):
  print_review(vector, score)

"""For convenience, we will write a function called `preprocess_sample_point` which takes as input a single raw review and ouputs its binary bag-of-words representation."""

def preprocess_sample_point(review, vocab):
  return vectorize(clean(review), vocab)

vectorized_review = preprocess_sample_point(
    'The movie was not bad, it was really good!', vocabulary)
print(sum(vectorized_review))
print(vectorized_review)

"""### Question 2.4 Cleaning, Again

You may have noticed that some of the reviews are not in English. If we keep them in the dataset, this may cause accuracy to decrease. This is due to the fact that many of them will contain no words from our vocabulary, and will all have a zero-vector bag-of-words representation. However, there may be non-English language reviews that contain at least one word which is spelled the same as an English word. So, a better heuristic to determine if a review is in English or not is to check if it has at least 5 words from our vocabulary.

To that end, create a variable called `english_data`, which contains only the bag-of-words representations of english reviews by keeping only those which have at least 5 non-zero entries.
"""

### Answer starts here ###
english_data = [[review, score] for review, score in vectorized_data if sum(review) > 4]
### Answer ends here ###

print(len(vectorized_data), len(english_data))

"""## 3. Train-Test Split

### Question 3.1 Shuffling

The dataset is not ordered randomly. In fact, reviews from the same movie are put one after another as well as movies from the same year. To avoid introducing bias when splitting the dataset, we should shuffle it.

To that end, first create a copy of the variable `english_data`, which will be called `shuffled_data`, and then shuffle it so that it consists of a random reordering of the rows in `english_data`. 

**Note**: In practice, making a copy is not necessary. This is done to make testing easier since Jupyter alters global state whenever a cell is executed.
"""

# We create a copy of the clean_data
### Answer starts here ###
### Answer ends here ###
shuffled_data = english_data.copy()
# We will check the first 5 reviews, non-randomized
for review, score in english_data[0:5]:
  print_review(review, sum(review))

# Randomly reorder `shuffled_data`, making sure that `clean_data` is not altered
### Answer starts here ###
random.shuffle(shuffled_data)
### Answer ends here ###

# Let's check the first 5 movies in the randomized list
for review, score in shuffled_data[0:5]:
  print_review(review, score)

"""### Question 3.2 Creating Feature and Class variables

Now that the data is shuffled, we will create a variable that will contain all the features, called `X` and another which will contain all the classes, called `y`.

Further, to simplify the task, we will use 2 classes intead of 11. That is, review scores 0, 1, 2, 3 will be class 0, review scores 9, 10 will be given class 1, and everything else will be ignored.
"""

### Answer start here ###
X = []
y = []

#only retain the reviews with scores 0,1,2,3,9,10. Ignore the rest.
for review, score in shuffled_data:
  if (score == 1 or score == 2 or score == 3 or score == 0):
    X.append(review)
    y.append(0)
  if (score == 9 or score == 10):
    X.append(review)
    y.append(1)
### Answer ends here ###

"""Let's check the class balance"""

for i in range(2):
  print('class {}:'.format(i), 
        100 * len([0 for value in y if value == i])/len(y))

"""We have to keep in mind that most of the dataset is made out of labels which are 1. For instance, if a classifier always outputs 1, they would have an accuracy of 67%. Thus, 67% should be our baseline performance, not 50%.

### Question 3.3 Spliting the Dataset

Partition the dataset into a test set and a training dataset. Select 80% of the data to be part of the training set and the rest to be part of the test set.

To that end, write a function called `train_test_split` which
takes as input `X`, `y` and `test_size`, a floating point number between 0 and 1indicating how much of the dataset should be part of the test set. The function should return a tuple in the order:

`(X_train, X_test, y_train, y_test)`
"""

def train_test_split(X, y, train_size):
  ### Answer starts here ###
  index = int(train_size * len(X))
  return X[:index], X[index:], y[:index], y[index:]
  ### Answer ends here ###

X_train, X_test, y_train, y_test = train_test_split(X, y, 0.8)

"""## 4. Support Vector Machines

A support vector classifier tries to find the best separating hyperplane through the data. If the data is linearly separable, it finds the a hyperplane which maximized the margin. If it isn't it tries to minimize cost associated with misclassifying points.

### Question 4.1 Creating a Support Vector Classifier
Using `scikit-learn`, create a support vector classifier for our review data.

1. Use `scikit-learn` to create a linear support vector classifer
2. Fit the model to our training set
3. Print training accuracy
4. Print test accuracy
"""

### Answer starts here ###
svm_clf = SVC(kernel='linear')
svm_clf.fit(X_train, y_train)

print("Training Accuracy: {}".format(accuracy_score(y_train, svm_clf.predict(X_train))))
print("Test Accuracy: {}".format(accuracy_score(y_test, svm_clf.predict(X_test))))
### Answer ends here ###

print(svm_clf.predict([preprocess_sample_point(
    'Boring. Such a bad movie. It was terrible and predictable', vocabulary)]))

print(svm_clf.predict([preprocess_sample_point(
    'I really liked this movie, it\'s great!', vocabulary)]))

"""## 5. Random Forests

Random forests are a kind of ensemble classifier, i.e. they are made up of a number of 'weak' learners where the final classification is a combination of the classifications of each learner.

### Question 5.1 Creating a Random Forest Classifier
Using `scikit-learn`, create a radom forest classifier for our review data.

1. Use `scikit-learn` to create a random forest classifier
2. Fit the model to our training set
3. Print training accuracy
4. Print test accuracy



Be sure to check the [documentation](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html). Try to play around with the hyperparameters to see if you can get higher accuracy. Specifically, try finding good values for `n_estimators`, `min_samples_split`, `max_depth` and `max_features`. Try to beat the linear SVM's accuracy.
"""

### Answer starts here ###
rfc = RandomForestClassifier(n_estimators=10, min_samples_split=2, max_depth=None, max_features='auto')
rfc.fit(X_train, y_train)

print("Training Accuracy: {}".format(accuracy_score(y_train, rfc.predict(X_train))))
print("Test Accuracy: {}".format(accuracy_score(y_test, rfc.predict(X_test))))
### Answer ends here ###

print(rfc.predict([preprocess_sample_point(
    'Boring. This movie is terrible', vocabulary)]))

print(rfc.predict([preprocess_sample_point(
    'This movie was pretty good', vocabulary)]))

"""##6. Naive Bayes
Until now, we've used pre-existing implementations of two types of classifiers: random forests and support vector machines. Now, we will cover a third type of classifier: naive Bayes classifers. However, this time we will be writing it from scratch.

Naive Bayes classifiers are part of a larger family of classifiers which are so called 'probabilistic classifiers'. This is because they do not only try to predict classes given features, but they estimate probabilities distributions over a set of classes.

First, we will go over some definitions.

**Definition.** A *prior probability* is the likelihood of an event given no further assumptions. For instance, the probability that it's raining is relatively low.

**Definiton.** A *posterior probability* or *conditional probability* is the likelihood of an event given that some other event has occurred. For instance, the probability that it's raining given that there are clouds is higher than if we don't make that assumption.

Now we will go over some motivation.

For the purpose of argument, imagine we had access to the probability distribution $\Pr$. That is, we know how likely features and classes are. For example, $\Pr(x_1 = 1)$ is the probability that the most common word, i.e. "the", is in a random movie review. Presumably, this probability is relatively high. As a second example, $\Pr(y = 1)$ is the probability that a random movie review is 'good'. In our case, this would be somewhere close to 0.67.

Since we hypothetically have access to the whole probability distribution, we also know conditional probabilities. For instance, we would know $\Pr(y = 0 \; \vert \; x_1 = 0)$, which is the probability that a random review is 'bad', given that it does not contain the word "the".

Given a probability distribution, we can find an optimal classifier which simply picks the class which maximizes the probability that we will see that class given the observed features, in other words our classifier $f: \B^n \to \B$ is given by:

$$ f(x_1, \ldots, x_n) = \argmax_{c \in \B} \Pr(y = c \given x_1, \ldots, x_n ).$$

Where $\argmax$ returns the element in $\B$ which maximizes the expression to its right, and $\B$ is the set with two elements, $\{0, 1\}$. For example, we have
$$ \argmax_{x \in \R} (x - x^2) = \frac 1 2, $$
since $\frac 1 2$ maximizes the expression $x - x^2$.

It would be great if we had access to the probability distribution $\Pr$, but unfortunately we don't in almost every case. This means we wish to try to estimate it given some samples, i.e. the training data.

However, we run into another issue: estimating the probability distribution is computionally expensive. Therefore, we assume that the different features are independent from one another. This is called the *naive conditional independence assumption*. In other words, we assume that

$$ \forall i \in \{1, \ldots, n\} : \Pr (x_i \given y, x_1, \ldots, x_{i-1}, x_{i+1}, \ldots, x_n) = \Pr(x_i \given y).$$

Using Bayes' Theorem, we can simplify the conditional independence assumption to:

$$\Pr(y \given x_1, \ldots, x_n) = \frac{\Pr(y) \prod_{i=1}^n \Pr(x_i \given y)}{\Pr(x_1, \ldots, x_n)}.$$

However, we can observe that the denominator is constant for a given input, so it's not actually necesarry to estimate it if all we want is to find the class with the maximum posterior probability. In other words,

$$ \Pr(y \given x_1, \ldots, x_n) \propto \Pr(y) \prod_{i=1}^n \Pr(x_i \given y), $$

so, our classification rule becomes

$$ f(x_1, \ldots, x_n) = \argmax_{y \in \B} \Pr(y) \prod _{i=1}^n \Pr(x_i \given y).$$

Where $\propto$ means "proportional to" and  $\prod_{i = 1}^n g(i)$ is like summation $\left(\sum_{i=1}^n g(i)\right)$, except that addition is replaced with multiplication. For example,

$$\prod_{i = 1}^5 i^2 = 1^2 \cdot 2^2 \cdot 3^2 \cdot 4^2 \cdot 5^2.$$

**Note**: To estimate prior and conditional probabilities, we use the ratios of occurence counts found in the dataset. For example, to estimate $\Pr(x_1 = 0 \; \vert \; y = 0)$, we have to calculate the number of instances of class zero for which $x_1 = 0$ and divide them by the number of instances of class 0.

**Note**: The naive independence assumption is usually false in practice for most features. Therefore, the resulting estimated probability distribution is usually a bad approximation of the true distribution. However, the resulting classifier often has a good performance, depending on the dataset.

### Quesiton 6.1 Estimating the Probability Distribution

It would be expensive to re-estimate prior and posterior probabilities every time, so we should save probabilities in memory.

Thus, you will need to save
1. $\Pr(y)$ for each $y \in \B$, and
2. $\Pr(x_i = u \; \vert \; y)$ for each $ i \in \{1, \ldots, n\}$, $u \in \mathbb{B}$ and $y \in \mathbb{B}$.

Remember that you are *estimating* the probabilities using the training set only.
"""

### Answer starts here ###

#Probability of y for each y in {0, 1
prob_y = []
prob_y.append(y_train.count(0)/len(y_train))
prob_y.append(y_train.count(1)/len(y_train))

#Probability of each x given y
prob_x_given_y = []

# for each word
for i in range(num_features):
  count_positive = 0
  count_negative = 0
  prob_for_word = []
  for j, X in enumerate(X_train):
    # if a specific word X[i] is present in the review and the review is positive P(X⋂y1), add one to the word's positive count
    if X[i] == 1 and y_train[j] == 1:
      count_positive += 1
    # if a specific word X[i] is present in the review and the review is negative P(X⋂y0), add one to the word's negative count
    if X[i] == 1 and y_train[j] == 0:
      count_negative += 1
  
  #Append P(X|y) = P(X⋂y)/P(y) for y in {0,1
  prob_for_word.append(count_negative/y_train.count(0))
  prob_for_word.append(count_positive/y_train.count(1))
  prob_x_given_y.append(prob_for_word)
  
  
### Answer ends here ###

"""### Question 6.2 Creating the Naive Bayes Classifier

Create a function called `naive_bayes` which will take as input a list of features $x_1, \ldots, x_n$ and outputs the class with the largest posterior probability given the input features.
"""

def naive_bayes(vec):
  ### Answer starts here ###
  
  # set variables from above as global (to access them in a function)
  global prob_y
  global prob_x_given_y
  
  list_of_probs = []
  
  #for 0 (negative) and 1 (positive)
  for i in range(len(prob_y)):
    x_given_y = 1
    for j in range(len(vec)):
      # for all the words present in the input list
      if vec[j] == 1:
        # get the corresponding probability of x given y from above variables
        # and add it to the multiplication terms ∏
        x_given_y *= prob_x_given_y[j][i]
        
    list_of_probs.append(x_given_y * prob_y[i])
  
  #find the highest probability between positive and negative 
  if list_of_probs[0] > list_of_probs[1]:
    return 0
  else: 
    return 1
  ### Answer ends here ###

"""### Question 6.3 Measuring Performance

Using the naive Bayes classifier, predict the classes for each sample point in the training set as well as the test set and print accuracies.

**Note.** You should get train and test accuracies of about 84-85%.
"""

### Answer starts here ###
train_preds = []
for X in X_train:
  train_preds.append(naive_bayes(X))

test_preds = []
for X in X_test:
  test_preds.append(naive_bayes(X))

# accuracy function
def accuracy(predictions, labels):
  correct = 0
  for index in range(len(predictions)):
    if (predictions[index] == labels[index]):
      correct += 1
  return correct/len(predictions)

print(accuracy(train_preds, y_train))
print(accuracy(test_preds, y_test))
    
### Answer ends here ###

print(rfc.predict([preprocess_sample_point(
    'Boring. This movie is terrible', vocabulary)]))

print(rfc.predict([preprocess_sample_point(
    'This movie was pretty good', vocabulary)]))

"""## 7. Conclusion

You have successfully completed MAIS 202 assignment 2! Hope you enjoyed! To submit, download as .py and upload it to its respective okpy assignment.
"""