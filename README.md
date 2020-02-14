# kub-logging

This example performs the fllowing tasks:

1. Monitor containers logs (stdout,stderr) by fluentd product.
2 Transfer them to mongoDB for further storing.
3. Extract the logs from mongoDB to flat files that accessible for viewing through ngnix web server.It possible to view all logs for the last 7 days in the flat files.


All part of example are running on containers within kuberneteds platform.

This example assumes that you already have kubernetis running and properly functioning.

For preparing this example i used microk8s platform.
For simulating log activity i Used dummy images from public hub repository. These images generate dummy logs every few seconds.

The folder fluentd-image containes a docker file and default fluentd configuration for building fluentd custom image with mongodb plugin.
The folder exctract_logs_image containes a docker file and other custom scripts for building custom nginx image with python script which performs for extracting logs from the mongodb to the flat files.

# Install steps:

1. kubectl apply -f log-generator.yml # create  a deployment with 2 replicas of dummy log generators images
2. kubectl apply -f mongo-volume.yml # create a local persistent volume for mongodb container
3. kubectl apply -f mongodb.yml # create a statefullset of one container running mongodb instance  with db is stored on the node's persistent storage
4. kubectl apply -f fluent.yml # create a daemonSet  running custom fluentd container   which monitors containers logs, tags them and stores in the mongodb
