import cStringIO
import gzip
import os

try:
    from urllib import urlopen
except ImportError:
    from urllib.request import urlopen

from setuptools import setup, find_packages
from setuptools.command.install import install as _install

highcharts_url = 'http://code.highcharts.com/highcharts.js'
resources_prefix = 'js/highcharts/resources/highcharts.js'

requires = [
    'fanstatic',
    ]

def download_file(url, path):
    usock = urlopen(url)
    data = usock.read()
    if usock.headers.get('content-encoding', None) == 'gzip':
        data = gzip.GzipFile(fileobj=cStringIO.StringIO(data)).read()
    open(path, 'w').write(data)

class install(_install):
    def run(self):
        _install.run(self)
        resources_dir = os.path.join(self.install_platlib, resources_prefix)
        download_file(highcharts_url, resources_dir)

setup(name='js.highcharts',
      version='0.0',
      description='fanstatic Highcharts.js',
      classifiers=[],
      author='Hiroki KIYOHARA',
      author_email='hirokiky@gmail.com',
      url='',
      keywords='fanstatic',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points={
          'fanstatic.libraries':
              'highcharts = js.highcharts:library',
          },
      cmdclass={'install': install}
      )
