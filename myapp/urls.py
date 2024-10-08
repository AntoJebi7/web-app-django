"""
URL configuration for myapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# to handle error or no page 
handler404 = 'myapp.views.custom_page_not_found'


urlpatterns = [
    # assign the app's url here to initialize
    # to assign root url to our app , just theave empty string ""
    # we need to bring up the urls by including (module)
    # nothing but , it just boot our login urls in the root page (first default page)

    
    path("",include("login.urls")),
    path("register/",include("registration.urls")),
     path("otp/",include("otp.urls")),
    #works based on the same above concept 
    path("blog/",include("blog.urls")),
    #when we give admin/ , it will boot admin.site.urls
    path('admin/', admin.site.urls),
    

    

]
