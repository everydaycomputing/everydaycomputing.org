deploy:
	gcloud app deploy app.yaml --project gene-tree

download:
	e

upload_local_database:
	appcfg.py upload_data \
		--filename=data.sql3 \
		--application=dev~everydaycomputingorg \
		--num_threads=1 \
		--url=http://localhost:53814/_ah/remote_api 

local:
	dev_appserver.py .