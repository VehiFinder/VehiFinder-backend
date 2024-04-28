from bs4 import BeautifulSoup
import requests

pages = {
    "TuCarro": {
        "url": "https://vehiculos.tucarro.com.co/ford-focus",
        "criteria": {
            "classes": {
                ".ui-search-item__title": 1,
                ".andes-money-amount__fraction:not(.ui-search-carousel--billboard span)" : 2,
                ".ui-search-card-attributes__attribute": 3, 
                ".ui-search-item__location": 4,
                ".andes-carousel-snapped__slide:not(.ui-search-billboard__card)": 5,
                },
        },
        "image_src": "data-src"
    },
    "carroya": {
        "url": "https://www.carroya.com/automoviles-y-camionetas/ford/focus",
        "criteria": {
            "classes": ".cy-publication-card-ds-milla__publication-price-total",
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
    attributes = []
    iterator = 0
    real_classes = [
        key  # El resultado a guardar
        for x in content  # Iterar sobre cada elemento de 'content'
        for key in classes.keys()  # Iterar sobre las llaves de 'classes'
        if "." + x['class'][0] in key  # Condición para incluir 'key' en 'real_classes'
    ]
        
    # print(sorted_content)
    sorted_content = sorted(real_classes, key=lambda x: classes[x])
    print(sorted_content)

    # for value in sorted_content:
    #     print(value.text)
    for values in content:
        iterator += 1
        if(values.img):
          attributes.append(values.img.get(pages.get(page_name).get("image_src")))
        else:
          attributes.append(values.text)
        if iterator == 6:
            iterator = 0
            new_car = create_car(attributes)
            cars.append(new_car)
            attributes = []
    return cars 

    # get_images(images)


# def get_images(images):
#     data_src_values = [img.get("data-src") for img in images]
#     for i, url in enumerate(data_src_values):
#         if f"{url}".endswith("webp"):
#             r = requests.get(f"{url}")
#             with open(f"imagenes/imagen_{i}.webp", "wb") as f:
#                 f.write(r.content)


def create_car(attributes):
    precio = attributes[0]
    año = attributes[1]
    kilometraje = attributes[2]
    nombre = attributes[3]
    ubicacion = attributes[4]
    imagen = attributes[5]
    new_car = Carro(precio, año, kilometraje, nombre, ubicacion, imagen)
    return new_car


    
# Calls
scrape_function("TuCarro")


# for car in cars:
#     print(car.nombre)
    