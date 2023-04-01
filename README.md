# git-fails
Mock common problematic/tricky git scenarios using real repos.


## Install
Create a virtualenv, clone the repo, install the package:
```
conda create -n gitfails-env python=3.10
pip install -e ."[dev]"
```


## Usage
The top-level command is `gitfails`

### List pre-defined scenarios
```
gitfails sc list
```

### Set the top-level working directory (in which repos are created)
```
gitfails set-working-dir <path/to/working/dir>
```

### Construct a scenario
```
gitfails sc create <name>
```

### Cleanup by removing all scenarios
WARNING: this deletes all repos/files in the working directory.
```
gitfails cleanup
```
