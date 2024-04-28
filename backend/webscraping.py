from bs4 import BeautifulSoup
import requests

pages = {
    "TuCarro": {
        "url": "https://vehiculos.tucarro.com.co/ford-focus",
        "criteria": {
            "classes": {
                ".ui-search-item__title": 1,
                ".andes-money-amount__fraction:not(.ui-search-carousel--billboard span)" : 2,
                ".ui-search-card-attributes__attribute:first-of-type": 3, 
                ".ui-search-card-attributes__attribute:nth-of-type(2)": 4, 
                ".ui-search-item__group__element.ui-search-item__location": 5,
                ".andes-carousel-snapped__slide:not(.ui-search-billboard__card)": 6,
                },
        },
        "image_src": "data-src"
    },
    "autocosmos": {
        "url": "https://www.autocosmos.com.co/auto/usado/bmw",
        "criteria": {
            "classes": ".listing-card__car",
        },
        "image_src": "data-src"
    },
    "automax": {
      "url": "https://automax.com.co/",
      "criteria": {
        
      },
      
    }
}
#Precio, nombre, año, kilometraje, 

class Carro:
    def __init__(self, nombre, precio, año, kilometraje, ubicacion, imagen):
        self.nombre = nombre  # Marca del carro
        self.año = año  # Año de fabricación
        self.kilometraje = kilometraje  # Kilometraje del carro
        self.precio = precio  # Precio del carro
        self.ubicacion = ubicacion  # Ubicación del carro
        self.imagen = imagen  # Imagen del carro

def scrape_function(page_name):
    cars = []
    criteria = pages.get(page_name).get("criteria")
    url = pages.get(page_name).get("url")
    get_page = requests.get(url)
    html_obtenido = get_page.text
    soup = BeautifulSoup(html_obtenido, "html.parser")
    classes = criteria.get("classes")
    css_selector = ', '.join([f"{class_name}" for class_name in classes.keys()])
    content = soup.select(css_selector)
    attributes = {1: [], 2:[], 3: [], 4:[], 5:[], 6:[]}
    iterator = 0
    # real_classes = [key for x in content for key in classes.keys() if "." + x['class'][0] in key]
    for value in content:
        if(value.img):
            lista = attributes[6]
            lista.append(value.img.get(pages.get(page_name).get("image_src")))
        else:
            class_name = [key for key in classes.keys() if value["class"][0] in key]
            if len(class_name) >= 2:
                    name = class_name[iterator]
                    lista = attributes[classes.get(name)]
                    lista.append(value.text)
                    if iterator == len(class_name) - 1:
                        iterator = 0
                    else:
                     iterator += 1
            else:
                lista = attributes[classes.get(class_name[0])]       
                lista.append(value.text)
    cars = create_cars(attributes)
    return cars 

def create_cars(attributes):
    cars = []           
    for car_index in range(0, len(attributes[1])):
        new_car = Carro(attributes[1][car_index], attributes[2][car_index], attributes[3][car_index], 
                        attributes[4][car_index], 
                        attributes[5][car_index], 
                        attributes[6][car_index])
        cars.append(new_car)
     
    return cars


    
# Calls
cars = scrape_function("TuCarro")
for car in cars:
    # print(car.nombre)
    # print(car.precio)
    # print(car.año)
    # print(car.kilometraje)
    # print(car.ubicacion)
    # print(car.imagen)
    print("----------")
    