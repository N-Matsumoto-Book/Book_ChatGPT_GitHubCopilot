# src/restaurants/routes.py

# =====================================
# Title: 飲食店一覧画面のルーティング
# =====================================

from flask import Blueprint, render_template, abort, request
from src.restaurants.services import RestaurantManager 

restaurants_bp = Blueprint("restaurants", __name__)

@restaurants_bp.route("/")
def index():
    """
    飲食店一覧画面を表示する。

    機能:
    - ログイン/ログアウトボタンの表示
    - 新規ユーザー登録へのリンクの表示
    - 飲食店検索バーの表示 (地域、料理の種類、席数、予算に基づく)
    - 検索結果の表示
    - フィルタリングオプションの表示
    - 各飲食店へのリンクの表示
    """
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