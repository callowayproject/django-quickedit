from setuptools import setup, find_packages
import quickedit


setup(name='django-quickedit',
      version=quickedit.__version__,
      description='Quick editing of fields in the django admin',
      author='Justin Quick',
      author_email='justquick@gmail.com',
      url='http://github.com/washingtontimes/django-quickedit',
      packages=find_packages(),
      include_package_data=True,
      classifiers=['Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Framework :: Django',
          'License :: OSI Approved :: Apache Software License',
          ],
      )
