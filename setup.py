from setuptools import setup, find_packages
setup(
    name = "django-insensitive",
    version = "0.1.0",
    packages = find_packages(),
    author = "George Ma",
    author_email = "george.ma1982@gmail.com",
    description = "A companion login backend for django-registration. django-registration checks user name duplicacy in a case insensitive way. However, it doesn't provide a user name case insensitive login backend, which is inconsistent. This login backend is a perfect companion with django-registration.",
    long_description = open('README').read(),
    license = "BSD",
    keywords = "django,login,case-insensitive",
    url = "https://github.com/georgema1982/django-insensitive",
    include_package_data=True,
    zip_safe=False,
)

