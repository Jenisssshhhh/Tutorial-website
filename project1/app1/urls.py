from django.urls import path
from app1 import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home),
    path('home',views.home,name = "home"),
    path('about',views.about,name="about"),
    path('login',views.login_view,name = "login"),
    path('signup',views.signup,name = "signup"),
    path('topics/<int:course_id>', views.topics, name='topics'),
    path('courses',views.courses,name = "courses"),
    path('category/<int:category_id>',views.category,name='category'),
    path('contact',views.contact,name = 'contact')
    


    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




    
