from flask import Blueprint, render_template, request, redirect, abort
from src.restaurants.services import RestaurantManager

restaurants_bp = Blueprint('restaurants_bp', __name__)


@restaurants_bp.route('/')
def index():
    try:
        location = request.args.get('location')
        cuisine_type = request.args.get('cuisine_type')

        # 入力のバリデーション
        if location and len(location) > 100:
            abort(400, description="Invalid location parameter.")
        if cuisine_type and len(cuisine_type) > 50:
            abort(400, description="Invalid cuisine_type parameter.")
        restaurants = RestaurantManager.get_restaurants_by_criteria(
            location, cuisine_type)
        return render_template('restaurants.html', restaurants=restaurants)
    except Exception as e:
        print(f"Error: {e}")  # 本番環境ではloggingモジュールを使用
        return e
