# Install Google Cloud SDK

## Steps

- Installer will run `gcloud init` upon installation
  - Authenticate with your Google account (e.g. mmckelve@illinois.edu)
  - Choose project: **everydaycomputingorg**
  - Don't set default Google Compute Engine zone
- Install Python 2.7
  - *NOTE: dev_appserver.py + webapp2 don't work with Python 3; need to start using a framework like Django or Flask to route requests instead of URL handlers in app.yaml -- https://cloud.google.com/appengine/docs/standard/python/migrate-to-python3/*
  - [X] Add python.exe to Path
- To add Python components to Google Cloud, run the following commands:
  - `gcloud components install app-engine-python`
  - `gcloud components install app-engine-python-extras`
