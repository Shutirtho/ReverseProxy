# ReverseProxyServer App

This application was built and packaged using Mac OS X El Captain version 10.11.6 and Docker for Mac.

This app assumes that you have Docker running in your system.

To run this reverse proxy server application:
Execute this from the parent folder of ReverseProxy folder --> ./ReverseProxy/run.sh

The server application can be accessed at http://localhost:9999 

If you are running the application server on a virtual machine using Docker Toolbox, connect to the server at the IP of your docker machine. You can find this IP with the following command : docker-machine ip.

Cleanup after executing the server application : 
docker container ls <br />
docker container stop [container id](for image = techallenge)<br />
docker container rm [container id](for image = techallenge) <br />
docker image ls <br />
docker image rmi [imgae ids] [imge id1 image id2] (for image = techallenge and image=python) <br />

Tools Used:
Flask Webframework
Docker for Mac https://docs.docker.com/docker-for-mac/

Nexbus's Documentation referred:
http://www.nextbus.com/xmlFeedDocs/NextBusXMLFeed.pdf

