from setuptools import setup

setup(
    name='bb2moodle',
    version='1.0.0',
    description=' Blackboard to Moodle',
    packages=['bb2moodle'],
    package_data={'bb2moodle': ['moodle.xml.template']},
    include_package_data=True,
    zip_safe=False,
    author='',
    author_email='',
    url='',
    license='GPL v3',
    platforms=['any'],
    keywords=['blackboard', 'moodle', 'migration', 'lms'],
    install_requires=['lxml', 'jinja2'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License (GPL)'
    ],
    long_description=' Blackboard to Moodle',
    entry_points={
        "console_scripts": [
            "bb2moodle = bb2moodle.main:main",
        ]
    },
)
