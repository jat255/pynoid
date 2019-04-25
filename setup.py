import setuptools

setuptools.setup(name='pynoid',
                 version='0.1.1',
                 description="A simple minter for opaque identifiers inspired "
                             "by California Digital Library's NOID.",
                 author='t. johnson',
                 author_email='thomas.johnson@oregonstate.edu',
                 py_modules=['pynoid'],
                 scripts=['pynoid.py'],
                 test_suite='test'
                 )
