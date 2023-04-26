# SFZBuilder

[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=TriYop_folder2sfz&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=TriYop_folder2sfz)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=TriYop_folder2sfz&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=TriYop_folder2sfz)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=TriYop_folder2sfz&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=TriYop_folder2sfz)
![CodeQL](https://github.com/TriYop/sfzbuilder/actions/workflows/codeql-analysis.yml/badge.svg)

SFZBuilder is a python port of the Versilian Studio's folderToSFZ tool.
It aims to automate SFZ sound banks creation using sample filenames naming convention.

---

## How to use it ?

    usage: SFZBuilder.py [-h] -i PATH [-o OUTPUT] [-d] [-l] [-v]

Builds a SFZ from a directory containing samples

optional arguments:
  -h, --help            show this help message and exit
  -i PATH, --input-dir PATH
                        path to the samples directory
  -o OUTPUT, --output-file OUTPUT
                        path to the output file
  -d, --drums           enhance generated soundfont for drums
  -l, --looping         try to identify looping points
  -v, --verbose         Display verbose output

more information available in [documentation](doc/index.md)

To read more about the origins of this project, please read [this article](https://blog.yvanjanet.net/2021/11/)

