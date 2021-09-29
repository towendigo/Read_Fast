from django.urls import path, include

urlpatterns = [
    path('book/', include("book.urls")),
    path('author/', include("author.urls")),     
]