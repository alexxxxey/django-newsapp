django-news-app
===============

News module for Django framework


1. Add "newsapp" to INSTALLED_APPS
2. For Django 1.8 run:
./manage.py migrate newsapp

2. Include the news URLconf in your project urls.py like this::

    url(r'^news/', include('newsapp.urls')),

3. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a new (you'll need the Admin app enabled).

4. You can extend new object with extra field by defining NEWSAPP_NEWS_CLASS = 'news.models.NewCustom' in settings.py and in models.py start writing your class like this 
```
from newsapp.models import NewAbstract, NewCategory
class NewCustom(NewAbstract):
    ...
    class Meta(NewAbstract.Meta):
        abstract = True
```


* support modeltranslation
* NEWSAPP_ENABLE_ARCHIVE = True - have archive widget (by years and months)
* NEWSAPP_ENABLE_CATEGORIES = True - have categories
* NEWSAPP_NEWS_ON_PAGE = 10 - news objects per page
* have active news manager ( New.active_objects.all() )
