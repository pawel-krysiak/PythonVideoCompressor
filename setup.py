#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import codecs, os

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
   name='python_video_compressor',
   version='1.0',
   description='Compresses all .mp4 Video files in given directory using ffmpeg',
   long_description=read("README.md"),
   keywords='video compressor ffmpeg mp4',
   author='Paweł Krysiak',
   url='https://github.com/pawel-krysiak/PythonVideoCompressor',
   packages=['python_video_compressor'],  #same as name
#    install_requires=['bar', 'greek'], #external packages as dependencies
   scripts=['bin/python_video_compressor'],
   license="BSD",
   classifiers=[
       "Development Status :: 1 - Alpha",
       "Operating System :: OS Independent",
       "Programming Language :: Python",
   ],
   zip_safe=False
)