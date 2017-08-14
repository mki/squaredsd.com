from django.conf.urls import url, include

from api.views.products import ProductsView

urlpatterns = [
    url(r'^products', ProductsView.as_view()),
]
