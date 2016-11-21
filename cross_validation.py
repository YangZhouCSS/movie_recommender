#CS584 HW#4
#Yang Zhou


import csv
import numpy as np
import random

#cross validation
#randomly select about 20% (about 128000 lines) ratings to be the test set

#create new train and test sets

##filename = 'data/train.csv'
##reader = csv.reader(open(filename, 'r'), delimiter=',')
##
##trainset =[]
##testset=[]
##lastrow=['75']
##for i,row in enumerate(reader):
##    if random.uniform(0.0,100.0)<80.0 or row[0] != lastrow[0]: #keep at least one row
##        trainset.append(row)
##    else:
##        testset.append(row)
##    lastrow = row
##
##print (len(trainset),"lines of train data")
##print (len(testset),"lines of test data")
##
##
##    
##with open("data/train_cv.csv",'w') as f:
##    for row in trainset:
##        for x in row:
##            f.write(x+',')
##        f.write('\n')
##
##
##with open("data/test_cv.csv",'w') as f:
##    for row in testset:
##        for x in row:
##            f.write(x+',')
##        f.write('\n')


#use movie_recommender.py to predict rating and then
#perform validation using the following code
filename = open('prediciton.dat','r')
y_predicted = filename.read().split('\n')
y_predicted =y_predicted[:-1]
for i,x in enumerate (y_predicted):
    y_predicted[i]=float(x)

filename = 'data/test_cv.csv'
reader = csv.reader(open(filename, 'r'), delimiter=',')
y_actual = []
for row in reader:
    y_actual.append(float(row[2]))


from sklearn.metrics import mean_squared_error
from math import sqrt

rmse = sqrt(mean_squared_error(y_actual, y_predicted))

print ('the root mean squared error is',rmse)
