from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from utilities.db import db

carbs = db['carbohydrate']
proteins = db['proteins']
fats = db['fats']

def get_cosine_matrix(nutrient):
    vectorizer = TfidfVectorizer()
    data = []
    if nutrient=='carbs':
        for i in carbs.find():
            data.append(i['nutritional_contents'])
    if nutrient=='proteins':
        for i in proteins.find():
            data.append(i['nutritional_contents'])
    if nutrient=='fats':   
        for i in fats.find():
            data.append(i['nutritional_contents'])
    tfidf_matrix = vectorizer.fit_transform(data)
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return cosine_sim

def get_recommendations(nutrient,cosine_sim,food_item):
    data = []
    if nutrient=='carbs':
        for i in carbs.find():
            data.append(i['name'])
    if nutrient=='proteins':
        for i in proteins.find():
            data.append(i['name'])
    if nutrient=='fats':
        for i in fats.find():
            data.append(i['name'])
    food_index = data.index(food_item)
    print(food_index)
    sim_scores = list(enumerate(cosine_sim[food_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:3]  

    similar_food_indices = [i[0] for i in sim_scores]
    similar_food_items = [data[similar_food_indices[0]],data[similar_food_indices[1]]]
    return similar_food_items

