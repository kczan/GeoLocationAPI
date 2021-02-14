#Sofomo GeoLocationAPI

Live version available here: https://geolocationapi-fc.herokuapp.com/api/geolocate/

credentials:

- username: filip
- password: geolocation

to use API via i.e Postman, make sure you're not requesting from localhost and mock the server IP.

Get your JWT token using endpoint /api/token/

GET, POST and DELETE requests should be sent to /api/geolocate/

## To run locally using docker:
- cd into repo directory
- run `docker-compose up -d --build`
- api now runs locally at **0.0.0.0:1337/api/geolocate/**
