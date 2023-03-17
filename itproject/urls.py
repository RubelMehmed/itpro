from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),
    path('itshop', include('itshop.urls'))
]


#    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
#     path('jet/dashboard/', include('jet.dashboard.urls',
#          'jet-dashboard')),  # Django JET dashboard URLS


# matreial ui
#path('', include('admin_material.urls')),
