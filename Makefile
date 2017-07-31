deploy:
	gcloud app deploy app.yaml --project gene-tree

download:
	appcfg.py download_data --application=everydaycomputingorg --url=everydaycomputingorg.appspot.com/_ah/remote_api --filename=data.sql3

upload_local_database:
	appcfg.py upload_data \
		--filename=data.sql3 \
		--application=dev~everydaycomputingorg \
		--num_threads=1 \
		--url=http://localhost:53814/_ah/remote_api 

local:
	./../google-cloud-sdk/platform/google_appengine/dev_appserver.py .