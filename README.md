# bayesian

Bayesian lessons, and tutorials.

Copyright 2018 onwards, Arpan P. Shah. Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. A copy of the License is provided in the LICENSE file in this repository.

## Current Status

This is a development and prototype version. 

Recommended installation approach is to clone bayesian using `git`:

```sh
git clone https://github.com/reacharpan/bayesian.git
```
Then, `cd` to the bayesian folder and create the python environment:

```sh
cd bayesian
conda env update environment.yml
```
This downloads all of the dependencies and then all you have to do is:

```sh
conda activate bayesian
```

To update everything at any time, cd to your repo and:

```sh
git pull
conda env update
```

You can also install this library in the local environment using ```pip```

```sh
pip install bayesian
```

However this is not currently the recommended approach, since pip needs to compile many libraries from scratch (which can be slow). 
