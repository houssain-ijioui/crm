from django.urls import path
from . import views 


urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("accounts/login/", views.login_view, name="login"),
    path("accounts/logout/", views.logout_view, name="logout"),
    path("accounts/register/", views.register, name="register"),
    path("products", views.products, name="products"),
    path("customer", views.customer, name="customer"),
    path("place_order", views.place_order, name="place_order"),
    path("c/<int:id>", views.customer_page, name="customer_page"),
    path("c/delete/<int:id>", views.delete_customer, name="delete_customer"),
    path("order/<int:id>", views.order, name="order"),
    path("delete_order/<int:id>", views.delete_order, name="delete_order"),
    path("search", views.search, name="search")
]
