import os
from setuptools import setup

setup(name='django-newsapp',
      version='0.5.1',
      description='Django news module',
      long_description='Django news module',
      author='Alexey Osovitniy',
      author_email='a@trialine.lv',
      packages=['newsapp',],
      url='https://github.com/alexxxxey/django-news-app',
      include_package_data=True,
      zip_safe=False,
      requires=['django(>=1.4)', 'easy_thumbnails'],
      classifiers=['Development Status :: Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Natural Language :: English',
                   'Operating System :: Unix',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Application'],
      license='New BSD')
