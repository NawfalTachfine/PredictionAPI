# PredictionAPI
This is a tutorial on serving predictions from a machine learning model through a REST API.

A version of this tutorial was [presented](http://slides.com/nawfaltachfine/prediction-api-pyparis-13062017/fullscreen) in the [PyParis](http://pyparis.org/talks.html#6629bc50a989d669b4b056d77b55c978) conference on 13/06/2017.

A complete written version is currently in the making.

## Steps
1. training and persisting the model on disk (cf. *modeling.ipynb*),
2. reproducing the pre-processing pipeline in the API application (cf. *application.py*),
3. encapsulating the application in a Docker container (cf. *Dockerfile*),
4. deploying the application to a cloud server.

## Technical Requirements
+ Python 3.5+ and virtualenv,
+ Docker,
+ The required Python librairies used can be installed from the included *requirements.txt* file:
```bash
virtualenv -p python3 pyenv
source pyenv/bin/activate
pip install -r requirements.txt
```

## Running the application locally
### Directly
```bash
cd PredictionAPI
export FLASK_APP=application.py
python3 -m flask run
```

### On Docker
```bash
cd PredictionAPI
docker build -t prediction-api .
docker run -d -p 5000:5000 prediction-api
```

### Testing the application
Once it is running, the API can be queried using HTTP POST requests.
I recommend using [postman](https://www.getpostman.com/) for testing.

URL: `http://0.0.0.0:5000/api/v1.0/aballone`

Here is a sample query:
```json
{    
  "inputs": [
    {
      "sex":"M",
      "length": 0.815000,
      "diameter": 0.055000,
      "height": 1.130000,
      "whole_weight": 2.825500,
      "shucked_weight": 1.488000,
      "viscera_weight": 0.760000,
      "shell_weight": 0.001500
    },
    {
      "sex":"F",
      "length": 0.815000,
      "diameter": 1.055000,
      "height": 1.130000,
      "whole_weight": 2.825500,
      "shucked_weight": 1.488000,
      "viscera_weight": 1.760000,
      "shell_weight": 0.001500
    }
  ]
}
```

The response should look like this:
```json
{
  "outputs": [
    {
      "label": 1,
      "prob": 0.109
    },
    {
      "label": 1,
      "prob": 0.183
    }
  ]
}
```
