from flask import request, make_response, jsonify
from codescripts.main_extraction import get_nutrition, get_recipe

def send_response(data, code):
    '''
    The function generates JSON response according to given result 
    Args:
    data: data to be returned
    code: HTTP message code
    Returns: 
    result: JSON response
    '''
    response = make_response(
        jsonify(
            data
        ),
        code,
    )
    response.headers["Content-Type"] = "application/json"
    return response

def nutrition_controller():
    '''
    The function extracts nutrition data and cost from recipe 
    Returns: 
    result: JSON result of API
    '''
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
            try:
                json = request.json
                recipe = json['food_item']
                nutrient = json['nutrient']
                city = json['city']
                nutrition_data = get_nutrition(nutrient,recipe,city)
                if nutrition_data:
                    data = nutrition_data
                    message = "Nutrition data and cost extracted successfully"
                    code = 200
                    status = True
                else:
                    data = {}
                    message = "Food item not in DB"
                    code = 402
                    status = False
            except:
                data = {}
                message = "JSON keys incorrect"
                code = 401
                status = False
    else:
        data = {}
        message = "Wrong input type. Only JSON body allowed!"
        code = 404
        status = False
    return send_response({
                'message': message,
                'status': status,  
                'data': data
            }, code) 

def recipe_controller():
    '''
    The function extracts recipe of gievn food item 
    Returns: 
    result: JSON result of API
    '''
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
            try:
                json = request.json
                item = json['food_item']
                nutrient = json['nutrient']
                recipe = get_recipe(nutrient,item)
                if recipe:
                    data = recipe
                    message = "Recipe fetched successfully"
                    code = 200
                    status = True
                else:
                    data = {}
                    message = "Food item not in DB"
                    code = 402
                    status = False
            except:
                data = {}
                message = "Exception encountered while fetching recipe. Check JSON body"
                code = 401
                status = False
    else:
        data = {}
        message = "Wrong input type. Only JSON body allowed!"
        code = 404
        status = False
    return send_response({
                'message': message,
                'status': status,  
                'data': data
            }, code) 
    