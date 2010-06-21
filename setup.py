from setuptools import setup, find_packages

setup(
    name = "django-mailpers",
    version = "0.1",
    url = 'http://github.com/bluszcz/django-mailpers',
    license = 'Simplified BSD License',
    description = "SMTP / Email helpers for Django apps.",
    author = 'Rafal bluszcz Zawadzki',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)
