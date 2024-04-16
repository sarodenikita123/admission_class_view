from django.urls import path
from .views import *


urlpatterns = [
    path("", CreateView.as_view(), name="create_url"),
    path("show/", ShowView.as_view(), name="show_url"),
    path("update/<int:pk>", UpdateView.as_view(), name="update_url"),
    path("cancel/<int:pk>", DeleteView.as_view(), name="cancel_url"),

]
