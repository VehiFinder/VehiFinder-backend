from config import Config

class CarModel:
    collection = Config.db['cars']
    
    @classmethod
    def save_car(cls, car):
        cls.collection.insert_one(car.__dict__)
    
    
    
    