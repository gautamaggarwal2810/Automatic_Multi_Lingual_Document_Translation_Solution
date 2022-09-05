
#!/bin/sh
destbucket=$1
mkdir -p artifacts/amazon-translate-a2i-workflow/
cd artifacts/amazon-translate-a2i-workflow/
s3bucket='s3://aws-ml-blog/artifacts/amazon-translate-a2i-workflow/'
cwd=$(pwd)
echo $cwd
aws s3 cp $cwd s3://$destbucket/artifacts/amazon-translate-a2i-workflow/ --recursive
