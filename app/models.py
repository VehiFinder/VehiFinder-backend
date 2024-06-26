from config import Config


class CarModel:
    collection = Config.db["cars"]

    @classmethod
    def save_car(cls, cars):
        car = [car.__dict__ for car in cars]
        cls.collection.insert_many(car)

    @classmethod
    def delete_car(cls, car_name):
        cls.collection.delete_one({"nombre": car_name})

    @classmethod
    def get_cars_by_filters(cls, filters):
        return list(cls.collection.find(filters))
