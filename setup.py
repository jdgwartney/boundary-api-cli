from distutils.core import setup
setup(
    name='boundary',
    version='0.0.2',
    url="https://github.com/boundary/boundary-api-cli",
    author='David Gwartney',
    author_email='davidg@boundary.com',
    packages=['boundary',],
    scripts=[
      'bin/action-list',
      'bin/hostgroup-create',
      'bin/hostgroup-delete',
      'bin/hostgroup-get',
      'bin/hostgroup-list',
      'bin/hostgroup-update',
      'bin/measurement-add',
      'bin/metric-create',
      'bin/metric-export',
      'bin/metric-get',
      'bin/metric-import',
      'bin/metric-list',
      'bin/metric-markdown',
      'bin/plugin-add',
      'bin/plugin-install',
      'bin/plugin-installed',
      'bin/plugin-remove',
      'bin/plugin-uninstall',
      'bin/relay-list',
      'bin/user-get',
    ],
    license='LICENSE.txt',
    description='Command line interface to Boundary REST APIs',
    long_description=open('README.txt').read(),
    install_requires=[
        "requests >= 2.3.0",
    ],
)

