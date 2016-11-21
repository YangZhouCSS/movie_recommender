#CSS584 HW#4
#Yang Zhou (11/10/2016)

import csv
import numpy as np


def create_utility_and_similarity_matrix():
    #load train data and create the utility matrix
    movies =[]
    users=[]

    filename = 'data/train.csv'
    reader = csv.reader(open(filename, 'r'), delimiter=',')

    for i,row in enumerate(reader):
        if row[0] not in users:
            users.append(row[0])
        if row[1] not in movies:
            movies.append(row[1])


    n_users = len(users)
    n_movies = len(movies)


    utility = np.zeros((n_users, n_movies))

    reader = csv.reader(open(filename, 'r'), delimiter=',')
    for row in reader:
        x = users.index(row[0])
        y = movies.index(row[1])
        utility[x][y] = row[2]


    np.savetxt("data/utility.csv", utility, delimiter=",")




##    #create normalized utility metrix
##    useravg=[]
##    for i,person in enumerate(users):
##        avg = sum(utility[i]) / (9936 - utility[i].count(0))
##        useravg.append(avg)
##
##    normalize = np.zeros((n_users, n_movies))
##    for i in range(0, n_users):
##        for j in range(0, n_movies):
##            if utility[i][j] != 0:
##                normalize[i][j] = utility[i][j] - useravg[i]
##            else:
##                normalize[i][j] = float('Inf')
##
##    np.savetxt("data/normalized_utility.csv", normalize, delimiter=",")




    #calculate the similarity between users and create the similarity metrix
    from sklearn.metrics.pairwise import cosine_similarity

    sim = np.zeros((n_users, n_users))

    for i,line in enumerate(utility):
        for j,otherline in enumerate(utility):
            selfvector = utility[i]
            nbvector = utility[j]
            selfvector = np.asarray(selfvector)
            nbvector = np.asarray(nbvector)
            selfvector = selfvector.reshape(1,-1)
            nbvector = nbvector.reshape(1,-1)
            s = cosine_similarity(selfvector,nbvector)
            s=s[0][0]
            sim[i][j] = s

    np.savetxt("data/similarity.csv", sim, delimiter=",")
