#!/bin/bash
set -e
DIRECTION=source/chapters
mkdir $DIRECTION/$1
mkdir $DIRECTION/$1/img
touch $DIRECTION/$1/index.rst

echo "
$1
========

texto del capitulo

.. toctree::
   :maxdepth: 2
   :caption: Capítulos de $1:
" > $DIRECTION/$1/index.rst
