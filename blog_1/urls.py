from django.urls import path, include

from .views import BlogListView, registration

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('user/registration/', registration),
    path("user/", include("django.contrib.auth.urls")),
]