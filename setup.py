from setuptools import setup


setup(
    name='clipperz',
    version='0.1.0',
    url='http://github.com/clipperz/password-manager/',
    author='Jokajak',
    install_requires=['Flask>=0.10.1',
                      'Flask-SQLAlchemy>=1.0',
                      'SQLAlchemy>=0.8.2',
                      'SQLAlchemy-migrate',
                      'Flask-Login',
                      'Flask-KVSession',
                      ],
    author_email='jokajak+clipperz@gmail.com',
    description='Clipperz password manager server',
    packages=['clipperz'],
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
