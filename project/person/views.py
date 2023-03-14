import json
import requests
from django.views import generic
from django.http import JsonResponse
from django.urls import reverse_lazy
from person.models import User, Rol
from .forms import UserForm, RolForm, PermissionsForm

# URL de la API que se utilizo 
URL_API = 'https://super-heroes-giweb-default-rtdb.firebaseio.com/'
# URL de la API especifica por id
SPECIFIC_URL_API = 'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=11007'

class ApiView(generic.DetailView):

# Solicitud Get
    def get_api(self):
        with requests.get(URL_API) as response:
            if response.status_code == 200:
                response_data = {'message': 
                                'La solicitud no fue exitosa. Código de estado:', 
                                'data': response.status_code}
                print(dir(response))
                print(response.raise_for_status())
                print("gefgdgfg"*12)
                print(response.__dict__)
                print("gefgdgfg"*12)
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
    
#CRUD delos usrios Rol Permisos 
class UserList(generic.ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users'

class UserDetail(generic.DetailView):
    model = User
    template_name = 'user/user_detail.html'
    context_object_name = 'user'

class UserCreate(generic.CreateView):
    model = User
    form_class = UserForm
    template_name = 'user/user_create.html'
    success_url = reverse_lazy('user_list')
    
class UserUpdate(generic.UpdateView):
    model = User
    form_class = UserForm
    template_name = 'user/user_create.html'
    success_url = reverse_lazy('user_list')

class UserDelete(generic.DeleteView):
    model = User
    template_name = 'user/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')
    
class RolList(generic.ListView):
    model = Rol
    template_name = 'rol/rol_list.html'
    context_object_name = 'rols'

class RolDetail(generic.DetailView):
    model = Rol
    template_name = 'rol/rol_detail.html'
    context_object_name = 'rol'

class RolCreate(generic.CreateView):
    model = Rol
    form_class = RolForm
    template_name = 'rol/rol_create.html'
    success_url = reverse_lazy('rol_list')
    
class RolUpdate(generic.UpdateView):
    model = Rol
    form_class = RolForm
    template_name = 'rol/rol_create.html'
    success_url = reverse_lazy('rol_list')

class RolDelete(generic.DeleteView):
    model = Rol
    template_name = 'rol/rol_confirm_delete.html'
    success_url = reverse_lazy('rol_list')
    
