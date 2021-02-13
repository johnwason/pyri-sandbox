from setuptools import setup, find_packages, find_namespace_packages

setup(
    name='pyri-sandbox',
    version='0.1.0',
    description='PyRI Teach Pendant User Software Sandbox',
    author='John Wason',
    author_email='wason@wasontech.com',
    url='http://pyri.tech',
    package_dir={'': 'src'},
    packages=find_namespace_packages(where='src'),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pyri-common'
    ],
    tests_require=['pytest','pytest-asyncio'],
    extras_require={
        'test': ['pytest','pytest-asyncio']
    },
    entry_points = {
        'pyri.plugins.robdef': ['pyri-sandbox-robdef=pyri.sandbox.robdef:get_robdef_factory'],
        'console_scripts': ['pyri-sandbox-service = pyri.sandbox.__main__:main'],
        'pyri.plugins.sandbox_functions': ['pyri-robotics-sandbox-functions=pyri.sandbox.sandbox_functions:get_sandbox_functions_factory']
    }
)