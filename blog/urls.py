from django.urls import path
from .views import BlogCreateView  # ContactsPageView, ProductDetailView
from blog.apps import BlogConfig
app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    # path('', ..., name='view'),
    # path('view/<int:pk>/', ..., name='view'),
    # path('edit/<int:pk>/', ..., name='edit'),
    # path('delete/<int:pk>/', ..., name='delete'),
]
