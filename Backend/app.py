from flask import Flask
from routes.diet_bp import diet_bp
from flask_cors import CORS

app = Flask(__name__)

app.register_blueprint(diet_bp)
cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route('/')
def hello():
    app.logger.info('Hello endpoint hit')
    return 'Use /nutrition and /recipe endpoints'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)