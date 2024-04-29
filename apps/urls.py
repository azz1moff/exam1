from django.urls import path

from apps.views import ContactListView

urlpatterns = [
    path('', ContactListView.as_view())
]
