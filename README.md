# pypicrename
Small utility for renaming mobile and digital camera photos according to their time metadata.

## Development notes:

This program has been tested ONLY on Ubuntu MATE 18.04. It should work on a wider range of linux distributions but use at your own risk.

## Installation:

Running `install.sh` would place the python program in your path. As an option argument you can specify the path where you want the command to be, for example:
```
$ bash install.sh $HOME/bin
```
This would allow you to call it from anywhere from the command line.

## Usage:

This programe is intended to be used from the command line in the directory that contains the photos that are to be renamed.
Open a terminal at the folder in question and type `pypicrename` and all the photos in that folder will get renamed according to their metadata creation time.
The output format will be: `%Y%m%d_%H%M%S.jpg` If that filename already exists an `_X` will be added until `X` becomes an integer high enough that the filename is not already present.
