#!/usr/bin/env python
"""pymatsolver: Matrix Solvers for Python

pymatsolver is a python package for easy to use matrix solvers.

"""

from setuptools import find_packages

# NOTE:
# numpy.distutils is deprecated because distutils is being removed in Python 3.12.
# However, using it is the fastest way to get us a working Mumps extension distributed.
# Once that's in use, we can figure out a long-term distribution solution.
from numpy.distutils.core import Extension, setup


mumps_extension = Extension(
    name = "pymatsolver.mumps.MumpsInterface",
    sources = [
        "pymatsolver/mumps/MumpsInterface.pyf",  # auto-generated wrapper from `make wrapper`
        "pymatsolver/mumps/mumps_interface.f90",
        "pymatsolver/mumps/mumps_p.f90",
        "pymatsolver/mumps/mumps_cmplx_p.f90",
    ],
    include_dirs=[
        # this isn't on gfortran's default include path!!
        "/usr/include",
    ],
    libraries=[
        "zmumps", "dmumps", "mumps_common", "mpiseq", "blas", "pord",
    ],
    library_dirs=[
        "/usr/lib"
    ],
    extra_f90_compile_args=[
        "-fcray-pointer", "-fPIC",
    ],
)

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Mathematics',
    'Topic :: Scientific/Engineering :: Physics',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    'Operating System :: Unix',
    'Operating System :: MacOS',
    'Natural Language :: English',
]

with open("README.rst") as f:
    LONG_DESCRIPTION = ''.join(f.readlines())

setup(
    name="pymatsolver",
    version="0.2.0",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        'numpy>=1.7',
        'scipy>=0.13',
    ],
    author="Rowan Cockett",
    author_email="rowanc1@gmail.com",
    description="pymatsolver: Matrix Solvers for Python",
    long_description=LONG_DESCRIPTION,
    license="MIT",
    keywords="matrix solver",
    url="http://simpeg.xyz/",
    download_url="http://github.com/simpeg/pymatsolver",
    classifiers=CLASSIFIERS,
    platforms=["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
    ext_modules=[mumps_extension],
)
