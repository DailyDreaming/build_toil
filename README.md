# build_toil
A script to build Toil from source.

To build a new master branch in the current working directory, run::

    python build_toil.py

To build a new branch with the name 'betterToilDebugging' in the current working directory, run::

    python build_toil.py -b betterToilDebugging

To activate the virtualenv (assuming you are still in the same current working directory the file was run from)::

    source toil/venv/bin/activate

Link to Toil: https://github.com/BD2KGenomics/toil