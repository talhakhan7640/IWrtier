from django.urls import path
from . import views
# from .views import CreateCheckoutSessionView

urlpatterns = [
    path('', views.home, name='home'),
    # path('create-checkout-session', CreateCheckoutSessionView.as_view(), name='create-checkout-session')
]
