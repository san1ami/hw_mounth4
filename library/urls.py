from django.contrib import admin
from django.urls import path, include
from books.views import *
from accounts.views import *
from clothes.views import *
from passport.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('books/', BookListView.as_view(), name='book_list'),
    path('books/add/', BookCreateView.as_view()),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/<int:pk>/edit/', BookUpdateView.as_view()),
    path('books/<int:pk>/delete/', BookDeleteView.as_view()),

    path('register/', RegisterView.as_view()),
    path('login/', UserLoginView.as_view(), name='login'),
    path('users/', UserListView.as_view()),

    path('clothes/male/', MaleClothesView.as_view()),
    path('clothes/female/', FemaleClothesView.as_view()),
    path('clothes/child/', ChildClothesView.as_view()),

    path('captcha/', include('captcha.urls')),

    path('passport/add/', PassportCreateView.as_view()),
]
