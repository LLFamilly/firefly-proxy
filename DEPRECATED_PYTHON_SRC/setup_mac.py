"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['main.py']
DATA_FILES = [
    'config.json',
    'firefly-blacklist.txt',
    'firefly-blacklist.meta.json',
    'firefly-hosts.txt',
    'firefly-hosts.meta.json',
    'firefly-hosts-disabled.txt',
    'custom-blacklist.txt',
    'custom-whitelist.txt',
    'meek-relays.txt',
    'cacert.pem',
    'README.md',
    'LICENSE',
    ('webpanel', ['webpanel/static', ]),
    ('webpanel', ['webpanel/templates', ])
]
OPTIONS = {
    'iconfile': 'firefly.icns',
    'plist': {'CFBundleShortVersionString':'0.3.0',},
    'argv_emulation': True
}

setup(
    name="Firefly",
    version="0.3.0",
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
