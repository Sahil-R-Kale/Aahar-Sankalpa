from flask import Flask
from routes.diet_bp import diet_bp
from flask_cors import CORS
from utilities.similarity import get_cosine_matrix

app = Flask(__name__)

app.register_blueprint(diet_bp)
cors = CORS(app, resources={r"*": {"origins": "*"}})

with app.app_context():
    carbohydrates_matrix = get_cosine_matrix('carbs')
    proteins_matrix = get_cosine_matrix('proteins')
    fats_matrix = get_cosine_matrix('fats')

@app.route('/')
def hello():
    app.logger.info('Hello endpoint hit')
    return 'Use /nutrition and /recipe endpoints'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)