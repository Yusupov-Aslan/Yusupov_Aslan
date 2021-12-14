from django.urls import path

from webapp.views import index_view, add_view

urlpatterns = {
    path('', index_view),
    path('', add_view)
    # path('', add),
    # path('', add),

}
