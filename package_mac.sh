#!/bin/bash
pyinstaller -F --add-data "static:static" --add-data "minerva-story:minerva-story" --add-data "$CONDA_PREFIX/lib/python3.10/site-packages/altair/vegalite/v4/schema:altair/vegalite/v4/schema" --add-data "$CONDA_PREFIX/lib/python3.10/site-packages/xmlschema/schemas:xmlschema/schemas" --add-data "$CONDA_PREFIX/lib/python3.10/site-packages/ome_types:ome_types" src/app.py
