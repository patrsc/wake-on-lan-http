# Wake on LAN HTTP

CLI and HTTP interface to use Wake on LAN for multiple configured devices.

Allows you to turn on, turn off and check state (on, off) for multiple devices in your network.
Note that if the HTTP API is exposed to your network anyone in the network can turn on and off your devices. Consider adding an additional layer of security, e.g. user authentication on your web server.

## Requirements

[Python](https://www.python.org/) 3.13 and [Poetry](https://python-poetry.org/).

## Installation

Clone repository and run:

```
poetry install
```

## Configuration

Copy devices template:

```
cp devices-template.json devices.json
```

Edit the file `devices.json` to add your devices.

## CLI usage

Turn a device (e.g. `server`) on:

```
poetry run python cli.py server on
```

Turn a device off:

```
poetry run python cli.py server on
```

Check the state of a device:

```
poetry run python cli.py server state
```

## API usage

Start API:

```
poetry run fastapi dev api.py
```

Open http://127.0.0.1:8000/ for the simple web interface or http://127.0.0.1:8000/docs for the API docs.
