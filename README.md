## Overview

See problem.txt for the original problem description.

This code was written in Python 3. The principle was to pretend that we may need the Account info for something besides inputting and outputting the CSV and also to show off that I know how to do unit tests.

##Libraries
I used the following libraries: 
```
argparse
csv
datetime
json
unittest
urllib
```
I believe all these libraries come with the standard install of Python 3.

##Instructions
Clone the repositiory. Enter the directory you place the repository. To run unit tests, run: 
```
$ python3 -m unittest
```

To run the program itself, run 
```
python3 account/main.py [filepath]
```
An output file will be created with the suffix of "-status". So if your input file is /bar/foo/chaz.csv, your output file will be /bar/foo/chaz-status.csv

##Caveats
Program assumes the file is correctly formatted as described in the problem description. Unit tests are not as decoupled as we'd ideally liked. As a result they assume that `https://interview.wpengine.io/v1/accounts/` is accessible from the computer that will run it. Since I was trying to get this to you at a reasonable time, the Single Responsibility Principle was broken (For example, the Account class does some date parsing/formatting).
