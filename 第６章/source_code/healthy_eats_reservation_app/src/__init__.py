from flask import Flask
from flask_sqlalchemy import SQLAlchemy # 追加
from flask_migrate import Migrate # 追加

# SQLAlchemyインスタンスの作成
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # 他の設定や初期化が必要であれば、ここに追加
    # 設定
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.sqlite' # 追加
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 追加

    # 初期化
    db.init_app(app) # 追加

    # マイグレーションエンジンの初期化
    migrate = Migrate(app, db) # 追加
    
    with app.app_context(): # 追加
        from src.restaurants.models import Restaurant # 追加

    # 各モジュールをインポートしてBlueprintを登録
    from src.restaurants.routes import restaurants_bp
    app.register_blueprint(restaurants_bp, url_prefix="/restaurants")

    return app
