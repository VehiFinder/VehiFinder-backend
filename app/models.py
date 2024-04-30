from config import Config


class CarModel:
    collection = Config.db["cars2"]

    @classmethod
    def save_car(cls, car):
        cls.collection.insert_one(car.__dict__)

    @classmethod
    def delete_car(cls, car_name):
        cls.collection.delete_one({"nombre": car_name})

    @classmethod
    def get_cars_by_filters(cls, filters):
        return list(cls.collection.find(filters))
