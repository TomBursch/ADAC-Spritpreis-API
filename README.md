<h1 align="center">
  ADAC-Spritpreis-API
</h1>
<p align="center">
  <a href="https://github.com/TomBursch/kitchenowl">
    <img alt="Stars" src="https://img.shields.io/github/stars/tombursch/ADAC-Spritpreis-API" />
  </a>
  <a href="LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/TomBursch/ADAC-Spritpreis-API" />
  </a>
  <a href="https://hub.docker.com/repository/docker/tombursch/kitchenowl">
    <img alt="Docker pulls" src="https://img.shields.io/docker/pulls/tombursch/adac-spritpreis-api" />
  </a>
</p>

## 🤖  Usage

Install using docker:

```
docker run -d -p 5000:5000 --name=adac-spritpreis --restart=unless-stopped tombursch/adac-spritpreis-api:latest
```

Search for gas stations here: https://www.adac.de/verkehr/tanken-kraftstoff-antrieb/kraftstoffpreise/

Click on show details and copy the station id. I.e the last part of the [domain](https://www.adac.de/verkehr/tanken-kraftstoff-antrieb/kraftstoffpreise/details/52066-aachen-aral/-1017401811/), `52066-aachen-aral/-1017401811/`.

The request `http://localhost:5000/details/52066-aachen-aral/-1017401811/` will now return a JSON respone with gas price details:
```
{
  "diesel": 1.469,
  "e10": 1.569,
  "super": 1.629
}
```

## 🔨 Built With

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Docker](https://docs.docker.com/)

## 📜 License

ADAC-Spritpreis-API is Free Software: You can use, study share and improve it at your will. Specifically you can redistribute and/or modify it under the terms of the Apache-2.0 License.
