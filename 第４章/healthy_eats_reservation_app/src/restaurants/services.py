from src.restaurants.models import Restaurant

class RestaurantManager:

    @staticmethod
    def get_all_restaurants():
        return Restaurant.query.all()

    @staticmethod
    def get_restaurant_by_id(restaurant_id):
        return Restaurant.query.get(restaurant_id)

    @staticmethod
    def get_restaurants_by_criteria(location=None, cuisine_type=None, page=1, per_page=10):
        filters = []
        if location:
            filters.append(Restaurant.location.contains(location))
        if cuisine_type:
            filters.append(Restaurant.cuisine_type.contains(cuisine_type))
        query = Restaurant.query.filter(*filters).paginate(page=page, per_page=per_page)
        return query.items
