from setuptools import setup
import quickedit


setup(name='django-quickedit',
      version=quickedit.__version__,
      description='Quick editing of fields in the django admin',
      author='Justin Quick',
      author_email='justquick@gmail.com',
      url='http://opensource.washingtontimes.com/projects/django-quickedit/',
      packages=['quickedit','quickedit.templatetags'],
      classifiers=['Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Framework :: Django',
          'License :: OSI Approved :: Apache Software License',
          ],
      )
