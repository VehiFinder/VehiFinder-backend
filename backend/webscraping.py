from bs4 import BeautifulSoup
import requests

pages = {
    "TuCarro": {
        "url": "https://vehiculos.tucarro.com.co/ford-focus",
        "criteria": {
            "classes": ".andes-money-amount__fraction:not(.ui-search-carousel--billboard span), .ui-search-item__title, .ui-search-card-attributes__attribute, .ui-search-item__location, .andes-carousel-snapped__slide",
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
        "url": "https://www.autocosmos.com.co/auto/usado?q=bmw",
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

class Carro:
    def __init__(self, precio, año, kilometraje, nombre, ubicacion, imagen):
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
    # if get_page.status_code != 200:
    #     print("Se ha producido un ERROR en la conexión")
    html_obtenido = get_page.text
    soup = BeautifulSoup(html_obtenido, "html.parser")
    classes = criteria.get("classes")
    content = soup.select(classes)
    attributes = []
    iterator = 0
    for values in content:
        print(values.get_text(separator=" ", strip=True,))
        print("--------------------------")
        # iterator += 1
        # if(values.img):
        #   attributes.append(values.img.get(pages.get(page_name).get("image_src")))
        # else:
        #   attributes.append(values.text)
        # if iterator == 6:
        #     iterator = 0
        #     new_car = create_car(attributes)
        #     cars.append(new_car)
        #     attributes = []
    # return cars 

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
scrape_function("autocosmos")

    