from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PostCreateView, PostListView, AddCommentView

urlpatterns = [
   path('principal/', views.principal, name='principal'),
   path('', views.post_list, name='post_list'), #si quiero que principal se muestre separado tengo que colocar en las comillas "poslist otra vez "
   path('post/new/', PostCreateView.as_view(), name='post_create'), #Creacion de nueva entrada
   path('post/list', PostListView.as_view(), name='post_list'),  # URL para ver todas las entradas
   path('post/<int:post_id>/comment/', AddCommentView.as_view(), name='add_comment'),  # URL para agregar comentarios
   
]