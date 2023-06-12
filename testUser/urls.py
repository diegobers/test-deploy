from django.urls import path

from .views import TestUserView

app_name = 'testUser'


urlpatterns = [
    path("", TestUserView.as_view(), name="index"),
    #path('', TemplateView.as_view(template_name='base.html'), name='home'),

]
