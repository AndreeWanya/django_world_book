from django.urls import path, re_path as url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),]