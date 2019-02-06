from django.urls import path
from test_app.views import test


urlpatterns = [
    path('', test, name='Testing')
]