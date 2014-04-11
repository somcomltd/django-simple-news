# coding=utf-8
from distutils.core import setup

setup(name='django-simple-news',
      version='1.1',
      description='News application for Django project',
      author='SomCom Ltd',
      author_email='bwillmore@somcom.com',
      url='http://github.com/somcomltd/Django-simple-news',
      packages=['news','news.templates','news.templatetags'],
	  include_package_data=True,
      classifiers=[
           'Development Status :: 5 - Production/Stable',
           'Environment :: Web Environment',
           'Framework :: Django',
           'Intended Audience :: Developers',
           'Intended Audience :: Education',
           'License :: OSI Approved :: GNU General Public License (GPL)',
           'Natural Language :: English',
           'Operating System :: OS Independent',
           'Programming Language :: Python :: 2.4',
           'Programming Language :: Python :: 2.5',
           'Programming Language :: Python :: 2.6',
           'Programming Language :: Python :: 2.7',
           'Topic :: Education',
           'Topic :: Internet :: WWW/HTTP :: Site Management',
           'Topic :: Printing',
      ],
      )
