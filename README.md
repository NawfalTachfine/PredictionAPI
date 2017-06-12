# PredictionAPI
This is a tutorial on serving predictions from a machine learning model through a REST API.

A version of this tutorial was presented in the [PyParis](pyparis.org) conference on 13/06/2017.

## Steps
1. training and persisting the model on disk,
2. reproducing the pre-processing pipeline in the API application,
3. encapsulating the application in a Docker container,
4. deploying the application to a cloud server.

# Technical Requirements
+ Python 3 and virtualenv
+ Docker
+ The required Python librairies used can be installed from the included *requirements.txt* file:
```bash
  virtualenv -p python3 pyenv
  source pyenv/bin/activate
  pip install -r requirements.txt
```
