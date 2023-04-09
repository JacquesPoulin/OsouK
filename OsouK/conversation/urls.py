
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


app_name = "conversation"

urlpatterns = [
  path("", views.inbox, name="inbox"),
  path("<int:pk>/", views.detail, name="detail"),
  path("new/<int:item_pk>/", views.new_conversation, name="new"),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)