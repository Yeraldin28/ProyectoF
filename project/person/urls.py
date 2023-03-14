from django.urls import path
from . import views
urlpatterns = [
    path('get_api/', views.ApiView.get_api , name="get_api"),
    path('post_api/', views.ApiView.post_api , name="post_api"),
    path('put_api/', views.ApiView.put_api , name="put_api"),
    path('delete_api/', views.ApiView.delete_api , name="delete_api"),
    path('', views.UserList.as_view(), name='user_list'),
    path('<int:pk>/', views.UserDetail.as_view() , name='user_detail'),
    path('nuevo/', views.UserCreate.as_view(), name='user_create'),
    path('<int:pk>/editar/', views.UserUpdate.as_view(), name='user_update'),
    path('<int:pk>/eliminar/', views.UserDelete.as_view(), name='user_delete'),
    #Rol
    path('rol/', views.RolList.as_view(), name='rol_list'),
    path('rol/<int:pk>/', views.RolDetail.as_view() , name='rol_detail'),
    path('rol/nuevo/', views.RolCreate.as_view(), name='rol_create'),
    path('rol/<int:pk>/editar/', views.RolUpdate.as_view(), name='rol_update'),
    path('rol/<int:pk>/eliminar/', views.RolDelete.as_view(), name='rol_delete')
    ]