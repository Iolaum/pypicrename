#!/usr/bin/env bash

# Watch your terminal output when installing.
# More things can go wrong than the ones tested here.
# They should be easy to fix.

# Check if an argument exists
# https://stackoverflow.com/a/6482403/1904901
cpath=$HOME/.local/bin
if [ -z "$1" ]
  then
    echo "No 'installation' directory supplied, using default:"
    echo "$cpath"
else
    cpath=$1
fi

# check if the directoty is in the users $PATH
# https://stackoverflow.com/a/1397670/1904901
if [[ "$PATH" == ?(*:)"$cpath"?(:*) ]]; then
    echo "Target directory found in users \$PATH variable, proceeding."
else
    echo "$cpath is not in user's \$PATH, aborting!"
    exit 1
fi

# "Install command"
cp pypicrename.py $cpath/pypicrename
chmod ug+x $cpath/pypicrename

echo "pypicrename is now in your path and can be called."
exit
