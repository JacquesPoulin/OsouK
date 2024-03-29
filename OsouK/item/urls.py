
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


app_name = "item"

urlpatterns = [
  path("", views.browse_item, name="browse"),
  path("newItem/", views.add_new_item, name="newItem"),
  path("<int:pk>/", views.detail, name="detail"),
  path("<int:pk>/edit/", views.edit_item, name="edit"),
  path("<int:pk>/delete/", views.delete_item, name="delete")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)