from django.conf.urls import url

from api.viewsets import (
    ProductViewSet,
    ProductViewSetPost,
)

urlpatterns = [
    url(r'^products/$', ProductViewSet.as_view(), name='products'),
    url(r'^productsPost/$', ProductViewSetPost.as_view(), name='productsPost'),
]
