from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth.views import login , logout
urlpatterns = [
    # Examples:
    # url(r'^$', 'src.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^home/$', 'fitness.views.home', name='home'),
   url(r'^login/$', login , {'template_name':'login.html'} , name='login'),
   url(r'^logout/$', logout ,{'template_name': 'logout.html' } ,name='logout'),
   url(r'^$', 'fitness.views.register' , name='register'),
   url(r'^blog/$', 'fitness.views.blog', name='blog'),
   url(r'^images/$', 'fitness.views.images', name='images'),
   url(r'^video/$', 'fitness.views.video', name='video'),
     url(r'^mentor/$', 'fitness.views.mentor', name='mentor'),
      url(r'^strpics/$', 'fitness.views.strpics', name='strpics'),
       url(r'^exepics/$', 'fitness.views.exepics', name='exepics'),
       url(r'^stretch/$', 'fitness.views.stretch', name='stretch'),
       url(r'^workout/$', 'fitness.views.workout', name='workout'),
    url(r'^admin/', include(admin.site.urls)),
     url(r'^contact/$', 'fitness.views.contact', name='contact'),
     url(r'^bmi/$', 'fitness.views.bmi', name='bmi'),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
