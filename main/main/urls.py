from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.userAdmin.urls')),
    url(r'^', include('apps.product.urls')),
    url(r'^', include('apps.customer.urls')),
    # url(r'^', include('apps.review.urls')),
    # url(r'^', include('apps.order.urls')),
]
