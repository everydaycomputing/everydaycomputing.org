Start the Development Server
================================================================================
Start the default server.

```
dev_appserver.py app.yaml
dev_appserver.py --clear_datastore=yes app.yaml
```

Start the backend tools (by itself).
```
dev_appserver.py dispatch.yaml backend-tools.yaml
```

This was for the modules version (its somewhere in the git repo, possibly
  before the first big merge with dev (August 2, 2016)
```
dev_appserver.py dispatch.yaml app.yaml mobile_frontend.yaml static_backend.yaml admin.yaml
```

## Kill the dev server ##
Sometimes you need to kill some processes on a given port:
```
lsof -P | grep '8080' | awk '{print $2}' | xargs kill -9
```


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
/Applications/google-cloud-sdk/platform/google_appengine/appcfg.py
appcfg.py download_data --application=everydaycomputingorg --url=http://everydaycomputingorg.appspot.com/_ah/remote_api --filename=data.sql3
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

## Examples that Work ##
Single service
```
 /Applications/google-cloud-sdk/platform/google_appengine/appcfg.py upload_data --filename=data.sql3 --application=dev~everydaycomputingorg --url=http://localhost:52900/_ah/remote_api --oauth2_access_token=ya29.Glz8A5pSeSMRAcZugWcS4fOgZi1OnGEPSMXdPvQlLynQQ2IHLvni6EiOF4CIz10gAn0WPhiS1EsZEFj6F17tvUC_GcQqJjWipMB2cVZVdwVCqjBvwC8YYnNbexOHDg
 ```

With microservice architecture you do not need to specify the application (see format above).  It doesn't work.  I don't know why.
```
 /Applications/google-cloud-sdk/platform/google_appengine/appcfg.py upload_data --filename=data.sql3
 --url=http://localhost:62342/_ah/remote_api --oauth2_access_token=ya29.Glz8A5pSeSMRAcZugWcS4fOgZi1OnGEPSMXdPvQlLynQQ2IHLvni6EiOF4CIz10gAn0WPhiS1EsZEFj6F17tvUC_GcQqJjWipMB2cVZVdwVCqjBvwC8YYnNbexOHDg
```
or with different data file:
```
 /Applications/google-cloud-sdk/platform/google_appengine/appcfg.py upload_data --filename=data_20170806.sql3  
 --url=http://localhost:52249/_ah/remote_api --oauth2_access_token=ya29.Glz8A5pSeSMRAcZugWcS4fOgZi1OnGEPSMXdPvQlLynQQ2IHLvni6EiOF4CIz10gAn0WPhiS1EsZEFj6F17tvUC_GcQqJjWipMB2cVZVdwVCqjBvwC8YYnNbexOHDg
```

Update App Engine Server
================================================================================
The following updates a server that is using a single default service defined in
app.yaml file.  

`cd` to the directory containing everydaycomputing.org/
  (probably ~/Development/GitHub)

```
cd ~/Development/GitHub
 /Applications/google-cloud-sdk/platform/google_appengine/appcfg.pyc update everydaycomputing.org/
appcfg.py update everydaycomputing.org/
```

## Public site ##
Note that almost everything is on the public site.
```
/Applications/google-cloud-sdk/platform/google_appengine/appcfg.py update app.yaml -A everydaycomputingorg -V 2-0-tweet
```

History:
* /Applications/google-cloud-sdk/platform/google_appengine/appcfg.py update app.yaml -A everydaycomputingorg -V 1

## FOR MICROSERVICE ##
> Microservices are deprecated for simplicity 8/2017.
```
 /Applications/google-cloud-sdk/platform/google_appengine/appcfg.py update backend-tools.yaml -A everydaycomputingorg -V 0
```


## Update Cron Jobs ##
```
gcloud app deploy cron.yaml
````


Post from Command Line
====================================================================================================
curl -XPOST -H "Content-Type: application/json" --data @test.json http://localhost:8081
