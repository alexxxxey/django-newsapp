import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
      name='django-newsapp',
      version='1.0.0',
      packages=find_packages(),
      include_package_data=True,
      description='Django News/Blog module',
      long_description=README,
      license='New BSD',
      author='Alexey Osovitniy',
      author_email='a@trialine.lv',
      url='https://github.com/alexxxxey/django-news-app',
      zip_safe=False,

      classifiers=[
            'Environment :: Web Environment',
            'Framework :: Django',
            'Framework :: Django :: 2.0',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: not OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.6',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
      ],
      requires=['django(>=2.0)', 'easy_thumbnails'],
)
