#CS584 HW#4
#Yang Zhou (11/10/2016)

import csv
import numpy as np
import create_matrix

#create_matrix.create_utility_and_similarity_matrix()  #use this line only in the first run. do not need to run thsi line again after changing k

#load the utility matrix
filename = 'data/utility.csv'
reader = csv.reader(open(filename, 'r'), delimiter=',')
utility = []
for row in reader:
    line = []
    for x in row:
        if float(x) > 999999999:
            x =0.0
        line.append(float(x))
    utility.append(line)

n_users=len(utility)



#load the similarity matrix
filename = 'data/similarity.csv'
reader = csv.reader(open(filename, 'r'), delimiter=',')
sim =[]
for row in reader:
    line = []
    for x in row:
        line.append(float(x))
    sim.append(line)


#load the test data
tusers = []
tmovies =[]

filename = 'data/test.csv'
reader = csv.reader(open(filename, 'r'), delimiter=',')

for i,row in enumerate(reader):
    if row[0] not in tusers:
        tusers.append(row[0])
    if row[1] not in tmovies:
        tmovies.append(row[1])

n_tusers = len(tusers)
n_tmovies = len(tmovies)

print (n_tusers, "test users")
print (n_tmovies , "test movies")


filename = 'data/test.csv'
reader = csv.reader(open(filename, 'r'), delimiter=',')
testdata =[]
for row in reader:
    line = []
    for x in row:
        line.append(x)
    testdata.append(line)


#load the movies ids
movies =[]

filename = 'data/train.csv'
reader = csv.reader(open(filename, 'r'), delimiter=',')

for i,row in enumerate(reader):
    if row[1] not in movies:
        movies.append(row[1])
n_movies = len(movies)
print (n_movies , "train movies")


#get the average rating of every user
useravg=[]
for i,u in enumerate(tusers):
    avg =0.0
    count = 0.0
    for x in utility[i]:
        avg += x
        count += 1.0
    avg = avg / count
    useravg.append(avg)
    
        

#use knn classification to find nearest neighbors and predict ratings
ratings =[]
for i,row in enumerate(testdata):
    u= tusers.index(row[0])
    if row[1] in movies:  #if this movie has been rated before
        m= movies.index(row[1])
        r = 0
        slist = sim[u]
        knn=np.argsort(slist)[-500:]   #index of 500 nearest neighbors
        knn=list(knn)
        knn.reverse()
        total_sim = 0
        for nb in knn:   #r = the weighted average of all neighbors
            if utility[nb][m] > 0:
                total_sim += slist[nb]
                r += utility[nb][m] * slist[nb]
        if total_sim > 0:
            r = r / total_sim
        else:  #if neighbors have not rated this movie
            r = useravg[u]  #the average rating of this user
            

    else:
        r = useravg[u] 

    if r < 0:
        r = 0
    if r > 5.0:
        r= 5.0
        
    ratings.append(r)

print ('there are',len(ratings),'ratings')
    
with open("prediciton.dat","w") as output: 
    for x in ratings:
        output.write(str(x)+'\n')








    
    
