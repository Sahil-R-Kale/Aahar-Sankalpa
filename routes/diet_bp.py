from flask import Blueprint
from controllers.diet_controller import nutrition_controller,recipe_controller,suggestions_controller

diet_bp = Blueprint('diet_bp', __name__)

diet_bp.route('/nutrition', methods=['POST'])(nutrition_controller)
diet_bp.route('/recipe', methods=['POST'])(recipe_controller)
diet_bp.route('/suggestions', methods=['POST'])(suggestions_controller)
