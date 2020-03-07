from setuptools import find_packages, setup
from pyjuzi import __version__

setup(
    name='pyjuzi',
    version=__version__,
    license='PRIVATE',
    author='fatelei',
    author_email='fatelei@gmail.com',
    url='https://github.com/fatelei/pyjuzi',
    description='juzi python sdk',
    packages=find_packages(where='.', exclude=['tests', 'scripts']),
    zip_safe=False,
)
