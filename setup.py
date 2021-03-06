# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

version = '1.1b2.dev0'
long_description = (
    open('README.rst').read() + '\n' +
    open('CONTRIBUTORS.rst').read() + '\n' +
    open('CHANGES.rst').read()
)

setup(name='collective.behavior.localdiazo',
      version=version,
      description='Dexterity behavior to enable a local Diazo theme.',
      long_description=long_description,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Framework :: Plone',
          'Framework :: Plone :: 4.3',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Topic :: Office/Business :: News/Diary',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='plone registry local behavior dexterity diazo',
      author='Simples Consultoria',
      author_email='products@simplesconsultoria.com.br',
      url='https://github.com/collective/collective.behavior.localdiazo',
      license='GPLv2',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['collective', 'collective.behavior'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'collective.behavior.localregistry',
          'plone.app.registry',
          'plone.app.theming >=1.1',
          'plone.autoform',
          'plone.behavior',
          'plone.registry',
          'Products.CMFCore',
          'Products.CMFPlone >=4.3',
          'setuptools',
          'zope.component',
          'zope.i18nmessageid',
          'zope.interface',
          'zope.schema',
      ],
      extras_require={
          'develop': [
              'manuel',
              'setuptools-flakes',
              'Sphinx',
          ],
          'test': [
              'interlude',
              'plone.app.dexterity',
              'plone.app.testing',
              'plone.dexterity',
              'plone.testing',
              'unittest2',
          ]
      },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
