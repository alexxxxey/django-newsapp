django-news-app
===============

News module for Django framework


1. Add "newsapp" to INSTALLED_APPS
2. For Django 1.7 run:
./manage.py migrate newsapp

2. Include the news URLconf in your project urls.py like this::

    url(r'^news/', include('newsapp.urls')),

3. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a new (you'll need the Admin app enabled).


* support modeltranslation
* have archive widget (by years and months)
* have only active news manager ( New.active_objects.all() )
