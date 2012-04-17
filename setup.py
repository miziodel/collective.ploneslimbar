from setuptools import setup, find_packages
import os

version = '1.0'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='collective.ploneslimbar',
      version=version,
      description="slimbar for listing local communities sites",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone",
        "Topic :: Software Development :: Libraries :: Python Modules"
        ],
      keywords='plone',
      author='Maurizio Delmonte, Abstract',
      author_email='maurizio.delmonte@abstract.it',
      url='http://github.com/collective/collective.ploneslimbar',
      license='gpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      extras_require={'test': ['plone.app.testing']},
      entry_points="""
      # -*- Entry points: -*-
  	  [z3c.autoinclude.plugin]
  	  target = plone
      """,
      )
