# -*- coding: utf-8 -*-

# A simple setup script to create an executable using PyQt4. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# PyQt4app.py is a very simple type of PyQt4 application
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application

from cx_Freeze import setup, Executable

includes = ['atexit', 'lxml']
excludes = ['collections.abc', 'tkinter']	
packages = ['lxml']
	
options = {
    'build_exe': {
        'includes': includes,
		"excludes": excludes,
		'packages': packages
    }
}

executables = [
    Executable('amazon_framerate_updater.py', base='Win32GUI', icon="icon.ico")
]

setup(name='Amazon Framerate Updater',
      version='1.0',
      description='Updates framerates for Amazon MMCs',
      options=options,
      executables=executables
      )