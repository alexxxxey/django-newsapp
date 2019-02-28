================================
News module for Django framework
================================

Installation
------------

1. Add **newsapp** to **INSTALLED_APPS**
2. Add **'newsapp': 'testpackage.migrations.news'** in MIGRATION_MODULES
3. Run manage.py **makemigrations newsapp**
4. Run manage.py **migrate newsapp**

5. Include the news in your project urls.py **path('news/', include('newsapp.urls'))**

Customization
--------------
Custom fields
~~~~~~~~~~~~~~
You can extend new object with extra field by defining in settings.py:
::

    NEWSAPP_NEWS_CLASS = 'news.models.NewCustom'

and in models.py start writing your class like this:
::

    from newsapp.models import NewAbstract, NewCategory
    class NewCustom(NewAbstract):
    ...your code here...
        class Meta(NewAbstract.Meta):
            abstract = True

Options
~~~~~~~~~~~~~~
* NEWSAPP_NEWS_ON_PAGE - how much news in list. Default 10
* NEWSAPP_ENABLE_ARCHIVE - add archive by date functionality
* NEWSAPP_ENABLE_CATEGORIES - add categories functionality
* NEWSAPP_ENABLE_TAGS - add tags functionality


Other
-----
* support django-modeltranslation
