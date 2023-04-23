# FALCON PY REST API
https://falcon.readthedocs.io/en/stable/

##### INSTALL PYTHON 3.11.1
https://www.python.org/downloads/

##### INSTALL PIPENV
`pip install pipenv`

cd ./falcon_rest_api

##### CREATE 'VIRTUAL ENVIROMENT' AND 'Pipfile' FROM 'requirements.txt'
`pipenv shell`

##### INSTALL DEPENDENCY
`pipenv install`

##### INSTALL WAITRESS
`pip install waitress`

##### RUN APP
`waitress-serve --listen=127.0.0.1:3000 app:app`

##### URL: `http://127.0.0.1:3000/api/v1/{route}`

##### PING API: GET: `http://127.0.0.1:3000/api/v1/ping`
