import json
import requests
from django.views import generic
from django.http import JsonResponse

# URL de la API que se utilizo 
URL_API = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'
# URL de la API especifica por id
SPECIFIC_URL_API = 'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=11007'

class ApiView(generic.DetailView):

# Solicitud Get
    def get_api(self):
        with requests.get(URL_API) as response:
            if response.status_code == 200:
                response_data = response.json()
            else:
                response_data = {'message': 
                                'La solicitud no fue exitosa. Código de estado:', 
                                'data': response.status_code}
        return JsonResponse(response_data, status=200)

# Solicitud Post
    def post_api(self):
        data = {'idDrink': '0000', 'strDrink': 'Drink Test'}
        with requests.post(URL_API, data=data) as response:
            if response.status_code == 200:
                response_data = {'message': 'Datos recibidos', 'data': data}
            else:
                response_data = {'message': 
                                'La solicitud no fue exitosa. Código de estado:',
                                'data': response.status_code}
        return JsonResponse(response_data)

# Solicitud Put
    def put_api(self):
        datos = {'idDrink': '0000', 'strDrink': 'Drink Test'}
        datos_json = json.dumps(datos)
        with requests.put(SPECIFIC_URL_API, data=datos_json) as response:
            if response.status_code == 405:
                response_data = {'message':
                                'Datos recibidos pero el servidor no permite hacer solicitudes PUT',
                                'data': response.status_code }
            else:
                response_data = {'message': 'La solicitud no fue exitosa. Código de estado:',
                                'data': response.status_code}
        return JsonResponse(response_data)

# Solicitud Delete
    def delete_api(self):
        with requests.delete(URL_API) as response:
            if response.status_code == 405:
                response_data = {'message':
                                'Datos recibidos pero el servidor no permite hacer solicitudes DELETE',
                                'data': response.status_code }
            else:
                response_data = {'message': 'La solicitud no fue exitosa. Código de estado:',
                                'data': response.status_code}
        return JsonResponse(response_data)

