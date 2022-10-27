# git-fails
Mock common problematic git scenarios using real repos.


## Install
Create a virtualenv, clone the repo, install the package:
```
git clone git@github.com/keithchev/git-fails
conda create -n gitfails-env python=3.10
pip install -e ."[dev]"
```


## Usage
The top-level command is `gitfail`.

### List pre-defined scenarios
```
gitfails list
```
