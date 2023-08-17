from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# SQLAlchemyインスタンスの作成
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # 他の設定や初期化が必要であれば、ここに追加
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # 初期化（追加）
    db.init_app(app)

    # マイグレーションエンジンの初期化（追加）
    migrate = Migrate(app, db)
    
    # モデルのインポート
    # 注意：このインポートはcreate_app関数の中で行われます。
    # これにより、循環参照の問題を避けつつ、モデルが適切にロードされます。
    with app.app_context():
        from src.restaurants.models import Restaurant

    # 各モジュールをインポートしてBlueprintを登録
    from src.restaurants.routes import restaurants_bp
    app.register_blueprint(restaurants_bp, url_prefix="/restaurants")

    return app
