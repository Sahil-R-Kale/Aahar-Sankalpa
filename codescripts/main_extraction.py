from utilities.db import db
from utilities.city_tiers import tier_1,tier_2,tier_3
from utilities.similarity import get_recommendations

carbs = db['carbohydrate']
proteins = db['proteins']
fats = db['fats']

def get_nutrition(nutrient,recipe,city):
    nutrient,recipe = nutrient.lower(),recipe.lower()
    if nutrient=='carbohydrates':
        fetched_object = carbs.find_one({'name':f'{recipe}'})
    elif nutrient=='proteins':
        fetched_object = proteins.find_one({'name':f'{recipe}'})
    elif nutrient=='fats':
        fetched_object = fats.find_one({'name':f'{recipe}'})
    result = {}
    if fetched_object:
        result.update({'recipe_name':f"{fetched_object['name']}",
                       'calories':f"{fetched_object['calories']}",
                       'fat_g':f"{fetched_object['fat_total_g']}",
                       'carbohydrates_g':f"{fetched_object['carbohydrates_total_g']}",
                       'protein_g':f"{fetched_object['protein_g']}",
                       'fiber_g':f"{fetched_object['fiber_g']}",
                       'sugar_g':f"{fetched_object['sugar_g']}",
                       'sodium_mg':f"{fetched_object['sodium_mg']}",
                       'cholesterol_mg':f"{fetched_object['cholesterol_mg']}"})
        if city.capitalize() in tier_1:
            result.update({'price':f"{fetched_object['price_tier_1']}"})
        elif city.capitalize() in tier_2:
            result.update({'price':f"{fetched_object['price_tier_2']}"})
        elif city.capitalize() in tier_3:
            result.update({'price':f"{fetched_object['price_tier_3']}"})
        else:
            result.update({'price':f"{fetched_object['price_tier_4']}"})
    return result

carb_recipes = db['carb_recipes'] 
protein_recipes = db['protein_recipes'] 
fats_recipes = db['fats_recipes'] 

def get_recipe(nutrient,item):
    nutrient,item = nutrient.lower(),item.lower()
    if nutrient=='carbohydrates':
        fetched_object = carb_recipes.find_one({'name':f'{item}'})
    elif nutrient=='proteins':
        fetched_object = protein_recipes.find_one({'name':f'{item}'})
    elif nutrient=='fats':
        fetched_object = fats_recipes.find_one({'name':f'{item}'})
    result = {}
    if fetched_object:
        result.update({'recipe_name':f"{fetched_object['name']}",
                       'recipe_title':f"{fetched_object['title']}",
                       'ingredients':f"{fetched_object['ingredients']}",
                       'instructions':f"{fetched_object['instructions']}",
                       'servings':f"{fetched_object['servings']}"
                    })
    return result

def get_suggestions(nutrient,food_item):
    nutrient,food_item = nutrient.lower(),food_item.lower()
    from app import carbohydrates_matrix,proteins_matrix,fats_matrix
    data = []
    if nutrient=='carbs':
        for i in carbs.find():
            data.append(i['name'])
        cosine_sim = carbohydrates_matrix
    elif nutrient=='proteins':
        for i in proteins.find():
            data.append(i['name'])
        cosine_sim = proteins_matrix
    elif nutrient=='fats':
        for i in fats.find():
            data.append(i['name'])
        cosine_sim = fats_matrix
    try:
        food_index = data.index(food_item)
        sim_scores = list(enumerate(cosine_sim[food_index]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:3]  
        similar_food_indices = [i[0] for i in sim_scores]
        similar_food_items = [data[similar_food_indices[0]],data[similar_food_indices[1]]]
    except:
        similar_food_items = []
    return similar_food_items
    