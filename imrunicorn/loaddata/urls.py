from django.urls import path
from . import views

# router = routers.DefaultRouter()
# router.register('roll', views.RollView)
# router.register('student', views.StudentView)
# router.register('courses', views.CourseView)

app_name = 'load_data'
urlpatterns = [
    path('', views.page_loads, name='home'),

    path('foot_pound_calculator/', views.page_foot_pound_calc, name='foot_pound_calculator'),

    path('loads/', views.page_loads, name='loads'),

    path('estimated_dope/<int:load_pk>', views.page_estimated_dope, name='page_estimated_dope'),
    path('estimated_dope/', views.page_estimated_dope, name='page_estimated_dope'),

    path('firearm_detail/<int:firearm_pk>', views.page_firearm_detail, name='page_firearm_detail'),
    path('firearm_detail/', views.page_firearm_detail, name='page_firearm_detail'),
]

