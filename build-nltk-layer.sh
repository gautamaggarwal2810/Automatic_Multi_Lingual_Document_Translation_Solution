

#!/bin/sh
curl -O https://bootstrap.pypa.io/get-pip.py
python3.8 get-pip.py --user
mkdir python
python3.8 -m pip install nltk -t python/
pip install nltk
python3 -m nltk.downloader punkt -d ./nltk_data/
zip -r layer.zip python nltk_data
aws lambda publish-layer-version --layer-name nltk-layer --zip-file fileb://layer.zip --compatible-runtimes python3.8 --region us-east-1
