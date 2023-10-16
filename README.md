# FastAPI template repository

This repository contains a minimal structure to start a FastAPI project, including a project skeleton, a Docker configuration and a CI with GitHub Actions. 

It is meant to be used as a [repository template](https://docs.github.com/repositories/creating-and-managing-repositories/creating-a-template-repository).

## Quickstart

### CLI

**Install dependencies**:
`$ pip install -r requirements.txt`

**Start**:
`$ python app/main.py`


### Docker

**Build and start** :
`$ docker run -it $(docker build -q .)`


## Testing

**Launch Unit tests**: `$ python -m unittest`

## Configuration
**Specifying port**: `$ PORT=3000 python app/main.py`


> Template created by [Alexis Tonneau](https://github.com/AlexisTonneau)