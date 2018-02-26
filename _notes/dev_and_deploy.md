# Start the development server #
dev_appserver.py app.yaml

# Update App Engine #
gcloud app deploy app.yaml --project everydaycomputingorg





Set Credentials for Remote API
================================================================================
The .json file was downloaded from the console

```
export GOOGLE_APPLICATION_CREDENTIALS=/Users/tbinkowski/Development/GitHub/EverydayComputing/everydaycomputing.org/EverydayComputingOrg-a3501e320e92.json
```

Download the Datastore
================================================================================
Hits the live datastore and pulls in down to data.sql3 file.

```
export GOOGLE_APPLICATION_CREDENTIALS=./EverydayComputingOrg-a3501e320e92.json

 /Applications/google-cloud-sdk/platform/google_appengine/appcfg.py download_data --application=everydaycomputingorg --url=http://everydaycomputingorg.appspot.com/_ah/remote_api --filename=data.sql3
```

Upload the Datastore Backup to Local Development Server
================================================================================
You have to start the server to upload to the API.

```
dev_appserver.py --clear_datastore=yes app.yaml
```

Sometimes it doesn't completely load all the data.  Workaround is to use an accessed token.
```
gcloud auth login
gcloud auth print-access-token
```


```
appcfg.py upload_data  --oauth2_access_token=<oauth2_access_token> --filename=data_updated.sql3
--application=dev~everydaycomputingorg
--url=http://localhost:58151/_ah/remote_api
```
