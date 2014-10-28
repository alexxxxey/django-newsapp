=====
Polls
=====

News package simple


Quick start
-----------

1. Add "news-app" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'news-app',
    )

2. Include the polls URLconf in your project urls.py like this::

    url(r'^news/', include('polls.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).
