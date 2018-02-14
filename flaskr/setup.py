from distutils.core import setup

setup(
    author="Unknown",
    author_email="no@no.no",
    name="flaskr",
    version="1.0.0.0",
    url="localhost",
    packages=['flaskr','flaskr.Models'],
    include_package_data = True,
    install_requires = [
        'flask',
        'flask_sqlalchemy',
        'psycopg2'
    ]
)11