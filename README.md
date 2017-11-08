# ReverseProxyServer App

This application was built and packaged using Mac OS X El Captain version 10.11.6 and Docker for Mac - Docker version 17.09.0-ce, build afdb6d4.<br />
This app assumes that you have Docker running in your system.

To run this reverse proxy server application: <br />
Execute this in the terminal from the parent folder of ReverseProxy folder --> <br />./ReverseProxy/run.sh<br /> <br />

The server application can be accessed at http://localhost:9999/stats <br /> <br />

For getting logs of the container running the application use the following commands : <br />
docker container ls <br />
docker logs [container id](for image = techallenge) <br /> <br />


If you are running the application server on a virtual machine using Docker Toolbox, connect to the server at the IP of your docker machine. You can find this IP with the following command : docker-machine ip.<br /> <br />

Cleanup after executing the server application : <br />
docker container ls <br />
docker container stop [container id](for image = techallenge)<br />
docker container rm [container id](for image = techallenge) <br />
docker image ls <br />
docker image rmi [image ids] [imge id1 image id2] (for image = techallenge and image = python) <br />

Tools Used: <br />
Flask web framework <br />
Docker for Mac https://docs.docker.com/docker-for-mac/ <br /> <br />

Nextbus's Documentation referred: <br />
http://www.nextbus.com/xmlFeedDocs/NextBusXMLFeed.pdf

