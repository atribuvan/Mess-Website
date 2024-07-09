from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'ajax'

urlpatterns = [
    path('update_rebate_status/', views.update_rebate_status, name='update_rebate_status'),
    path('add_caterer/', views.add_caterer, name='add_caterer'),
    path('update_caterer_info/', views.update_caterer_info, name='update_caterer_info'),
    path('get_caterer_info/<int:caterer_id>/', views.get_caterer_info, name='get_caterer_info'),
    path('add_cafeteria/', views.add_cafeteria, name='add_cafeteria'),
    path('get_cafeteria/<int:id>/', views.get_cafeteria, name='get_cafeteria'),
    path('update_cafeteria/', views.update_cafeteria, name='update_cafeteria'),
    path('add_semester/', views.add_semester, name='add_semester'),
    path('add_messperiod/', views.add_mess_period, name='add_messperiod'),
    path('get-dates/<int:semester_id>/<int:mess_period_id>/', views.get_dates, name='get_dates'),
    path('shortRebateForm/', views.shortRebateForm, name='shortRebateForm'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)