# SFZBuilder

[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=TriYop_folder2sfz&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=TriYop_folder2sfz)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=TriYop_folder2sfz&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=TriYop_folder2sfz)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=TriYop_folder2sfz&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=TriYop_folder2sfz)
![CodeQL](https://github.com/TriYop/sfzbuilder/actions/workflows/codeql-analysis.yml/badge.svg)

SFZBuilder is a python port of the Versilian Studio's folderToSFZ tool.
It aims to automate SFZ sound banks creation using sample filenames naming convention.

---

## How to use it ?

    usage: python3 folder2sfz.py [-h] path
    
    Builds a SFZ from a directory containing samples
    
    positional arguments:
      path        path to the samples directory
    
    optional arguments:
      -h, --help  show this help message and exit

more information available in [documentation](doc/index.md)
