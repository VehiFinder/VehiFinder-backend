from config import Config

class CarModel:
    collection = Config.db['cars']
    
    @classmethod
    def save_car(cls, car):
        cls.collection.insert_one(car.__dict__)
    
    @classmethod
    def delete_car(cls, car_name):
        cls.collection.delete_one({'nombre': car_name})
    
    
    